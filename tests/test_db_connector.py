"""
    NOTE: per i test utilizzo il db employees.sql in https://github.com/datacharmer/test_db
    per MariaDB
    https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/
"""
from app.MySqlConnector import MysqlConnector  
import pytest
import os

@pytest.fixture
def dbClass():
    return MysqlConnector()

def test_constructor(dbClass):
    assert isinstance(dbClass, MysqlConnector)

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

def test_env(mock_db_env):
    assert os.getenv('MYSQL_DATABASE') == 'nation'

def test_db_info(dbTest):
    sql = "SHOW DATABASES"
    assert type(dbTest.execute(sql)) is list

def test_db_select(dbTest):
    table = "countries"
    condition = "country_id = 1"
    returned_fields = ['name']
    result = dbTest.select(table, condition, returned_fields)
    assert result[0][1] == 'Aruba'