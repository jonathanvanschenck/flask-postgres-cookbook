import uuid

config = {
    "FLASK_APP":"wsgi.py"
}

with open(".env","w") as f:
    f.write("SECRET_KEY="+str(uuid.uuid4().hex)+"\n")
    for k,v in config.items():
        f.write(k+"="+v+"\n")
