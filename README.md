# django-channels-integration
![51549342-3e3fc000-1e90-11e9-9bc8-8497e82f9c88.jpg](https://user-images.githubusercontent.com/9060759/51549342-3e3fc000-1e90-11e9-9bc8-8497e82f9c88.jpg)

## Refer this blog
```
https://medium.com/@meet_patel/ab15c5f1cc0e
```
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
### create environment variables:
```
Create a .env file in root directory by copying the .env.example file.
After copying the contents, edit the SECRET_KEY with your respective secret key.
```
### Start the server:
``` 
python manage.py runserver
```
---OR---
```
daphne -b 127.0.0.1 -p 8000 channel_integration.config.asgi:application
```