import { BadRequestException, Injectable, NotFoundException } from '@nestjs/common';
import { Address, Prisma } from '@prisma/client';
import { PrismaService } from 'src/prisma/prisma.service';
import { AddressesPrisma } from './addresses.prisma';
import { newAddress } from './dto';

@Injectable()
export class AddressesService extends AddressesPrisma{

    constructor(prismaService: PrismaService) {
        super(prismaService)
    }

    async newAddress(address: newAddress) {
        await this.addAddress(address)
    }

    async getAddressByID(id: number) {
        await this.getAddress(id)
    }

    async changeAddress(address: string, addressID: number, userID: number) {
        return await this.editAddress(address, addressID)
    }

    async delAddress(addressId: number) {
        try {
            await this.deleteAddress(addressId)
        } catch (exception) {
            if (exception instanceof Prisma.PrismaClientKnownRequestError && exception.code === 'P2015') {
                throw new NotFoundException(`Entry doesn't exist`)
            }
        }
    }

    /* Check whether address belongs to user **/
    async isPersonalAddress(addressID: number, userID: number): Promise<boolean> {
        const userAddrs = await this.getUserAddresses(userID);
        return userAddrs.some((addr: Address) => addr.id === addressID)
    }

}