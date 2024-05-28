#!/usr/bin/env python3
"""A flask applicaion"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
app = Flask(__name__)

babel = Babel(app)


class Config:
    """Class to configure babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LANGUAGE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determines the best match with supported laguages for every request"""

    # Check if the incoming request contains the 'locale' argument
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config("LANGUAGES"))


app.route("/")


def index():
    """returns the template attached to it"""
    return render_template("index.html", title=_("home_title"),
                           header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)
