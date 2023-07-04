import { Controller, Get, Body, Post, UseGuards, Delete, Param, Put, ForbiddenException, ParseIntPipe } from '@nestjs/common';
import { JwtAuthGuards } from 'src/auth/auth.jwt-guard';
import { UserID } from 'src/decorators';
import { AddressesService } from './addresses.service';
import { Address } from '@prisma/client';

@UseGuards(JwtAuthGuards)
@Controller('address')
export class AddressesController {

    constructor(private readonly addressService: AddressesService) {}

    @Get()
    async getAddresses(@UserID() userID: number): Promise<Address[]> {
        return await this.addressService.getUserAddresses(userID)
    }

    @Post()
    async addAddress(@Body() address: {address: string}, @UserID() userID: number): Promise<Address[]> {
        await this.addressService.newAddress({
            address: address.address,
            userID
        })
        return await this.addressService.getUserAddresses(userID)
    }

    @Delete(':id')
    async deleteAddress(@Param('id', ParseIntPipe) addressID: number, @UserID() userID: number): Promise<Address[]> {
        if (!await this.addressService.isPersonalAddress(addressID, userID)) throw new ForbiddenException(`Access denied. Deleting not self address not allowed`);
        await this.addressService.delAddress(addressID);
        return await this.addressService.getUserAddresses(userID);
    }

    @Put(':id')
    async editAddress(@Param('id') addressID: number, @Body() newAddress: {address: string}, @UserID() userID: number): Promise<Address[]> {
        if (!await this.addressService.isPersonalAddress(addressID, userID)) {
            throw new ForbiddenException(`Access denied. Editing not self address not allowed`)
        }
        await this.addressService.changeAddress(newAddress.address, addressID, userID);
        return await this.addressService.getUserAddresses(userID);
    }
}