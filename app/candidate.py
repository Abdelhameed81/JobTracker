from dataclasses import dataclass

@dataclass
class Candidate:
    """ This class contains the candidate details """
    name: str
    email: str
    phone: str
    cv: str