
# python-basic-rest-api

Basic rest api codebase to perform CRUD operation and persist in json file

## Setup the local python environment

The following url can be used and find python software to install

#### Download website: `https://www.python.org/downloads/`
#### Download postman: `https://www.postman.com/downloads/`

## Setup a git repo locally
- Create a project folder `python-basic-rest-api`
   	 - Clone the code
     - Setup a virtual environment
   	 - Install following command to install virtual environment module from pip
	   	 - c:\> `pip install virtualenv`
	   	 - Go to the project directory
	   	 - c:\> `cd python-basic-rest-api`
	   	 - c:\python-basic-rest-api>
   	 - Run the following command to **create a virtual environment**
	   	 - c:\python-basic-rest-api> `python -m venv venv`
   	 - **Activate** virtual environment
   		 - env/Scripts/activate.bat //In CMD
   		 - env/Scripts/Activate.ps1 //In Powershel
	   	 - > c:\python-basic-rest-api> env/Scripts/activate.bat
	   	 - (venv) c:\python-basic-rest-api>
	   	 - After installation all required libraries, generate a text file listing all your project dependencies by running the code below:
   	 - (venv) c:\python-basic-rest-api> pip freeze > requirements.txt
   	 - To **deactivate** your virtual environment, simply run the following code in the terminal:
	   	 - > (venv) c:\python-basic-rest-api> `deactivate`
	 - Run the following command to **install all required libraries** at once, first go to virtual environment
		 - > c:\python-basic-rest-api> `venv/scripts/activate` and hit enter key
		 - > (venv) c:\python-basic-rest-api> pip install -r requirements.txt
   	 - List down all the python modules to see if virtual environment is working
	   	 - > (venv) c:\python-basic-rest-api> pip list //it should show you all the installed python modules
	   	 - Run the following command to generate **requirements.txt** file
	   	 - > (venv) c:\python-basic-rest-api> `pip freeze > requirements.txt`    

## Api endpoints

 - Home endpoint 
	 - `GET ~/`
 - Helloworld endpoint
	 - `GET ~/helloworld`
 - Search an employee record per id
	 - `GET ~/employee/{id}`
	 - Sample: `~/employee/101` 
 - Get all employee records
	 - `GET ~/employee`
 - Create an employee record
	 - `POST ~/employee`
	 - Sample: Here is the payload`{"id": 107, "location": "LA Remote", "name": "robin chang", "role": "sw engineer", "title": "sw engineer"}`
 - Update an employee record
	 - `PUT ~/employee/{id}`
	 - Sample: Here is the request `~/employee/107` and payload is `{"location": "CA Remote", "name": "robin chang", "role": "sw engineer", "title": "sw engineer"}`
 - Save employee data to json file locally
	 - `POST ~/save`
	 - This will save all employee records into a `employee.json` file at local computer system
