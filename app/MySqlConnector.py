import sqlalchemy as db
from sqlalchemy.sql import select, update, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, MetaData
import os, sys

class MysqlConnector:

    def __init__(self, is_test=False):
        
        dialect = "mysql+pymysql"
        hostname = os.getenv("MYSQL_HOSTNAME")
        username = os.getenv("MYSQL_USERNAME")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE_TEST") if is_test else os.getenv("MYSQL_DATABASE")
        self.engine_str = f"{dialect}://{username}:{password}@{hostname}:3306/{database}"
    
    def db(self):
        try:
            _db = db.create_engine(
                self.engine_str, echo=False, encoding='utf-8', pool_pre_ping=True, pool_recycle=3600)
            return _db
        except Exception as e:
            print(e)

    def execute(self, sql):
        conn = self.db().connect()
        try:
            return conn.execute(sql).fetchall()
        except Exception as e:
            print(e)
            return False
        finally:
            conn.close()

    def select(self, table, condition="", returned_fields=[]):
        # TODO: rendere più efficiente
        returned_values = None
        metadata = MetaData()
        t_meta = Table(table, metadata,
                       autoload=True, autoload_with=self.db())
        conn = self.db().connect()

        try:
            if "query" in condition:
                s = condition.split(':')[1]
            elif condition == "":
                s = select([t_meta])
            else:
                where = condition.replace(" ", "").split('=')
                s = select([t_meta]).where(t_meta.c[where[0]] == where[1])

            result = conn.execute(s)
            return result.fetchall()
            # row = result.fetchall()
            # if row is not None:
            #     returned_values = {}
            #     for field in returned_fields:
            #         returned_values[field] = row[field]

        except Exception as e:
            print("ERROR", e)
        finally:
            conn.close()

        return returned_values

    def update(self, table, condition, updating_fields):
        where = condition.replace(" ", "").split('=')
        conn = self.db().connect()
        try:

            metadata = MetaData()
            t_meta = Table(table, metadata,
                              autoload=True, autoload_with=self.db())
            upd = t_meta.update().\
                where(t_meta.c[where[0]] == where[1]).\
                values(updating_fields)
            result = conn.execute(upd)

        except Exception as e:
            print(f"Exception: {e}. query: {where}" )
            sys.exit(0)
            return False
        finally:
            conn.close()
            
        return True

    def insert(self, table, values_list):
        try:
            connection = self._engine.connect()
            metadata = MetaData()
            t_meta = Table(table, metadata,
                              autoload=True, autoload_with=self._engine)
            ins = t_meta.insert()
            result = connection.execute(ins, values_list)

        except Exception as e:
            print(e)
            return False
        finally:
            connection.close()
        
        return result.inserted_primary_key[0]

    def delete(self, table, condition):
        where = condition.replace(" ", "").split('=')
        connection = self._engine.connect()
        try:

            metadata = MetaData()
            t_meta = Table(table, metadata,
                           autoload=True, autoload_with=self._engine)
            deleted = t_meta.delete().\
                where(t_meta.c[where[0]] == where[1])
            result = connection.execute(deleted)

        except Exception as e:
            print(e)
            return False
        finally:
            connection.close()

        return True
