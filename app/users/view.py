from flask import request, jsonify
from app import app
from app.users.processor import Processor
from app.base.helper import session_to_id_user
from app.base.helper import make_response

PREFIX = '/api/user'


@app.route(PREFIX, methods=['GET'])
def all_user():
    return make_response(jsonify(Processor().users()))


@app.route(PREFIX + '/profile', methods=['GET', 'OPTIONS'])
def profile_user():
    if request.method == 'OPTIONS':
        print(request.method)
        return make_response(jsonify({}))
    id_user = session_to_id_user(request.headers)
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return make_response(jsonify(answer))


@app.route(PREFIX + '/<int:id_user>', methods=['GET', 'OPTIONS'])
def profile(id_user):
    if request.method == 'OPTIONS':
        print(request.method)
        return make_response(jsonify({}))
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return make_response(jsonify(answer))


@app.route(PREFIX + '/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return make_response(jsonify({}))
    data = request.json
    print(f'data = {data}')
    return make_response(jsonify(Processor().login(data)))


@app.route(PREFIX + '/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    data = request.json
    print(f'data = {data}')
    return make_response(jsonify(Processor().create(data)))

