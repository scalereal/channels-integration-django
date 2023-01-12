# channels-integration-django
![51549342-3e3fc000-1e90-11e9-9bc8-8497e82f9c88.jpg](https://user-images.githubusercontent.com/9060759/51549342-3e3fc000-1e90-11e9-9bc8-8497e82f9c88.jpg)

## Getting started:
### Clone this repository:
```
git clone https://github.com/scalereal/channels-integration-django.git
```
### Install pipenv
```
pip install pipenv
```
### Activate environment:
```
pipenv shell
```
### Install dependencies:
```
pipenv install
```
### Start the server:
``` 
python manage.py runserver
```
---OR---
```
daphne -b 127.0.0.1 -p 8000 channel_integration.config.asgi:application
```