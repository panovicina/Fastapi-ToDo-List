## ToDo-list REST API


### Description
Restfull application implemented with FastAPI that allows you to perform CRUD operations on users, todo-lists and tasks.

#### Features
- async SQLALchemy + PostgreSQL
- alembic migrations
- JWT authentication
- dockerized
- pre-commit with black, flake8, isort

### Quick start with docker-compose:
1) Made entrypoint executable if needed
   
```shell
chmod +x entrypoint.sh
```

3) run containers

```shell
docker-compose  up
```
