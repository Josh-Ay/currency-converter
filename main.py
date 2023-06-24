from app import create_new_app
from app.config import ProductionConfig
from app.error_handlers.error_handler import handle_page_not_found
from app.routes.convert_blueprint import convert_blueprint

# creating a new flask app
app = create_new_app(ProductionConfig())

# registering blueprints to handle routing and error handlers for the app
app.register_blueprint(convert_blueprint)
app.register_error_handler(404, handle_page_not_found)

if __name__ == '__main__':
    # production use
    app.run()

    # development use
    # app.run(debug=True, port=6404)
