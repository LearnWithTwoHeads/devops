from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # Important for the app to point to locahost here
    app.run(host="0.0.0.0", port=8080)