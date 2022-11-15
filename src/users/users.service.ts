import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { User } from '@prisma/client';
import { newUser, UserDTO } from './dto/user.dto';

@Injectable()
export class UsersService {

    constructor(private readonly prismaService: PrismaService) {}

    // Whether user exist, if true add them to DB.
    async addUser(user: newUser) {

        const {username , ...existedUser} = user;

        if (await this.isUserExist(existedUser)) throw new UnauthorizedException('Bad credentials')

        return await this.prismaService.createUserEntry(user);
    }

    async getUser(user: UserDTO) {
        return await this.prismaService.getUser(user)
    }

    async isUserExist<T extends {email:string}>(user: T): Promise<boolean> {
        let userEntry: undefined | User;

        try {
            userEntry = await this.prismaService.getUser(user)
        } catch(e) {
            if (!(e instanceof UnauthorizedException)) throw e
        }

        if (userEntry) return true

        return false
    }
}
