import pathlib
from app.Anonymizer import Anonymizer
from app.MySqlConnector import MysqlConnector
from dotenv import load_dotenv
import os, sys

env_path = pathlib.Path('.').resolve() / 'app/.env'
load_dotenv(dotenv_path=env_path, verbose=True)

connector = MysqlConnector()

fields_drupal_users = ['mail:llemail', 'name:llemail', 'init:llemail']
fields = [
        'first_name:llname', 
        'last_name:llname', 
        'address1:asterisks',
        'locality:city',
        'email:llemail',
        'mobile:asterisks',
        'birthdate:nodate']

strategy = [
    {"tablename" : "admin_consumer_refers", "pkey": "id", 
    "fields": ['referral_name:llname', 'referral_email_id:llemail']    
    },
    {"tablename" : "admin_consumers", "pkey": "id", "fields": fields},
    {"tablename" : "admin_old_consumers", "pkey": "id", "fields": fields},
    {"tablename" : "consumer_temp", "pkey": "id", 
    "fields": ['name:llname', 'surname:llname','email:llemail']    
    },
#    {"tablename" : "users", "pkey": "uid", "fields": fields_drupal_users},
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

