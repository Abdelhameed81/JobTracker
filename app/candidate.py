class Candidate:
    """ This class contains the candidate details """

    def __init__(self, name: str, email: str, phone: str, cv: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.cv = cv