from dataclasses import dataclass
import validators
from app.exceptions import InvalidEmailError


@dataclass(frozen=True)
class Email:
    email: str

    def __post_init__(self) -> None:
        if not validators.email(self.email):
            raise InvalidEmailError(self.email)
