import json

import facebook
from flask import request, Response, session
from flask.views import MethodView
from google.appengine.ext import ndb

from application import app
from application.models import User


class FriendsWebhook(MethodView):
    def get(self):
        mode = request.args.get('hub.mode')
        challenge = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')

        if verify_token != app.config['WEBHOOK_TOKEN']:
            return Reponse(status=400)

        return Response(challenge, status=200)

    def post(self, data):
        print(data)

def add_user(profile, friends):
    user = User(
        id=profile['id'].decode('utf-8'),
        name=profile['name'].decode('utf-8')
    )

    for friend in friends['data']:
        entry = User.get_or_insert(
            friend['id'].decode('utf-8'),
            name=friend['name'].decode('utf-8')
        )
        user.friends.append(entry.key)
    user.put()

class FriendsView(MethodView):

    def get(self):
        code = 200
        graph = facebook.GraphAPI(session['facebook_token'][0])
        profile = graph.get_object("me")
        user_entry = ndb.Key('User', profile['id'].decode('utf-8')).get()

        # If it's the user's first time, create its entry and friend list
        if not user_entry:
            friends = graph.get_connections("me", "friends")
            add_user(profile, friends)
        user = User.get_by_id(profile['id'].decode('utf-8'))

        data = {
            'friends': [{'name': f.name} for f in ndb.get_multi(user.friends)]
        }
        data['count'] = len(data['friends'])
        return Response(json.dumps(data), status=code)

app.add_url_rule('/webhooks/friends', view_func=FriendsWebhook.as_view('friends-webhook'))
app.add_url_rule('/api/friends', view_func=FriendsView.as_view('friends-view'))
