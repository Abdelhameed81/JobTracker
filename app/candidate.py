from dataclasses import dataclass
from app.email import Email


@dataclass
class Candidate:
    """ This class contains the candidate details """
    name: str
    email: Email
    phone: str
    cv: str