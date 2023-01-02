class IndexPairAlreadyExist(BaseException):
    """Raised when an insert or update fails due to a duplicate key error."""

    def __init__(self, *args: tuple, msg: str, **kwargs: dict) -> None:
        self.msg = msg
        super().__init__(*args)
