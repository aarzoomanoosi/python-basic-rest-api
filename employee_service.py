from employee import Employee, seed_employee_data
import json

# write seed data to file
def save_data(employees): 
    emp_json = ""
    # serilaizing into json string
    for emp in employees:
        if emp_json == "":
            emp_json = emp.json
        else:
            emp_json += "," + emp.json

    emp_json = f"[{emp_json}]"

    with open("employee.json", "w", encoding="utf-8") as outfile:
        outfile.write(emp_json)


# initialize seed data
def init_seed_data():
    return seed_employee_data()


# get employee record per id
def find_by_id(employees, id):
    for data in employees:        
        if data.id==id:
            return data.toJson()


# get all employee records
def get_all(employees):
    emp = []
    for data in employees:
        emp.append(data.toJson())

    return emp


# create an employee record
def create(payload):
    emp = Employee(id=payload["id"],
                   name=payload["name"],
                   title=payload["title"],
                   location=payload["location"],
                   role=payload["role"])
    return emp


# update an employee record
def update(employees, payload, id):
    for emp in employees:
        if emp.id == id:
            emp.name = payload["name"]
            emp.title = payload["title"]
            emp.location=payload["location"]
            emp.role=payload["role"]
            return True
        
    return False

