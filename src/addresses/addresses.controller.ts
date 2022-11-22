import { Controller, Get, Body, Query, ParseIntPipe, Post, UseGuards, HttpStatus, Delete, Param, Put,  } from '@nestjs/common';
import { JwtAuthGuards } from 'src/auth/auth.jwt-guard';
import { UserID } from 'src/decorators';
import { AddressesService } from './addresses.service';

@UseGuards(JwtAuthGuards)
@Controller('address')
export class AddressesController {

    constructor(private readonly addressService: AddressesService) {}

    @Get()
    async getUsersAddresses(@Query('user', ParseIntPipe) userID: number ) {
        const addressesList = await this.addressService.getUserAddresses(userID);
        const addresses = Object.fromEntries(addressesList.entries());
        return addresses
    }

    @Post()
    async addAddress(@Body() address: {address: string}, @UserID() id: number) {
        await this.addressService.newAddress({
            address: address.address,
            userID: id,
        })
    }

    @Delete(':id')
    async deleteAddress(@Param('id') addressID: number, @UserID() userID: number) {
        return await this.addressService.delAddress(addressID, userID)
    }

    @Put(':id')
    async editAddress(@Param('id') addressID: number, @Body() newAddress: {address: string}, @UserID() userID: number) {
        return await this.addressService.changeAddress(newAddress.address, addressID, userID)
    }
}
