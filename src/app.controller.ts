import { Controller, Get, Param, ParseIntPipe, Post } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async index() {
    return 'Hello WORLD!'
  }
}
