import { Body, Controller, Post } from '@nestjs/common';
import { newUser, UserDTO } from 'src/users/dto/user.dto';
import { UsersService } from 'src/users/users.service';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {

    constructor(
        private readonly usersService: UsersService,
        private readonly authService: AuthService,
        ){}

    @Post('sign-up')
    async signUp(@Body() user: newUser) {
        return await this.usersService.addUser(user)
    }

    @Post('sign-in')
    async signIn(@Body() user: UserDTO) {
        return await this.authService.login(user)
    }

}
