import sqlite3

from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/names")
def names():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    names = cur.execute('SELECT * FROM names').fetchall()

    all_names = []

    for name in names:
        all_names.append(name[0])

    response = make_response(
        jsonify({
            "names": all_names
        })
    )

    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/names/<name>", methods=["PUT"])
def add_name(name):
    connection = sqlite3.connect("data.db")

    cur = connection.cursor()

    cur.execute("INSERT INTO names (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    connection.close()

    response = make_response(
        jsonify({
            "name": name
        })
    )
    
    response.headers["Content-Type"] = "application/json"
    return response
    

if __name__ == "__main__":
    connection = sqlite3.connect("data.db")

    with open("names.sql") as f:
        connection.executescript(f.read())

    app.run(host="0.0.0.0", port=8080)
