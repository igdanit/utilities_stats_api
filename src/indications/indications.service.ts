import { Inject, Injectable, OnModuleInit } from '@nestjs/common';
import { ClientGrpc } from '@nestjs/microservices';
import { Observable } from 'rxjs';
import { INDICATIONS_SERVICE_NAME, IndicationsClient, GetIndicationsRequest, GetIndicationsTypesRequest, PostIndicationRequest, PostIndicationTypeRequest, IndicationsResponse, IndicationsTypesResponse } from './indications.pb'

@Injectable()
export class IndicationsService implements OnModuleInit {
    private indicationsService: IndicationsClient

    constructor(@Inject(INDICATIONS_SERVICE_NAME) private client: ClientGrpc) {}

    onModuleInit() {
        this.indicationsService = this.client.getService<IndicationsClient>(INDICATIONS_SERVICE_NAME)
    }

    async getIndicaiotns(data: GetIndicationsRequest): Promise<Observable<IndicationsResponse>> {
        return this.indicationsService.getIndications({
            indicationTypeID: data.indicationTypeID,
            maxQuantity: data.maxQuantity
        })
    }

    async insertIndication(indication: PostIndicationRequest) {
        return this.indicationsService.postIndication({
            indicationsTypeID: indication.indicationsTypeID,
            indication: indication.indication,
            createdAt: indication.createdAt
        })
    }

    async getIndicationTypes(data: GetIndicationsTypesRequest): Promise<Observable<IndicationsTypesResponse>> {
        return this.indicationsService.getIndicationsTypes({
            addressID: data.addressID,
            maxQuantity: data.maxQuantity
        })
    }

    async insertIndicationType(type: PostIndicationTypeRequest) {
        return this.indicationsService.postIndicationType({
            addressID: type.addressID,
            type: type.type
        })
    }

}

