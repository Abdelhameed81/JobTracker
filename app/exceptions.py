from sys import exception


class Exceptions(exception):
    pass

class InvalidStatusTransitionError(Exceptions):
    def __init__(self) -> None:
        pass

