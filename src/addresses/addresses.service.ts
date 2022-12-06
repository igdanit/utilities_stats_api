import { BadRequestException, Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
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

        // Fetch list of addresses
        const userAddresseIDs = await this.getUserAddresses(userID)

        // Verify presence of address and edit it
        if (userAddresseIDs.some((address) => address.id === addressID)) {
            return await this.editAddress(address, addressID)
        }
        
        throw new BadRequestException("Address doesn't exist")
        
    }

    async delAddress(addressId: number, userId: number) {
        try {
            await this.deleteAddress(addressId)
        } catch (exception) {
            if (exception instanceof Prisma.PrismaClientKnownRequestError && exception.code === 'P2015') {
                return {'Status Code': 401, message:"Entry doesn't exist"}
            }
        }
    }

}
