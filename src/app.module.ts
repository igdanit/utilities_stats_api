import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { ConfigModule } from '@nestjs/config'
import { AddressesModule } from './addresses/addresses.module';
import { IndicationsModule } from './indications/indications.module';

@Module({
  imports: [
    AuthModule,
    UsersModule,
    ConfigModule.forRoot({
      isGlobal: true,
      cache: true,
    }),
    AddressesModule,
    IndicationsModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
