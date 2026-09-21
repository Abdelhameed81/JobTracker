import pytest

from app.email import Email
from app.job import Job
from app.candidate import Candidate
from app.application import Application
from app.application_status import ApplicationStatus


@pytest.fixture
def job() -> Job:
    return Job("Test job title", "Test company name", "Test job location", "Test job work arrangement", "Test job salary", "Test company description", "Test job responsibilities")

@pytest.fixture
def candidate() -> Candidate:
    return Candidate("Test candidate name", "Test candidate email", "111111111", "Test candidate CV")

@pytest.fixture
def application(candidate, job) -> Application:
    return Application(candidate, job)

@pytest.fixture
def closed_application(application) -> Application:
    application.change_status(ApplicationStatus.UNDER_REVIEW)
    application.change_status(ApplicationStatus.REJECTED)
    application.change_status(ApplicationStatus.CLOSED)
    return application

@pytest.fixture
def email() -> Email:
    return Email("test@email.com")
