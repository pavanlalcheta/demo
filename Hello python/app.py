from datetime import datetime
from flask import Flask
import os

app = Flask(__name__)

Data_dir = '/app/data'
myfile = os.path.join(Data_dir,'greeting_log.txt')

if not os.path.exists(Data_dir):
    os.makedirs(Data_dir)

@app.route('/')
def hello():
    # return "hello Docker"
    mesaage = 'hello docker'
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    with open(myfile,'a') as f:
        f.write(f"{timestamp}:{mesaage}\n")

    log_content = ''
    try:
        with open(myfile,'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        log_content = "No Prviouse Log Found..!"

    return f"Log:<br><pre>{log_content}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
