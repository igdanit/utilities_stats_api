export interface UserWithId {
    id: number;
}

export interface UserWithEmail {
    email: string;
}

export type FindObject = UserWithId | UserWithEmail