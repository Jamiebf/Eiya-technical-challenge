# Eiya-technical-challenge
Technical Challenge, development of api rest to know the location of a fleet of vehicles in 3 different cities.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Install Project](#install-project)
- [Run project](#run-project)

## Introduction
This is a development of an API Rest as a technical-challenge for Eiya. This API expose endpoints in a context for a fleet of vehicles.

## Installation
### Prerequisites
This project is a Python/Flask application. You must install the following tools:
- [Python 3.8.9] (https://www.python.org/downloads/release/python-389/)
- Virtualenv
```bash
pip3 install virtualenv
```

 ### Install Project
You must create a virtual environment in the directory of the project.

Access to directory of the project.
```
cd {path-of-directory}
```

Create virtual enviroment. In this case "env" is the name of your virtual environment, you can change it as you prefer.
```
python3 -m venv env 
```

Once the virtual environment was created you must activate it.
```
source env/bin/activate
```

Then, you must install the required libraries for the project.
```
python -m pip install -r requirements.txt
```
At this point you have ready all your environment in Python. Before execute the project you have run the database script in order to have the data model.


## Run project
Run the command
```
python3 run.py
```

**NOTE:** The API documentation is available as a Postman Collection.
