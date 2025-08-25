import pytest

def pytest_addoption(parser):
    parser.addoption("--my-logfile", action="store", help="Path to log file")

@pytest.fixture
def log_file(request):
    return request.config.getoption("--my-logfile")