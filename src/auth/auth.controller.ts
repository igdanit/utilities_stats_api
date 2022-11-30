import { Body, Controller, Get, HttpStatus, Post, Res, UseGuards, UsePipes } from '@nestjs/common';
import { Response } from 'express';
import { UserID } from 'src/decorators';
import { newUser, UserDTO } from 'src/users/dto/user.dto';
import { UsersService } from 'src/users/users.service';
import { JwtAuthGuards } from './auth.jwt-guard';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {

    constructor(
        private readonly usersService: UsersService,
        private readonly authService: AuthService,
        ){}


    // Add new user
    @Post('sign-up')
    async signUp(@Body() user: newUser, @Res() res: Response) {
        await this.usersService.addUser(user)
        
        res.statusCode = HttpStatus.CREATED;
        res.send({
            statusCode: HttpStatus.CREATED,
            message: "User created",
        })
    }

    // Issue JWT
    @Post('sign-in')
    async signIn(@Body() user: UserDTO) {
        return await this.authService.login(user)
    }


    @UseGuards(JwtAuthGuards)
    @Get('update-jwt')
    async updateJWT(@UserID() userID: number) {
        return await this.authService.updateJWT(userID)
    }

}
