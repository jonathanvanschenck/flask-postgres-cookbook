# flask-postgres-cookbook
A little example of hooking a postgres db to a flask webserver, based on docker containers

# Setup
```bash
 $ python3 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
 (venv) $ python scripts/create_env.py
```


# Run
```bash
 (venv) $ gunicorn wsgi --bind localhost:8000
```



# To Do
 - [x] Get a running flask app
 - [ ] Add sqlite3 functionality
 - [ ] Set up postgres docker container
 - [ ] Get flask to interface with the postgres container
 - [ ] Dockerify flask app
