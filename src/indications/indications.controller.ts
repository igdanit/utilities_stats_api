import { Controller, Get, Post, UseGuards, Body, Param } from '@nestjs/common';
import { JwtAuthGuards } from 'src/auth/auth.jwt-guard';
import { UserID } from 'src/decorators';
import { PostIndicationRequest, PostIndicationTypeRequest} from './indications.pb'
import { IndicationsService } from './indications.service';

@UseGuards(JwtAuthGuards)
@Controller('indications')
export class IndicationsController {

    constructor(private readonly indicationService: IndicationsService) {}

    @Post(':typeID')
    async postIndication(@Param('typeID') typeID: string,@Body() indication: Omit<PostIndicationRequest, 'indicationsTypeID'>, @UserID() userID: number) {
        
        let data = {
            indicationsTypeID: typeID,
            indication: indication.indication,
            createdAt: indication.createdAt
        }

        console.log(data)
        
        return await this.indicationService.insertIndication(data)
    }

    @Get(':typeID')
    async getIndications(@Param('typeID') typeID: string, @UserID() userID: number) {
        return await this.indicationService.getIndicaiotns({
            indicationTypeID: typeID,
            maxQuantity: 0 // 0 means all
        })
    }

    @Post('type')
    async postIndicationType(@Body() indicationType: PostIndicationTypeRequest, @UserID() userID: number) {
    }

    @Get('type/:addressID')
    async getIndicationTypes(@Param('addressID') addressID: string, @UserID() userID: number) {
        return await this.indicationService.getIndicationTypes(
            {
                addressID,
                maxQuantity: 0 // 0 means all
            }
        )
    }
}
