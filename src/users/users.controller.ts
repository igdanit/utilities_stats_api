import { Body, Controller, Get, Post, UseGuards, Res, HttpStatus, Query, Param, UnauthorizedException, ParseIntPipe} from '@nestjs/common';
import { Response } from 'express';
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
}