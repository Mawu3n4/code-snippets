from flask import Flask
from settings import configuration

app = Flask('application')
app.config.update(**configuration)

import urls
