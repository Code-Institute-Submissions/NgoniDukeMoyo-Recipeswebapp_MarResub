from flask import Flask j

from .extentions import mango

def create_app():
    app = flask(__name__)

    mango.init_app(app)

    return app