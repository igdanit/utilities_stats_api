class BadRequest(BaseException):
    def __init__(self, *args, msg: str, **kwargs) -> None:
        self.msg = msg
        super().__init__(*args, **kwargs)
