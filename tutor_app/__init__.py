from flask import Flask

from .home.routes import home
from .tutors.routes import tutors

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret"

    app.register_blueprint(home)
    app.register_blueprint(tutors)

    return app
