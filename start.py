import pathlib
from app.Anonymizer import Anonymizer
from app.MySqlConnector import MysqlConnector
from dotenv import load_dotenv
import os, sys

env_path = pathlib.Path('.').resolve() / 'app/.env'
load_dotenv(dotenv_path=env_path, verbose=True)

connector = MysqlConnector()

#fields = ['mail:llemail', 'name:llemail', 'init:llemail']
fields = ['firstname:llname', 'lastname:llname', 'email:llemail']
strategy = [
    {"tablename" : "uaip_users", "pkey": "user_id", "fields": fields}
#    {"tablename" : "be_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "ca_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "ch_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "de_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "dk_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "es_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "iot_users","pkey": "uid", "fields": fields},
#    {"tablename" : "it_users", "pkey": "uid", "fields": fields},
#    {"tablename" : "uk_users", "pkey": "uid", "fields": fields}
]


if __name__ == "__main__":
    a = Anonymizer(connector, strategy)
    a.run()

