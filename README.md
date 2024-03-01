
# python-basic-rest-api

Basic rest api codebase to perform CRUD operation and persist in json file

## Setup the local python environment

The following url can be used and find python software to install

### Download website: `https://www.python.org/downloads/`
 - Setup a git repo locally
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
	   	 - c:\python-basic-rest-api> env/Scripts/activate.bat
	   	 - (venv) c:\python-basic-rest-api>
	   	 - After installation all required libraries, generate a text file listing all your project dependencies by running the code below:
   	 - (venv) c:\python-basic-rest-api> pip freeze > requirements.txt
   	 - To **deactivate** your virtual environment, simply run the following code in the terminal:
	   	 - (venv) c:\python-basic-rest-api> `deactivate`
	 - Run the following command to **install all required libraries** at once
	   	 - c:\python-basic-rest-api> pip install -r requirements.txt
