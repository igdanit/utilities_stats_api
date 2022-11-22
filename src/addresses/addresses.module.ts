import { Module } from '@nestjs/common';
import { PrismaModule } from 'src/prisma/prisma.module';
import { AddressesController } from './addresses.controller';
import { AddressesService } from './addresses.service';

@Module({
  controllers: [AddressesController],
  providers: [AddressesService],
  imports: [PrismaModule]
})
export class AddressesModule {}
