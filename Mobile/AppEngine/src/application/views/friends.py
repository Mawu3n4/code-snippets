import json

import facebook
from flask import request, Response, session, redirect
from flask.views import MethodView
from google.appengine.ext import ndb
from google.appengine.api import users

from application import app
from application.models import User


def update_friendlists(user):
    graph = facebook.GraphAPI(user.token)
    profile = graph.get_object("me")
    friends = graph.get_connections("me", "friends")

    for friend in friends['data']:
        entry = User.get_or_insert(
            friend['id'].decode('utf-8'),
            name=friend['name'].decode('utf-8')
        )
        entry.friends.append(user.key)
        entry.put()


class FriendsWebhook(MethodView):
    def get(self):
        mode = request.args.get('hub.mode')
        challenge = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')

        if verify_token != app.config['WEBHOOK_TOKEN']:
            return Response(status=400)

        return Response(challenge, status=200)

    def post(self):
        data = request.get_json(silent=True, force=True)

        # Only one permission is hooked
        entry = data['entry'][0]

        profile_id = entry['uid']
        new_friend = User.get_by_id(profile_id)

        if entry['changed_fields'][0] == 'user_friends':
            # Add current user to his friends friend lists
            update_friendlists(new_friend)

        return Response(status=200)


class FriendsView(MethodView):

    def get(self):
        profile_id = request.args.get('profile_id')
        if not profile_id and not session.get('profile_id'):
            return redirect('/#/login')
        profile_id = profile_id or session.get('profile_id')
        user = User.get_by_id(profile_id)
        if not user:
            return Response(
                'No profile \'{}\' found. Please specify profile_id'.format(profile_id),
                status=400
            )

        data = {
            'friends': [{'name': f.name} for f in ndb.get_multi(user.friends)]
        }
        data['count'] = len(data['friends'])

        return Response(json.dumps(data), status=200)


app.add_url_rule('/webhooks/friends', view_func=FriendsWebhook.as_view('friends-webhook'))
app.add_url_rule('/api/friends', view_func=FriendsView.as_view('friends-view'))
