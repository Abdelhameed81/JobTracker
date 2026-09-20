from enum import Enum, auto


class ApplicationStatus(Enum):
    APPLIED = auto()
    UNDER_REVIEW = auto()
    INTERVIEW_REQUESTED = auto()
    INTERVIEW = auto()
    OFFER = auto()
    OFFER_ACCEPTED = auto()
    OFFER_REJECTED = auto()
    REJECTED = auto()
    CLOSED = auto()