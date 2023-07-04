import { Body, Controller, Get, HttpCode, Post, UseGuards } from '@nestjs/common';
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
    @HttpCode(201)
    async signUp(@Body() user: newUser) {
        console.log(user)
        await this.usersService.addUser(user)
        return await this.authService.login(user)
    }

    // Issue JWT
    @Post('sign-in')
    async signIn(@Body() user: UserDTO) {
        console.log(user)
        return await this.authService.login(user)
    }


    @UseGuards(JwtAuthGuards)
    @Get('update-jwt')
    async updateJWT(@UserID() userID: number) {
        return await this.authService.updateJWT(userID)
    }

}
