import { IsInt, IsString,} from 'class-validator'

export class newAddress {

    @IsInt()
    userId: number;

    @IsString()
    address: string;
}