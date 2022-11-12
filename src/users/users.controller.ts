import { Controller, Get, Post, Body, Patch, Param, Delete, UsePipes, ValidationPipe } from '@nestjs/common';
import { newUser, User } from './dto/user.dto';
import { UsersService } from './users.service';

@Controller()
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @UsePipes(new ValidationPipe({
    whitelist: true,
    forbidNonWhitelisted: true,
    transform: true,
  }))
  @Post()
  index(@Body() user: User | newUser) {
    if (user instanceof User) {
      return this.usersService.getUser(user)
    }
    return this.usersService.addUser(user)
  }
}
