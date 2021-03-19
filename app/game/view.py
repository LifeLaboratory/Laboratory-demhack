from flask import request, jsonify
from app import app
from app.game.processor import Processor
from app.base.helper import header_option, session_to_id_user

PREFIX = '/api/game'


@app.route(PREFIX, methods=['GET'])
def get_game_info():
    if request.method == 'GET':
        id_user = session_to_id_user(request.headers)
        return jsonify(Processor().get_game_info(id_user), header_option())


@app.route(PREFIX + '/question', methods=['POST', 'OPTIONS'])
def send_game_answer():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()

    json_data = request.json
    return jsonify(Processor().send_game_answer(json_data)), header_option()


@app.route(PREFIX + '/events', methods=['GET', 'OPTIONS'])
def get_game_events():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()

    id_user = session_to_id_user(request.headers)
    return jsonify({'event': Processor().get_game_events(id_user)}), header_option()


@app.route(PREFIX + '/action', methods=['POST', 'OPTIONS'])
def execute_game_action():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()

    data = request.json
    print(f'data = {data}')
    return jsonify(Processor().execute_game_action(data)), header_option()
