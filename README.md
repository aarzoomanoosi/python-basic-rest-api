# python-basic-rest-api
Basic rest api codebase to perform CRUD operation and persist in json file

# Setup the local python environment

Install python software. The following url can be used to search and find python software to instll
Download website: `https://www.python.org/downloads/`

1. Setup a git repo locally
1.1 Create a project folder `python-basic-rest-api` 
1.2 Clone the code

2. Setup a virtual environment
2.1 Install following command to install virtual environment module from pip
c:\> pip install virtualenv

2.2 Go to the project directory
c:\> cd python-basic-rest-api
c:\python-basic-rest-api> 

2.3 Run the following commnd to create a virtual environment
c:\python-basic-rest-api> python -m venv venv

2.4 Activate virtual environment
env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershel
c:\python-basic-rest-api> env/Scripts/activate.bat

(venv) c:\python-basic-rest-api>

2.5 After installation all required libraries, generate a text file listing all your project dependencies by running the code below:
(venv) c:\python-basic-rest-api> pip freeze > requirements.txt

2.6 To deactivate your virtual environment, simply run the following code in the terminal:
(venv) c:\python-basic-rest-api> deactivate

2.7 Run the following command to install all required libraries at once
c:\python-basic-rest-api> pip install -r requirements.txt

