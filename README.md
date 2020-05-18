# flask-postgres-cookbook
A little example of hooking a postgres db to a flask webserver, based on docker containers

# Setup
```bash
 $ docker-compose build
 $ docker-compose up
 $ cd flask
 $ python3 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
 (venv) $ python scripts/create_env.py
 (venv) $ chmod +x scripts/configure_db.sh
 (venv) $ ./scripts/configure_db.sh
```


# Run
```bash
 (venv) $ gunicorn wsgi --bind localhost:8000
```

# Clean up
```bash
 (venv) $ deactivate
 $ cd ..
 $ docker-compose down
```

# To Do
 - [x] Get a running flask app
 - [x] Add sqlite3 functionality
 - [x] Set up postgres docker container
 - [x] Get flask to interface with the postgres container
 - [ ] Dockerify flask app
