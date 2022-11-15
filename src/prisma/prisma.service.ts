import { INestApplication, Injectable, OnModuleInit, UnauthorizedException } from '@nestjs/common';
import { PrismaClient} from '@prisma/client';
import { newUser } from 'src/users/dto/user.dto';

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
        await this.user.create({ data: user });
    }

    // Check whether user exist or not
    async getUser<T extends {email: string}>(user: T) {
        const userEntry = await this.user.findUnique({
            where: {email: user.email},
        })

        if (!userEntry) throw new UnauthorizedException('Bad credentials')
    
        return userEntry
    }

}