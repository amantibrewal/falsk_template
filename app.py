from distutils.log import debug
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get("http://52.66.235.2:8000/")
    print(resp.text)
    return "Hello World!!"

if __name__ == "__main__":
    app.run(debug=True)