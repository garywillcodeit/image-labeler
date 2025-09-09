from flask import render_template
from ..controllers.app_init import app_init


def home_route():
    app_init()
    return render_template("index.html")
