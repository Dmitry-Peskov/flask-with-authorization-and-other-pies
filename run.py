from flask import Flask
from config import config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.database.dsn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


if __name__ == "__main__":
    web_portal = create_app()
    web_portal.run(
        host=config.app.host,
        port=config.app.port,
        debug=config.app.debug
    )
