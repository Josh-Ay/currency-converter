from app.error_handlers.blueprints import error_blueprint
from flask import jsonify


@error_blueprint.errorhandler(404)
def handle_page_not_found(e):
    return jsonify('Requested resource could not be found on the server'), 404
