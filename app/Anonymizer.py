from faker import Faker
from faker.providers import internet
from app.AnonymizerProviders import LocalList
from sys import stdout
import sys

class Anonymizer:
    def __init__(self, db, strategies, countries=['it_IT']):
        self.faker = Faker(countries)
        self.faker.add_provider(internet)
        self.faker.add_provider(LocalList())
        self.strategies = strategies
        self.db = db


    def run(self):
        for strategy in self.strategies:
            self.update(strategy)

    def update(self, strategy):
        tablename, primary_key, fields = strategy.values()
        rows = self.db.select(tablename, returned_fields=fields)
        i = 0
        for row in rows:
            i += 1
            updating_fields = {}
            for field in fields:
                if ":" not in field:
                    field = f"{field}:"
                updating_fields[field.split(":")[0]] = self.setNewDefinition(field.split(":")[1])
            self.db.update(tablename, f"{primary_key}={row[0]}", updating_fields)
            stdout.write("\r%d/%d" % (i, len(rows)))

        return True

    def setNewDefinition(self, pattern):
        if pattern == 'llname':
            return self.faker.llname()
        elif pattern == 'llcompletename':
            return self.faker.llcompletename()
        elif pattern == 'llemail':
            return self.faker.llemail()
        elif pattern == 'llfiscal_code':
            return self.faker.llfiscal_code()
        elif pattern == 'llphone':
            return self.faker.llphone()
        elif pattern == 'completename':
            return self.faker.name()
        elif pattern == 'name':
            return self.faker.first_name()
        elif pattern == 'last_name':
            return self.faker.last_name()
        elif pattern == 'ipv4_private':
            return self.faker.ipv4_private()
        elif pattern == 'language':
            return self.faker.language_name()
        elif pattern == 'prefix':
            return self.faker.prefix()
        elif pattern == 'city':
            return f"{self.faker.city_prefix()} {self.faker.city()}"
        elif pattern == 'address':
            return self.faker.street_address()