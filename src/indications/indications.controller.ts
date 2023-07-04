import { Controller, Get, Post, UseGuards, Body, Param, ParseIntPipe, ConflictException, InternalServerErrorException, Logger, Query, ForbiddenException, BadRequestException, NotFoundException, Res } from '@nestjs/common';
import { AddressesService } from 'src/addresses/addresses.service';
import { JwtAuthGuards } from 'src/auth/auth.jwt-guard';
import { UserID } from 'src/decorators';
import { PostIndicationRequest, PostIndicationTypeRequest} from './indications.pb'
import { IndicationsService } from './indications.service';
import { GrpcMethod } from '@nestjs/microservices';
import * as grpc from "@grpc/grpc-js";

@UseGuards(JwtAuthGuards)
@Controller('indication')
export class IndicationsController {
    
    private readonly logger = new Logger(IndicationsController.name);
    
    constructor(protected readonly indicationService: IndicationsService, protected readonly addressesService: AddressesService) {}

    @Post('type')
    async postIndicationType(@Body() indicationType: PostIndicationTypeRequest, @UserID() userID: number): Promise<void> {
        try {
            const grpcResponse = await this.indicationService.insertIndicationType({
                ...indicationType,
                userID: userID.toString(),
            });
            if (!grpcResponse.ok) {
                this.logger.error(grpcResponse.error)
                throw new ConflictException(grpcResponse.error)
            }
        } catch (e) {
            if (e instanceof ConflictException) throw e;
            this.logger.error(e);
            throw new InternalServerErrorException();
        }
    }
    
    @Get('type')
    async getIndicationTypes(@Query('addrID', ParseIntPipe) addressID: string, @UserID() userID: number) { // addressID should be string type. Because number type will represent empty string as 0. 
        // check whether addressID belong to the user
        if (!this.addressesService.isPersonalAddress(parseInt(addressID), userID)) throw new ForbiddenException(`User doesn't has addrID=${addressID}. Access denied.`)
        const res = await this.indicationService.getIndicationTypes(
            {
                addressID: parseInt(addressID),
                maxQuantity: 0 // 0 means all
            }
        )
        // check whether response is successful
        if (res.ok) {
            return res.value
        } else {
            this.logger.error(res.error);
            throw new BadRequestException('Bad request');
        }
    }

    @Post(':typeID')
    async postIndication(@Param('typeID') typeID: string, @Body() indication: Omit<PostIndicationRequest, "indicationTypeID" | "userID">, @UserID() userID: number): Promise<void> {
        // check whether indicationTypeID belong to the user
        const isPersonalTypeID = await this.indicationService.isPersonalTypeID(userID.toString(), typeID);
        if (!isPersonalTypeID.ok) {
            this.logger.error(isPersonalTypeID.error);
            throw new NotFoundException();
        }
        
        // Make the RPC to insert new indication to provided typeID
        const data: PostIndicationRequest = {
            ... indication,
            indicationsTypeID: typeID,
            userID: userID.toString(),
        }
        const serviceResponse = await this.indicationService.insertIndication(data);
        if (!serviceResponse.ok) {
            switch (serviceResponse.error.code) {
                case (grpc.status.ALREADY_EXISTS):
                    throw new ConflictException('Current month already recorded');
                default:
                    this.logger.error(serviceResponse.error);
            }
        }
    }

    @Get(':typeID')
    async getIndications(@Param('typeID') typeID: string, @UserID() userID: number) {
        // check whether indicationTypeID belong tp the user
        const isPersonalTypeID = await this.indicationService.isPersonalTypeID(userID.toString(), typeID)
        if (!isPersonalTypeID.ok) {
            this.logger.error(isPersonalTypeID.error);
            return new NotFoundException();
        }
        // Make RPC to fetch indications by provided typeID
        const serviceResponse =  await this.indicationService.getIndicaiotns({
            indicationTypeID: typeID,
            maxQuantity: 0 // 0 means all
        })
        if (!serviceResponse.ok) {
            switch (serviceResponse.error.code) {
                case(grpc.status.NOT_FOUND):
                    throw new NotFoundException(`There's no such data`)
                default:
                    this.logger.error(serviceResponse.error)
            }   
        } else {
            return serviceResponse.value
        }
    }

}
