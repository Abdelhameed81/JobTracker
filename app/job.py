class Job:
    """ This class contains the company details """
    def __init__(self, title: str, company_name: str, location: str, work_arrangement: str, salary: str, company_description: str, responsibilities: str):
        self.title = title
        self.company_name = company_name
        self.location = location
        self.work_arrangement = work_arrangement
        self.salary = salary
        self.company_description = company_description
        self.responsibilities = responsibilities