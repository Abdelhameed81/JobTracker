import pytest
from app.application_status import ApplicationStatus
from app.exceptions import InvalidStatusTransitionError


def test_application(application, candidate, job) -> None:
    assert application.candidate == candidate
    assert application.job == job
    assert application.get_status() == ApplicationStatus.APPLIED

def test_application_can_change_to_valid_status(application) -> None:
    application.change_status(ApplicationStatus.UNDER_REVIEW)
    assert application.get_status() == ApplicationStatus.UNDER_REVIEW

def test_application_rejects_invalid_status_transition(application) -> None:
    with pytest.raises(InvalidStatusTransitionError):
        application.change_status(ApplicationStatus.INTERVIEW)