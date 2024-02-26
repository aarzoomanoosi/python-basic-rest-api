from typing import List
from dataclasses import dataclass, asdict, field
from json import dumps

@dataclass
class Employee:
    id: int
    name: str
    title: str
    location: str
    role: str

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "location": self.location,
            "role": self.role
        }

    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)

    @property
    def json(self):
        """
        get the json formated string
        """
        return dumps(self.__dict__)
    

def seed_employee_data():
    _employees = []
    emp1 = Employee(id=101, name="John Ali", title="Dev Manager", location="Los Angeles, CA, USA", role="Tech Lead")
    emp2 = Employee(id=102, name="Aarzoo Manoosi", title="Staf Software Engineer", location="Los Angeles, CA, USA", role="Software Architect")
    emp3 = Employee(id=103, name="Tom Green", title="Sr. Software Engineer", location="Los Angeles, CA, USA", role="Software Developer")
    emp4 = Employee(id=104, name="Ash Grant", title="Software Engineer-II", location="Los Angeles, CA, USA", role="Software Developer")
    emp5 = Employee(id=105, name="Ram Singh", title="Software Engineer-III", location="Los Angeles, CA, USA", role="Software Developer")
    emp6 = Employee(id=106, name="Kim Kristy", title="Quality Engineer-II", location="Los Angeles, CA, USA", role="Software Tester")

    _employees.append(emp1)
    _employees.append(emp2)
    _employees.append(emp3)
    _employees.append(emp4)
    _employees.append(emp5)
    _employees.append(emp6)

    return _employees
