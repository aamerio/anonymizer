# anonymizer

[https://pypi.org/project/pynonymizer/]
[https://github.com/jerometwell/pynonymizer]
[https://faker.readthedocs.io/en/master/index.html]

```python
from faker import Faker
from faker.providers import internet
#fake = Faker(['it_IT', 'en_US', 'ja_JP'])
#for _ in range(10):
#    print(fake.name())
fake = Faker()
#fake.add_provider(internet)
#print(fake.ipv4_private())



# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class
class MyProvider(BaseProvider):
    def foo(self):
        return ['bar','lop']

# then add new provider to faker instance
fake.add_provider(MyProvider)

# now you can use:
print(fake.foo())
```
