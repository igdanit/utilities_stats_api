import { MaxLength, IsEmail, IsString, IsOptional } from 'class-validator'

export class newUser {
    @IsOptional()
    @MaxLength(30)
    username: string;

    @IsEmail()
    email: string;

    @IsString()
    passwordHash: string;
}

export class User {
    @IsEmail()
    email: string;

    @IsString()
    passwordHash: string;
}