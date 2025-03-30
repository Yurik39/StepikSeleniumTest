import pytest


@pytest.fixture()
def set_up():
    """Старт и финиш теста"""
    print("Start test")
    yield
    print("Finish test")
