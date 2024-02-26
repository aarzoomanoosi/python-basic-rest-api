from flask import Flask, request
from employee_service import init_seed_data, find_by_id, save_data, get_all, create, update

app = Flask(__name__)


# initilize seed data
employees = init_seed_data()


# default endpoint
@app.route("/")
def home():
    return {"Message": "This is a default endpoint"}


# helloworld endpoint
@app.route("/helloworld")
def hello_world():
    return {"Message": "Hello World!"}


# search employee by id
@app.route("/employee/<int:id>")
def employee_find_by_id(id):
    print(id)
    data = find_by_id(employees, id)

    if data == None:
        return "", 204
    else:
        return data, 200
    

# get all employees info
@app.route("/employee", methods=['GET'])
def getall():
    response = get_all(employees)
    return response, 200


# create an employee
@app.route("/employee", methods=['POST'])
def create_employee():
    employee = request.json
    emp = create(employee)
    employees.append(emp)
    return "", 201


# update an employee record
@app.route("/employee/<int:id>", methods=['PUT'])
def update_employee(id):
    payload = request.json
    if update(employees, payload, id) == True:
        return {"Message": "Successfully updated"}, 200
    else:
        return {"Message": "Bad request"}, 400


# save data to json file
@app.route("/save", methods=['POST'])
def save():
    save_data(employees)
    return "", 200



if __name__ == "__main__":
    app.run(debug=True)

    