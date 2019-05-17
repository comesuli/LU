from flask import Flask
from flask_jwt_extended import JWTManager
import test.talk as talk
import test.pas as pas

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!  2
jwt = JWTManager(app)

app.register_blueprint(talk.talk1)
app.register_blueprint(pas.user1)
app.register_blueprint(pas.pas2)

if __name__ == '__main__':
    app.run(debug=True)
