from flask import request, jsonify
from app import app
from app.rating.processor import Processor
from app.base.helper import session_to_id_user
from app.base.helper import make_response
PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET', 'OPTIONS'])
def all_rating():
    if request.method == 'OPTIONS':
        return make_response(jsonify({}))
    id_user = session_to_id_user(request.headers) or None
    top = Processor().get_top_users(id_user)
    func = {
        'top': top
    }
    answer = jsonify(func)
    return make_response(answer)
