import { Controller, Get, Post, UseGuards, Res, HttpStatus, Query, Param, UnauthorizedException, ParseIntPipe, ForbiddenException} from '@nestjs/common';
import { JwtAuthGuards } from 'src/auth/auth.jwt-guard';
import { UserID } from 'src/decorators';
import { PrismaService } from 'src/prisma/prisma.service';
import { UsersService } from './users.service';


@UseGuards(JwtAuthGuards)
@Controller('user')
export class UsersController {

    constructor(
        private readonly userService: UsersService,
        private readonly prismaService: PrismaService,
        ) {}

    @Get(':id')
    async getUser(@Param('id') id: number, @UserID() userID:number) {
        if (id !== userID) {
            throw new ForbiddenException('Trying fetch another user data')
        }
        return await this.userService.getUser({id})
    }
}