import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { newUser, UserDTO } from './dto/user.dto';

@Injectable()
export class UsersService {

    constructor(private readonly prismaService: PrismaService) {}

    // Whether user exist, if true add them to DB.
    async addUser(user: newUser) {

        const {username , ...existedUser} = user;

        if (await this.prismaService.getUser(existedUser)) {
            throw new UnauthorizedException('Bad credentials, hello ma ma')
        }

        return await this.prismaService.createUserEntry(user);
    }

    async getUser(user: UserDTO) {
        return await this.prismaService.getUser(user)
    }
}
