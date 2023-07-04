interface Success<T> {
    ok: true,
    value: T
}

interface Fail<E> {
    ok: false,
    error: E
}

export type Result<T, E> = Success<T> |  Fail<E>

export class FailedResult<E> implements Fail<E> {
    public ok: false = false
    constructor(public error: E) {}
}

export class SuccessfulResult<T> implements Success<T> {
    public ok: true = true
    constructor(public value: T) {}
}