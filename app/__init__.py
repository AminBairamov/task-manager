from flask import Flask
from .database import db
from .users import users_bp
from .routes.tasks import tasks_bp

__all__ = [db]

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    @app.route("/")
    def index():
        return "Hello, Task Manager!"

    @app.route("/favicon.ico")
    def favicon():
        return "", 204


    return app

