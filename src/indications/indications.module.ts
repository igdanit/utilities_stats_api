import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { IndicationsController } from './indications.controller';
import { IndicationsService } from './indications.service';
import { INDICATIONS_SERVICE_NAME, INDICATIONS_PACKAGE_NAME  } from './indications.pb';
import { AddressesModule } from 'src/addresses/addresses.module';

@Module({
    controllers: [IndicationsController],
    providers: [IndicationsService],
    imports: [
        ClientsModule.register([
            {
                name: INDICATIONS_SERVICE_NAME,
                transport: Transport.GRPC,
                options: {
                    package: INDICATIONS_PACKAGE_NAME,
                    protoPath: "microservices/indications/grpcService/protobufs/indications.proto",
                    url : 'localhost:50051',
                }
            }
        ]),
        AddressesModule
    ]
})
export class IndicationsModule {}
