"""
.. module:: application.urls
    :synopsis: Register routes of the application
"""


from flask import render_template

from application import app
from application.views import HelloWorldView


app.add_url_rule('/', 'hello_world', view_func=HelloWorldView.as_view('helloworld'))

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
