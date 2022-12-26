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
  indicationsTypeID: string;
  indication: number;
  /** If date has a default value than DB value will date.now() */
  createdAt?: DateMessage | undefined;
}

export interface Indication {
  id: string;
  indication: number;
  indicationTypeID: number;
  createdAt: DateMessage | undefined;
}

export interface IndicationsResponse {
  indications: Indication[];
}

export interface GetIndicationsTypesRequest {
  addressID: string;
  maxQuantity: number;
}

export interface PostIndicationTypeRequest {
  addressID: string;
  type: string;
}

export interface IndicationType {
  id: string;
  addressID: string;
  type: string;
}

export interface IndicationsTypesResponse {
  indicationsTypes: IndicationType[];
}

export const INDICATIONS_PACKAGE_NAME = "indications";

export interface IndicationsClient {
  postIndication(request: PostIndicationRequest): Observable<Empty>;

  getIndications(request: GetIndicationsRequest): Observable<IndicationsResponse>;

  postIndicationType(request: PostIndicationTypeRequest): Observable<Empty>;

  getIndicationsTypes(request: GetIndicationsTypesRequest): Observable<IndicationsTypesResponse>;
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
}

export function IndicationsControllerMethods() {
  return function (constructor: Function) {
    const grpcMethods: string[] = ["postIndication", "getIndications", "postIndicationType", "getIndicationsTypes"];
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
