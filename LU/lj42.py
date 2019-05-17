from flask import jsonify,request,Blueprint
from flask_jwt_extended import create_access_token
class Lujing(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
lujings={}

lu = Blueprint('lu', __name__)

@lu.route('/signup',methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"msg":"Missing JSON in request"})
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username in lujings:
        return jsonify({"msg":"this username had use"})
    lujings[username] = Lujing(username, password)
    return jsonify({"msg":"success!"})
jing = Blueprint('jing', __name__)
@jing.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"})
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"msg": "Missing name or password"})
    loginuser=lujings.get(username,None)
    if not loginuser:
        return jsonify({"msg":"username not exists"})
    elif loginuser.password == password:
        return jsonify(access_token=create_access_token(identity=username))
    else:
        return jsonify({"msg":"username or password is not correct!"})