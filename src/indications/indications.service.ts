import { Inject, Injectable, OnModuleInit } from '@nestjs/common';
import { ClientGrpc } from '@nestjs/microservices';
import { firstValueFrom } from 'rxjs';
import { INDICATIONS_SERVICE_NAME, IndicationsClient, GetIndicationsRequest, GetIndicationsTypesRequest, PostIndicationRequest, PostIndicationTypeRequest, IndicationsResponse, IndicationType} from './indications.pb'
import * as grpc from '@grpc/grpc-js';
import { Result, SuccessfulResult, FailedResult } from '../utilities'
import { Empty } from './google/protobuf/empty.pb';
import * as rxjs from "rxjs";

@Injectable()
export class IndicationsService implements OnModuleInit {
    private indicationsService: IndicationsClient

    constructor(@Inject(INDICATIONS_SERVICE_NAME) private client: ClientGrpc) {}

    onModuleInit() {
        this.indicationsService = this.client.getService<IndicationsClient>(INDICATIONS_SERVICE_NAME)
    }

    async getIndicaiotns(data: GetIndicationsRequest): Promise<Result<IndicationsResponse, grpc.ServiceError>> {
        try {
            return new SuccessfulResult(
                await firstValueFrom(
                    this.indicationsService.getIndications({
                        indicationTypeID: data.indicationTypeID,
                        maxQuantity: data.maxQuantity
                    })
                )
            )
        } catch (e) {
            if (e?.code === grpc.status.NOT_FOUND) {
                return new FailedResult(e)
            }
            // should be logging
            throw e
        }
    }

    async insertIndication(indication: PostIndicationRequest): Promise<Result<Empty, grpc.ServiceError>> {
        try {
            return new SuccessfulResult(
                await firstValueFrom(
                    this.indicationsService.postIndication({
                        userID: indication.userID,
                        indicationsTypeID: indication.indicationsTypeID,
                        indication: indication.indication,
                        createdAt: indication.createdAt
                    })
                )
            )
        } catch (e) {
            // Combination of same (indicationTypeID) and (createdAt) could be at most one.
            if (e?.code === grpc.status.ALREADY_EXISTS) {
                // Notify the user. Indication at that day already exist
                return new FailedResult(e)
            }
            throw e
        }
    }

    async getIndicationTypes(data: GetIndicationsTypesRequest): Promise<Result<IndicationType[], grpc.ServiceError>> {
        try {
            const res = await firstValueFrom(
                this.indicationsService.getIndicationsTypes({
                    addressID: data.addressID,
                    maxQuantity: data.maxQuantity
                })
            );
            return new SuccessfulResult(res.indicationsTypes)
        } catch(e) {
            if (e?.code === grpc.status.NOT_FOUND) {
                return new SuccessfulResult(
                    new Array<IndicationType>()
                )
            }
            return new FailedResult(e);
        }
    }

    async insertIndicationType(type: PostIndicationTypeRequest): Promise<Result<Empty, grpc.ServiceError>> {
        try {
            return new SuccessfulResult( 
                await firstValueFrom(
                    this.indicationsService.postIndicationType({
                        userID: type.userID,
                        addressID: type.addressID,
                        type: type.type
                    })
                )
            )
        } catch(e) {
            // Combination of same (addressID) and (type) could be at most one.
            if (e?.code === grpc.status.ALREADY_EXISTS) {
                return new FailedResult(e)
            }
            throw e
        }
    }

    async isPersonalTypeID(userID: string, typeID: string): Promise<Result<boolean, grpc.ServiceError | rxjs.EmptyError>> {
        try {
            const response = await firstValueFrom(
                this.indicationsService.isUsersIndicationType({
                    userID: userID,
                    typeID: typeID
                })
            )
            return new SuccessfulResult(response.status)
        } catch (e) {
            return new FailedResult(e)
        }
    }

    async isPersonalIndication(userID: string, indicationID: string): Promise<Result<boolean, grpc.ServiceError | rxjs.EmptyError>> {
        try {
            const response = await firstValueFrom(
                this.indicationsService.isUsersIndication({
                    userID: userID,
                    indicationID: indicationID
                })
            )
            return new SuccessfulResult(response.status)
        } catch(e) {
            return new FailedResult(e)
        }
    }
}
