from typing import Optional

from pydantic import BaseModel


class Details(BaseModel):
    email: str
    phone: str


class Person(BaseModel):
    name: str
    age: int
    city: str
    details: Optional[Details] = None


# person = Person(name='John', age=30, city='New York', details=Details(email='john@gmail.com', phone='123-456-7890'))
person = Person(name='John', age=30, city='New York')

json_str = person.json(exclude_none=True)  # 通过exclude_none参数，可以排除值为None的字段
print(json_str)

person = Person.parse_raw(json_str)
print(person)
