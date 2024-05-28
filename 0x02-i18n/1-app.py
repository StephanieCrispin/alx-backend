#!/usr/bin/env python3
"""A flask applicaion"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)

babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LANGUAGE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

app.route("/")


def index():
    """returns the template attached to it"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
