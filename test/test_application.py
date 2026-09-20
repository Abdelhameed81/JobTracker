
def test_application(application, job, candidate) -> None:
    assert application.job == job
    assert application.candidate == candidate
    assert application.status == "APPLIED"