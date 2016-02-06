from flask import Flask

app = Flask('application')

import urls
import views.facebook_login
