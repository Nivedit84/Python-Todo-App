import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Environment variable for app name
APP_NAME = os.getenv("APP_NAME", "Todo API")

# In-memory todo storage
todos = []

@app.route("/")
def home():
    return {"message": f"Welcome to {APP_NAME}"}

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return {"error": "Task is required"}, 400
    todo = {"id": len(todos) + 1, "task": data["task"]}
    todos.append(todo)
    return todo, 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Todo deleted"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
