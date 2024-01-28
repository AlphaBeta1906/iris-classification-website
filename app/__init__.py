from flask import Flask

app = Flask(__name__)

def create_app():
    from .routes import routes
    
    app.register_blueprint(routes)

    return app