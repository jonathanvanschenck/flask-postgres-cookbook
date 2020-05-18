import uuid

config = {
    "FLASK_APP":"wsgi.py",
    "DATABASE_URL":"postgresql://flask_user:guess_me@localhost:54320/flask_db"
}

with open(".env","w") as f:
    f.write("SECRET_KEY="+str(uuid.uuid4().hex)+"\n")
    for k,v in config.items():
        f.write(k+"="+v+"\n")
