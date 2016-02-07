"""
.. module:: application.models
    :synopsis: Defines the User model
"""

from google.appengine.ext import ndb


class User(ndb.Model):
    """ Custom User model, use the facebook profile id as the model id """

    # Facebook auth token
    token = ndb.StringProperty()

    name = ndb.StringProperty()
    friends = ndb.KeyProperty(kind="User", repeated=True)
