import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    # Attempt to connect to the postgres server
    try:
        s.connect(('postgres', 5432))
        s.close()
        break
    except socket.error as ex:
        print("Still waiting . . .")
        time.sleep(1.0)
