import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from user import user_blue
from workshop import workshop_blue
from square import square_blue
from forum import forum_blue

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, use_native_unicode='utf8')
CORS(app, supports_credentials=True)


app.register_blueprint(user_blue)
app.register_blueprint(workshop_blue)
app.register_blueprint(square_blue)
app.register_blueprint(forum_blue)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
