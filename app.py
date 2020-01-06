from flask import Flask
import os
import uuid
import requests 

app = Flask(__name__)
randomid = uuid.uuid4()
@app.route('/')
def index():
    hostname = os.uname()[1]

    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'

@app.route('/ha')
def callHA():
    URL = "http://flask:8080"
    r = requests.get(url = URL) 
    data = r.content 
    return data
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)