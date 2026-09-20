
def test_application(application, candidate, job) -> None:
    assert application.candidate == candidate
    assert application.job == job
    assert application.get_status() == "APPLIED"