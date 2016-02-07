from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    friends = ndb.KeyProperty(kind="User", repeated=True)
    token = ndb.StringProperty()
