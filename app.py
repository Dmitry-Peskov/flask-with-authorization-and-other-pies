from flask import Flask
from config import config
from core import database, migrations, login_manger, BaseModel
from apps import auth_route, auth_models, registration_route


def create_app() -> Flask:
    # Инстанцируем и конфигурируем приложение
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.database.dsn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config.project.secret_key
    # Подключаем компоненты
    database.init_app(app)
    migrations.init_app(app)
    # login_manger.init_app(app)
    # Подключаем маршруты
    app.register_blueprint(registration_route, url_prefix="/registration")
    app.register_blueprint(auth_route, url_prefix="/auth")
    return app


if __name__ == "__main__":
    web_portal = create_app()
    web_portal.run(
        debug=config.app.debug
    )
