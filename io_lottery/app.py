from flask import Flask, Response, request, jsonify

from io_lottery.controllers import AddUserController, AddUserRequest, GetUserController, UpdateUserController, DeleteUserController
from io_lottery.repositories import UserRepository
from io_lottery.views import UserView

app = Flask(__name__)


@app.get("/users/<id>")
def get_user(id: int) -> Response:
    repository = UserRepository()
    controller = GetUserController(repository=repository)
    try:
        controller.get(id)
    except NotImplementedError:
        pass
    return Response(status=501)


@app.post("/users")
def add_user() -> Response:
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    controller.add(request=AddUserRequest(json=request.json))
    return Response(response=jsonify(request.json), status=201)
    # return jsonify(request.json)


@app.put("/users/<id>")
def update_user(id: int) -> Response:
    repository = UserRepository()
    controller = UpdateUserController(repository=repository)
    controller.update(request=AddUserRequest(json=request.json))
    return Response(response=jsonify(request.json), status=200)


@app.patch("/users/<id>")
def patch_user(id: int) -> Response:
    repository = UserRepository()
    controller = UpdateUserController(repository=repository)
    controller.patch(request=AddUserRequest(json=request.json))
    return Response(response=jsonify(request.json), status=200)


@app.delete("/users/<id>")
def delete_user(id: int) -> Response:
    repository = UserRepository()
    controller = DeleteUserController(repository=repository)
    try:
        controller.delete(id)
    except NotImplementedError:
        pass
    return Response(status=204)


app.add_url_rule("/users_new", view_func=UserView.as_view("users_new"))


# @app.get("/users/<id>")
# def get_user(id: int) -> Response:
#     return Response(status=501)


@app.put("/users/<id>")
def upgrade_user(id: int) -> Response:
    raise NotImplementedError
