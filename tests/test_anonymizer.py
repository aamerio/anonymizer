from app.Anonymizer import Anonymizer
from app.MySqlConnector import MysqlConnector  
import pytest

@pytest.fixture
def anonClass():
    return Anonymizer(None, None)

def test_constructor(anonClass):
    assert isinstance(anonClass, Anonymizer)

@pytest.fixture
def mock_db_env(monkeypatch):
    monkeypatch.setenv("MYSQL_HOSTNAME", "localhost")
    monkeypatch.setenv("MYSQL_USERNAME", "root")
    monkeypatch.setenv("MYSQL_PASSWORD", "database_password")
    monkeypatch.setenv("MYSQL_DATABASE", "nation")
    
@pytest.fixture
def dbTest(mock_db_env):
    connector = MysqlConnector()
    return connector

@pytest.fixture
def strategy():
    fields = ["name:llname"]
    return [{"tablename" : "vips", "pkey": "vip_id", "fields": fields}]

@pytest.fixture
def anon(dbTest, strategy):
    runner = Anonymizer(dbTest, strategy)
    return runner

def test_setNewDefinition(anon):
    assert type(anon.setNewDefinition('llname')) is str
    assert anon.setNewDefinition('llname') != 'pippo'
#
# def test_
# def test_run(anon):
#    assert anon.run() is True
