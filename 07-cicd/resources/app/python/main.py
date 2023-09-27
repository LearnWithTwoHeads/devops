import mysql.connector

from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="mysql",
        port=3306,
    )

@app.route("/names")
def names():
    connection = create_db_connection()

    cur = connection.cursor()

    cur.execute('SELECT * FROM names')
    result = cur.fetchall()

    all_names = []

    for name in result:
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
    connection = create_db_connection()

    cur = connection.cursor()

    cur.execute("INSERT INTO names (name) VALUES (%s)",
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
    connection = create_db_connection()

    cur = connection.cursor()
    with open("names.sql") as f:
        cur.execute(f.read())

    app.run(host="0.0.0.0", port=8080)