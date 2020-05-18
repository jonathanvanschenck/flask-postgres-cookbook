import uuid

config = {
    "FLASK_APP":"wsgi.py",
    #                               user      pswd     host   port  db_name
    "DATABASE_URL":"postgresql://flask_user:guess_me@postgres:5432/flask_db"
}

with open(".env","w") as f:
    f.write("SECRET_KEY="+str(uuid.uuid4().hex)+"\n")
    for k,v in config.items():
        f.write(k+"="+v+"\n")
