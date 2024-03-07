import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "details": {
        "email": "john@gmail.com",
        "phone": "123-456-7890"
    }
}

json_str = json.dumps(person)
print(json_str)

person = json.loads(json_str)
print(person)


class Details:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "email": self.email,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        return Details(data["email"], data["phone"])

    def __str__(self):
        return f"Details(email={self.email}, phone={self.phone})"


class Person:
    def __init__(self, name: str, age: int, city: str, details: Details = None):
        self.name: str = name
        self.age: int = age
        self.city: str = city
        self.details: Details = details

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "details": self.details.to_dict() if self.details else None
        }

    @staticmethod
    def from_dict(data):
        return Person(data["name"], data["age"], data["city"],
                      Details.from_dict(data["details"]) if "details" in data else None)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city}, details={self.details})"


person = Person("John", 30, "New York", details=Details("john@gmail.com", "123-456-7890"))
json_str = json.dumps(person.to_dict())
print(json_str)

person = Person.from_dict(json.loads(json_str))
print(person)
