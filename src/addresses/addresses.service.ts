import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { AddressesPrisma } from './addresses.prisma';
import { newAddress } from './dto';

@Injectable()
export class AddressesService extends AddressesPrisma{

    constructor(prismaService: PrismaService) {
        super(prismaService)
    }

    async newAddress(address: string, userId: number) {
        await this.addAddress({address, userId})
    }

    async editAddress(address: string, addressId: number, userId: number) {
        await this.editAddress(address, addressId)
    }

    async delAddress(addressId: number, userId: number) {
        await this.deleteAddress(addressId)
    }
}
