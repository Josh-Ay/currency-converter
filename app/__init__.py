from flask import Flask
from flask_compress import Compress
from app.config import Config

compress = Compress()


def create_new_app(config_obj: Config) -> Flask:
    app = Flask(__name__, static_folder='', template_folder='')

    app.config.from_object(config_obj)
    compress.init_app(app)

    return app

