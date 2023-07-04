/* eslint-disable */
import { GrpcMethod, GrpcStreamMethod } from "@nestjs/microservices";
import { Observable } from "rxjs";
import { DateMessage } from "./date.pb";
import { Empty } from "./google/protobuf/empty.pb";

export const protobufPackage = "indications";

export interface GetIndicationsRequest {
  indicationTypeID: string;
  /** The number of indications will be 0 <= N <= max_quantity, N is integer */
  maxQuantity: number;
}

export interface PostIndicationRequest {
  userID: string;
  indicationsTypeID: string;
  indication: number;
  /** If date has a default value than DB value will date.now() */
  createdAt?: DateMessage | undefined;
}

export interface IsUsersIndicationRequest {
  userID: string;
  indicationID: string;
}

export interface Indication {
  id: string;
  indication: number;
  indicationTypeID: string;
  userID: string;
  createdAt: DateMessage | undefined;
}

export interface IndicationsResponse {
  indications: Indication[];
}

export interface IsUsersIndicationResponse {
  status: boolean;
}

export interface GetIndicationsTypesRequest {
  addressID: number;
  maxQuantity: number;
}

export interface PostIndicationTypeRequest {
  userID: string;
  addressID: number;
  type: string;
}

export interface IsUsersIndicationTypeRequest {
  userID: string;
  typeID: string;
}

export interface IndicationType {
  id: string;
  addressID: number;
  type: string;
  userID: string;
}

export interface IndicationsTypesResponse {
  indicationsTypes: IndicationType[];
}

export interface IsUsersIndicationTypeResponse {
  status: boolean;
}

export const INDICATIONS_PACKAGE_NAME = "indications";

export interface IndicationsClient {
  postIndication(request: PostIndicationRequest): Observable<Empty>;

  getIndications(request: GetIndicationsRequest): Observable<IndicationsResponse>;

  postIndicationType(request: PostIndicationTypeRequest): Observable<Empty>;

  getIndicationsTypes(request: GetIndicationsTypesRequest): Observable<IndicationsTypesResponse>;

  isUsersIndication(request: IsUsersIndicationRequest): Observable<IsUsersIndicationResponse>;

  isUsersIndicationType(request: IsUsersIndicationTypeRequest): Observable<IsUsersIndicationTypeResponse>;
}

export interface IndicationsController {
  postIndication(request: PostIndicationRequest): void;

  getIndications(
    request: GetIndicationsRequest,
  ): Promise<IndicationsResponse> | Observable<IndicationsResponse> | IndicationsResponse;

  postIndicationType(request: PostIndicationTypeRequest): void;

  getIndicationsTypes(
    request: GetIndicationsTypesRequest,
  ): Promise<IndicationsTypesResponse> | Observable<IndicationsTypesResponse> | IndicationsTypesResponse;

  isUsersIndication(
    request: IsUsersIndicationRequest,
  ): Promise<IsUsersIndicationResponse> | Observable<IsUsersIndicationResponse> | IsUsersIndicationResponse;

  isUsersIndicationType(
    request: IsUsersIndicationTypeRequest,
  ): Promise<IsUsersIndicationTypeResponse> | Observable<IsUsersIndicationTypeResponse> | IsUsersIndicationTypeResponse;
}

export function IndicationsControllerMethods() {
  return function (constructor: Function) {
    const grpcMethods: string[] = [
      "postIndication",
      "getIndications",
      "postIndicationType",
      "getIndicationsTypes",
      "isUsersIndication",
      "isUsersIndicationType",
    ];
    for (const method of grpcMethods) {
      const descriptor: any = Reflect.getOwnPropertyDescriptor(constructor.prototype, method);
      GrpcMethod("Indications", method)(constructor.prototype[method], method, descriptor);
    }
    const grpcStreamMethods: string[] = [];
    for (const method of grpcStreamMethods) {
      const descriptor: any = Reflect.getOwnPropertyDescriptor(constructor.prototype, method);
      GrpcStreamMethod("Indications", method)(constructor.prototype[method], method, descriptor);
    }
  };
}

export const INDICATIONS_SERVICE_NAME = "Indications";
