import { Controller, Get, Post, Body, Patch, Param, Delete, UsePipes, ValidationPipe } from '@nestjs/common';
import { newUser, User } from './dto/user.dto';
import { UsersService } from './users.service';

@Controller('user')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post('sign-up')
  async signUp(@Body() user: newUser) {
    return await this.usersService.addUser(user)
  }

  @Post('sign-in')
  async signIn(@Body() user: User) {
    return await this.usersService.getUser(user)
  }
}