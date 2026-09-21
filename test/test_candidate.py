from app.candidate import Candidate
from app.email import Email


def test_candidate(candidate: Candidate) -> None:
    assert candidate.name == "Test candidate name"
    assert isinstance(candidate.email, Email)
    assert candidate.email.email == "test@email.com"
    assert candidate.phone == "111111111"
    assert candidate.cv == "Test candidate CV"