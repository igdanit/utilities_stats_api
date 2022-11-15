import { Module } from '@nestjs/common';
import { JwtModule } from '@nestjs/jwt';
import { UsersModule } from 'src/users/users.module';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';

@Module({
  imports: [
    UsersModule,
    JwtModule.register({
      secret: process.env['ACCESS_TOKEN_SECRET'],
      signOptions: {expiresIn: '15m'}, 
    })
  ],
  controllers: [AuthController],
  providers: [AuthService]
})
export class AuthModule {}
