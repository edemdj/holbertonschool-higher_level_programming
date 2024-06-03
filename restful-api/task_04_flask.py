#!/usr/bin/python3
"""docstring"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if "username" in data:
        username = data["username"]
        users[username] = {
            "name": data.get("name", ""),
            "age": data.get("age", ""),
            "city": data.get("city", "")
        }
        return jsonify({"message": "User added successfully", "user": users[username]}), 201
    else:
        return jsonify({"error": "Missing username in request data"}), 400

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

