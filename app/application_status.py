from enum import Enum, auto

class ApplicationStatus(Enum):
    APPLIED = auto()
    UNDER_REVIEW = auto()
    INTERVIEW_REQUESTED = auto()
    INTERVIEW = auto()
    OFFER = auto()
    REJECTED = auto()