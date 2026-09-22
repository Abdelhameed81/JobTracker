from dataclasses import dataclass


@dataclass
class Job:
    """ This class contains the job details """
    title: str
    company_name: str
    location: str
    work_arrangement: str
    salary: str
    company_description: str
    responsibilities: str