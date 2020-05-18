# flask-postgres-cookbook
A little example of hooking a postgres db to a flask webserver, based on docker containers.

# Setup
```bash
 $ docker-compose build
```

# Run
```bash
 $ docker-compose up
```

# Clean up
```bash
 $ docker-compose down
 $ docker volume prune
```

# To Do
 - [x] Get a running flask app
 - [x] Add sqlite3 functionality
 - [x] Set up postgres docker container
 - [x] Get flask to interface with the postgres container
 - [x] Dockerify flask app
