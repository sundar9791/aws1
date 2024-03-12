import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/route1')
def hello():
    return 'Route1 Data'

@app.route('/route2')
def hello():
    return 'Route2 Data'
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
