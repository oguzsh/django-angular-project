# Django Simple Rest Api Project

## Setup

### Create a virtual environment to isolate our package dependencies locally

1. Create venv
`python -m venv env`

2. Activate venv
- On Linux use :
    `source env/bin/activate`

- On Windows use :
    `env\Scripts\activate`
    
### Install Django and Django REST framework into the virtual environment
- `pip install -r requirements.txt`


### Migrate Database
- `cd apiProject`
- `python manage.py migrate`

### Admin Panel
username : admin
password: admin123

If you want create a new super user : 
`python manage.py createsuperuser --email admin@example.com --username admin`

### Start Server
`python manage.py runserver`
