import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { newUser } from './dto/user.dto';

@Injectable()
export class UsersService {

    constructor(private readonly prismaService: PrismaService) {}

    async addUser(user: newUser) {
        if (await this.prismaService.isUserExist(user)) {
            throw new UnauthorizedException('Bad credentials')
        }

        return await this.prismaService.createUserEntry(user);
    }
}
