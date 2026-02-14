from flask import Flask
import os

def create_app():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app = Flask(
        __name__,
        static_folder=os.path.join(base_dir, "static"),
        template_folder=os.path.join(base_dir, "templates")
    )

    from app.routes import main
    app.register_blueprint(main)

    return app
