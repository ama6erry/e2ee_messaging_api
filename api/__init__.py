from flask import Flask

#import routes
from api.routes.status import status

def create_app():
    app = Flask(__name__)




    # Run register blueprint
    register_blueprints(app)





    return app



def register_blueprints(app: Flask):
    app.register_blueprint(status)