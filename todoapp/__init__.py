from flask import Flask j

from .extentions import mango

def create_app():
    app = flask(__name__)

    app.config['MANGO_URI'] = 'mongodb+srv://Duke:Kingdong20@recipewebappcluster.crmag.mongodb.net/mydb?retryWrites=true&w=majority'

    mango.init_app(app)

    return app