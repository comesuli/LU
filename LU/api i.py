from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager, create_access_token   #1

class User(object):
    def __init__(self,username, password):
        self.username = username
        self.password = password


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!  2
jwt = JWTManager(app)                           # 3
users = {}
@app.route('/signup', methods=['POST'])
def signup():
   # if not request.is_json:
      #  return jsonify({"msg": "Missing JSON in request"}), 400  # 4.5
    username = request.form['username']
    password = request.form['password']
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if username in users:
        return jsonify({"msg": "This username have used!"}),201
    users[username]=User(username,password)
    return jsonify({"msg": "Signup success!"}), 200


@app.route('/login', methods=['POST'])
def login():                                               #
   #  if not request.is_json:
        #  return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.form['username']  #
    password = request.form['password']  #
    if (not username) or (not password):           #
        return jsonify({"msg": "Missing username or password parameter"}), 400  #
    loginuser = users.get(username,None)        # 6
    if not loginuser:
        return jsonify({"msg":"username not exists"}), 400
    elif loginuser.password == password:
        return jsonify(access_token=create_access_token(identity=username)), 200    # 8
    else:
        return jsonify({"msg":"Username or password is not correct!"}), 401     # 9


if __name__ == "__main__":
    app.run()
