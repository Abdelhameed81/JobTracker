from app.candidate import Candidate
from app.exceptions import InvalidStatusTransitionError
from app.job import Job
from app.application_status import ApplicationStatus


class Application:
    """ This class contains the application details """

    allowed_status_transitions = {
        ApplicationStatus.APPLIED: {ApplicationStatus.UNDER_REVIEW},
        ApplicationStatus.UNDER_REVIEW: {ApplicationStatus.INTERVIEW_REQUESTED, ApplicationStatus.REJECTED},
        ApplicationStatus.INTERVIEW_REQUESTED: {ApplicationStatus.INTERVIEW},
        ApplicationStatus.INTERVIEW: {ApplicationStatus.OFFER, ApplicationStatus.REJECTED},
        ApplicationStatus.OFFER: {ApplicationStatus.OFFER_ACCEPTED, ApplicationStatus.OFFER_REJECTED},
        ApplicationStatus.OFFER_ACCEPTED: {ApplicationStatus.CLOSED},
        ApplicationStatus.OFFER_REJECTED: {ApplicationStatus.CLOSED},
        ApplicationStatus.REJECTED: {ApplicationStatus.CLOSED},
        ApplicationStatus.CLOSED: set()
    }

    def __init__(self, candidate: Candidate, job: Job) -> None:
        self.candidate = candidate
        self.job = job
        self._status: ApplicationStatus = ApplicationStatus.APPLIED

    def get_status(self) -> ApplicationStatus:
        return self._status

    def change_status(self, new_status: ApplicationStatus) -> ApplicationStatus:
        if new_status in self.allowed_status_transitions[self._status]:
            self._status = new_status
            return self._status
        else:
            raise InvalidStatusTransitionError()
