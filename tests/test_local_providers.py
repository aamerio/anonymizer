from app.AnonymizerProviders import LocalList
import pytest

@pytest.fixture
def loclist():
    return LocalList()

def test_constructor(loclist):
    assert isinstance(loclist, LocalList)

def test_llname(loclist):
    assert loclist.llname != ''

def test_llphone(loclist):
    assert loclist.llphone() == "***-*********"