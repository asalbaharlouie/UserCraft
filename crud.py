from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
current_id = 1

@app.post("/users")
def create_user():
    global current_id

    data = request.get_json()

    if not data or "name" not in data or "email" not in data or "family" not in data or "password" not in data:
        return jsonify({"response": "bad request"}), 400

    user_id = current_id
    users[user_id] = {
        "id": user_id,
        "name": data["name"],
        "family": data["family"],
        "email": data["email"],
        "password": data["password"]
    }

    current_id += 1

    response_data = {
        "id": user_id,
        "name": data["name"],
        "family": data["family"],
        "email": data["email"]
    }

    return jsonify(response_data), 200


@app.get("/<int:user_id>")
def get_user(user_id):
    if user_id not in users:
        return jsonify({"response": "Client does not exist"}), 404

    user = users[user_id]

    response_data = {
        "id": user["id"],
        "name": user["name"],
        "family": user["family"],
        "email": user["email"]
    }

    return jsonify(response_data), 200


@app.put("/users")
def update_user():
    data = request.get_json()

    if not data or "id" not in data:
        return jsonify({"response": "bad request"}), 400

    user_id = data["id"]

    if user_id not in users:
        return jsonify({"response": "Client does not exist"}), 404

    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "family" in data:
        users[user_id]["family"] = data["family"]
    if "email" in data:
        users[user_id]["email"] = data["email"]
    if "password" in data:
        users[user_id]["password"] = data["password"]

    return jsonify({
        "id": users[user_id]["id"],
        "name": users[user_id]["name"],
        "family": users[user_id]["family"],
        "email": users[user_id]["email"]
    }), 200


@app.delete("/<int:user_id>")
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"response": "Client does not exist"}), 404

    del users[user_id]
    return jsonify({"response": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)