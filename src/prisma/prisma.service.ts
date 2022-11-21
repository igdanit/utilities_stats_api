import { BadRequestException, ForbiddenException, INestApplication, Injectable, OnModuleInit, UnauthorizedException } from '@nestjs/common';
import { PrismaClient} from '@prisma/client';
import { newAddress } from 'src/addresses/dto';
import { newUser } from 'src/users/dto/user.dto';
import { FindObject } from './prisma.service.interface';

@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit{
    
    // Establish connection
    async onModuleInit() {
        await this.$connect();
    }

    // Shutdown hook
    async enableShutdownHooks(app: INestApplication) {
        this.$on('beforeExit', async () => {
            await app.close();
        });
    }

    // Create user entry
    async createUserEntry(user: newUser) {
        return await this.user.create({ data: user });
    }

    // Fetch user entry
    async getUser(user: FindObject) {

        const findObject = 'id' in user ? {id: user.id} : {email: user.email}

        const userEntry = await this.user.findUnique({
            where: findObject
        })

        if (userEntry === null) throw new UnauthorizedException("Bad credentials")

        return userEntry
    }

    // Check whether user exist or not
    async isUserExist(user: FindObject): Promise<boolean> {
        try {
            await this.getUser(user);
            return true
        } catch (e) {
            if (e instanceof UnauthorizedException) {
                return false
            }
            throw e
        }
    }
}