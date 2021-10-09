h1 align="center">Authentication</h1>
#### Pre Requirements
| Tools | Download Link  |
| ------ | ------ |
| 
| python | [python](https://www.python.org/) |
| xampp | [xampp](https://www.apachefriends.org/index.html) |
| 
- Add Database Name : **ecommerce_db**

```
#### Backend Development Workflow
```sh
cd server
pip install virtualenv
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
pip install mysqlclient
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

