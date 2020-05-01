from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap= Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    #initialise blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initializing flask extensions
    from .request import configure_request
    configure_request(app)
    # Will add the views and forms

    return app