from flask import request, jsonify
from app import app
from app.rating.processor import Processor
from app.base.helper import header_option, session_to_id_user

PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET', 'OPTIONS'])
def all_rating():
    if request.method == 'OPTIONS':
        return jsonify({}), header_option()
    id_user = session_to_id_user(request.headers) or None
    top = Processor().get_top_users(id_user)
    func = {
        'top': top
    }
    answer = jsonify(func)
    return answer, header_option()
