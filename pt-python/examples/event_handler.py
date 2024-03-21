from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
import requests

app = APIGatewayRestResolver()


@app.get("/todos/<todo_id>")
def get_todo_by_id(todo_id: int):
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    todo.raise_for_status()

    return todo.json()


@app.route("/todos", methods=["POST", "PUT"])
def create_todo():
    todo_data: dict = app.current_event.json_body  # deserialize json str to dict
    todo = requests.post("https://jsonplaceholder.typicode.com/todos", data=todo_data)
    todo.raise_for_status()

    return todo.json()


def lambda_handler(event: dict, context: LambdaContext):
    return app.resolve(event, context)
