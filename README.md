# Heroes Example App using Angular2 and Django-Rest-Framework 

## For the lazy

### Starting the application

```
docker-compose -f compose.yml -f compose-development.yml up -d database
docker-compose -f compose.yml -f compose-development.yml run --rm backend bash -c "./manage.py migrate"
docker-compose -f compose.yml -f compose-development.yml up -d
```

Connect to `localhost:8088`.

### Stopping and cleaning up

Only just stop:

```
docker-compose -f compose.yml -f compose-development.yml stop
```

Remove all: **WARNING** this destroys the database and all data in it!
```
docker-compose -f compose.yml -f compose-development.yml down
```

### Starting the project

docker-compose -f compose.yml -f compose-development.yml up -d database
docker-compose -f compose.yml -f compose-development.yml run --rm backend bash -c "./manage.py migrate"
docker-compose -f compose.yml -f compose-development.yml up -d

Connect to `localhost:8088`.

## Structure

### Folder `backend`

The REST Service, using Django REST framework.

### Folder `database`

Serves as example on how to extend an Postgres Image (adding the 
postgis extensions).
This is not actually used in this project, but it often is required
in the projects I do.

### Folder `documentation`

This folder contains the documentation of the project, if any.

### Folder `frontend`

The (slightly modified) Tour-of-Heroes example App
from the Angular2 Tutorial

### Folder `nginx`

Serves as a reverse-proxy for the entire project. Easy way to deploy,
shows how it could be done. Is easier to simulate a real deploy
situation without the hassle of having a staging server.
Actual deployment involves much more than what should be
covered here.

## Running in production

Deploying or running in production isn't covered here.

For pointers, see at least
https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
