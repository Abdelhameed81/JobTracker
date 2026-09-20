from app.candidate import Candidate
from app.job import Job


class Application:
    """ This class contains the application details """
    def __init__(self, candidate: Candidate, job: Job) -> None:
        self.candidate = candidate
        self.job = job
        self.status:  str = "APPLIED"