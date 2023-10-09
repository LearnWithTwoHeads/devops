import os
import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_cors import CORS

backend_url = os.environ.get("BACKEND_URL")

app = Flask(__name__, template_folder="template")

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    response = requests.get(f"{backend_url}/names")
    data = response.json()
    names = ["Yoofi", "Abena", "Kosi"]
    return render_template("index.html", names=data["names"])

@app.route("/names", methods=["POST"])
def names():
   print("GETTING IN HERE")
   if "name" not in request.form:
       return redirect(url_for("home"))

   name = request.form["name"]
   response = requests.put(f"{backend_url}/names/{name}")
   return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)