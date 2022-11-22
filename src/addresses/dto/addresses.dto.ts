import { IsInt, IsString,} from 'class-validator'

export class newAddress {

    @IsInt()
    userID: number;

    @IsString()
    address: string;
}