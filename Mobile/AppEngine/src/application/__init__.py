"""
.. module:: application
    :synopsis: Initialise the app
"""

import os

from flask import Flask

app = Flask('application')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

import urls
