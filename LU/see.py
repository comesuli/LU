from flask import Blueprint

pig = Blueprint('pig', __name__)


@pig.route('/three', methods=['POST'])
def three():
    return "hello"