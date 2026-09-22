

class InvalidStatusTransitionError(Exception):
    pass

class InvalidEmailError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f"Invalid email address: {email}")
