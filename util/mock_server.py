from flask import Flask, request, jsonify
from jsonpath_ng import parse

app = Flask(__name__)


@app.route("/api/resource")
def mock_resource():
    data = {"message": "This is a mock response from the server.", "status": "success"}
    return jsonify(data)


@app.route("/api/post-example", methods=["POST"])
def post_example():
    data = request.json  # Get JSON data from the request
    name = data.get("name")
    message = data.get("message")
    response = {"status": "success", "message": f"Hello, {name}! You said: {message}"}
    return jsonify(response)


# Sample data to simulate a database
users = {1: {"name": "Vu Truong"}, 2: {"name": "Bob"}}

# Simulate user to api_test the schema
users_schema_test = [{"id": 1, "name": "Vu Truong"}, {"id": 2, "name": "Bob"}]


@app.route("/api/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    if "name" in data:
        users[user_id]["name"] = data["name"]

    return jsonify(users[user_id])


@app.route("/api/user/<int:user_id>", methods=["PUT"])
def update_user_v2(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    jsonpath_expr = parse(f"$[?(@.id == ${user_id})].name")
    if "name" in data:
        users[user_id]["name"] = data["name"]

    return jsonify(users[user_id])


@app.route("/api/user/")
def get_user():
    return jsonify(users)


@app.route("/api/users_schema/")
def get_user_schema():
    return jsonify(users_schema_test)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
