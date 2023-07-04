import { MaxLength, IsEmail, IsString, IsOptional } from 'class-validator'

export class newUser {
    @IsOptional()
    @MaxLength(30)
    username: string;

    @IsEmail()
    email: string;

    @IsString()
    password: string;
}

export class UserDTO {
    @IsEmail()
    email: string;

    @IsString()
    password: string;
}