import pytest
from app.job import Job
from app.candidate import Candidate
from app.application import Application


@pytest.fixture
def job() -> Job:
    return Job("Test job title", "Test company name", "Test job location", "Test job work arrangement", "Test job salary", "Test company description", "Test job responsibilities")

@pytest.fixture
def candidate() -> Candidate:
    return Candidate("Test candidate name", "Test candidate email", 111111111, "Test candidate CV")

@pytest.fixture
def application(job, candidate) -> Application:
    return Application(job, candidate)