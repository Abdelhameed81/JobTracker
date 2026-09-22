from dataclasses import FrozenInstanceError
import pytest
from app.email import Email
from app.exceptions import InvalidEmailError


def test_valid_email(email) -> None:
    assert isinstance(email, Email)
    assert email.email == "test@email.com"



def test_invalid_email() -> None:
    with pytest.raises(InvalidEmailError):
        Email("test")



def test_email_is_immutable(email) -> None:
    with pytest.raises(FrozenInstanceError):
        email.email = "123"



def test_email_objects_with_same_emails_are_equal(email) -> None:
    assert email == Email(email.email)