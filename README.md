# djangoDRFtemplate-docker

Template for creating a Django REST project contains various features & tools

## Features
- docker compose files for development/production evironment
- Postgresql DB
- Celery/Redis setup
- JWT auth ([djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)) along views for create/delete user & change password
- OpenAPI docs using [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) (swagger UI)
- VScode debugger config
- VScode settings for black (linting/formating)



## Usage

Install cookiecutter
`pip install cookiecutter`

Create project
`cookiecutter https://github.com/talha700/drf_postgresql_biolerplate.git`  

