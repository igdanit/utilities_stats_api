import {createParamDecorator, ExecutionContext, UnauthorizedException } from "@nestjs/common";
import { Buffer } from 'node:buffer';

export const UserID = createParamDecorator(
    (data: unknown, ctx: ExecutionContext) => {
        const request = ctx.switchToHttp().getRequest();
        const headers = request.headers;
        const authHeader = headers['authorization'];

        let userID: number | undefined;

        try {

            // Drop schema of AUTH header
            const jwt = authHeader.split(' ')[1];

            const payloadAsBase64String = jwt.split('.')[1];

            const payload = JSON.parse(Buffer.from(payloadAsBase64String, 'base64').toString())

            // Encoding payload from BASE64. Fetch sub field
            userID = payload.sub

        } catch (e) {
            throw e
        } finally {
            if (userID === undefined) {
                throw new UnauthorizedException('Bad JWT provided')
            }
        }

        return userID
    }
)