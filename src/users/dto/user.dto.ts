import { MaxLength, IsEmail, IsString } from 'class-validator'

export class newUser {
    @MaxLength(30)
    username: string;

    @IsEmail()
    email: string;

    @IsString()
    passwordHash: string;
}