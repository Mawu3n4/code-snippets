from flask import render_template

from application import app

from views import facebook_login
from views import friends

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return '404, Nothing Found', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return '500, Unexpected error: {}'.format(e), 500

@app.route("/")
def index():
    return render_template('index.html')
