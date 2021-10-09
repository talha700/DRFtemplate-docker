[[_TOC_]]
##### Dependecies  
`pip install cookiecutter`

##### Create new project:  
Go to your workspace or anywhere you would like to create this project and run:  
`cookiecutter https://github.com/talha700/drf_postgresql_biolerplate.git`  
It will request username and password of you gitlab account, enter them and follow the instructions. 

##### Information to be entered during project creation:
Each filed contains default value but it is preferred to set your own. Most of these valus goes to environment variables in 
.env.dev or .env.prod so you can modify these values anytime in env files.

- "project_name": Name of the project. Spaces allowed
- "project_slug": This will be lower cased and stripped version of project_name, but you can change it.
- "secret_key": The same Authentication service is using, otherwise JWT tokens will not be verifiable.
- "postgres_password": Password for PostgreSQL,
- "postgres_db": Database name to be created. You can leave default value here without worries
- "first_superuser_username": You can leave default value here without worries
- "first_superuser_password": Default value tells you what to do
- "first_superuser_email": Fake  email is OK. Leave default.
- "postgres_port": There should not be reason to change this
- "pgadmin_default_user": Admin user for PGAdmin to create.
- "pgadmin_default_email": Fake  email is OK. Leave default.
- "pgadmin_default_user_password": Default value tels you what to do
- "allowed_hosts": You can add development server address if you like.
- "django_port_for_dev": The port on which Django server will be running
- "_copy_without_render": Leave default value here

##### Usage of newly created project
Created project will be generated with it's own README.md. Please check it for more details about newly created project startup and usage


##### For curious people
Here you can find cookicutter project documentation: https://cookiecutter.readthedocs.io/en/1.7.2/  
You will not need it for creating new projects, but if want to somehow improve this template, you are welcome :)
