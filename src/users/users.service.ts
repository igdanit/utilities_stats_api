import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { newUser, User } from './dto/user.dto';

@Injectable()
export class UsersService {

    constructor(private readonly prismaService: PrismaService) {}

    // Whether user exist, if true add them to DB.
    async addUser(user: newUser) {

        if (await this.prismaService.getUser(user)) {
            throw new UnauthorizedException('Bad credentials')
        }

        return await this.prismaService.createUserEntry(user);
    }

    async getUser(user: User) {
        return await this.prismaService.getUser(user)
    }
}
