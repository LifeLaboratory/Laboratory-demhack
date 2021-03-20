from flask import request, jsonify
from app import app
from app.game.processor import Processor
from app.base.helper import header_option, session_to_id_user, check_session

PREFIX = '/api/game'


@app.route(PREFIX, methods=['GET', 'POST', 'OPTIONS'])
def get_game_info():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    if request.method == 'GET':
        id_user = session_to_id_user(request.headers)
        return jsonify(Processor().get_game_info(id_user), header_option())
    if request.method == 'POST':
        data = request.json
        check_session(data, request.headers)
        return jsonify(Processor().start_new_game(data), header_option())


@app.route(PREFIX + '/question', methods=['POST', 'OPTIONS'])
def send_game_answer():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()

    json_data = request.json
    id_user = session_to_id_user(request.headers)
    json_data['id_user'] = id_user
    return jsonify(Processor().send_game_answer(json_data), header_option())
