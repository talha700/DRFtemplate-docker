# djangoRFtemplate-docker

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

1. Install cookiecutter <br/>
`pip install cookiecutter`

2. Create project <br/>
`cookiecutter https://github.com/talha700/drf_postgresql_biolerplate.git`
 
    cookiecutter will prompt for the settings


3. Create `env.dev` file by refering to `env.example.dev`

4. Build & Start

    > docker-compose up 

    to run in detached mode

    > docker-compose up -d 
