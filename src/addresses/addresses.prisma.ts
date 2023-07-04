import { ForbiddenException, Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { newAddress } from "./dto";

@Injectable()
export class AddressesPrisma {
    constructor(protected readonly prismaService: PrismaService) {}
    
    async addAddress(address: newAddress) {
        if (await this.prismaService.isUserExist({id: address.userID})) {
            return await this.prismaService.address.create({ data: {
                address: address.address,
                userID: address.userID
            }})
        }
        throw new ForbiddenException("User doesn't exist")
    }
    
    async editAddress(address: string, addressID: number) {
        return await this.prismaService.address.update({
            where: {id: addressID},
            data: {address: address}
        })
    }

    async deleteAddress(addressID: number) {
        return await this.prismaService.address.delete({
            where: {id: addressID}
        })
    }

    async getAddress(id: number) {
        return await this.prismaService.address.findUnique({
            where: {id}
        })
    }

    async getUserAddresses(userID: number) {
        return await this.prismaService.address.findMany({
            where: {userID}
        })
    }
}