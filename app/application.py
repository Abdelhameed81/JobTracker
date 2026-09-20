from app.candidate import Candidate
from app.job import Job
from app.application_status import ApplicationStatus


class Application:
    """ This class contains the application details """
    def __init__(self, candidate: Candidate, job: Job) -> None:
        self.candidate = candidate
        self.job = job
        self._status: ApplicationStatus = ApplicationStatus.APPLIED

    def get_status(self) -> ApplicationStatus:
        return self._status