from flask import Flask

app = Flask(__name__)

def say_hello():
    return "Hello World"

@app.route("/")
def hello():
    return say_hello()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
