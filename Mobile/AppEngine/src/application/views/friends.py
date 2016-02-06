import json

from flask import request, Response
from flask.views import MethodView

from application import app
from application.models import Friendship

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

class FriendsView(MethodView):

    def get(self):
        code = 200
        data = Friends.all()

        return Response(json.dumpps(data), status=code)

app.add_url_rule('/webhooks/friends', view_func=FriendsWebhook.as_view('friends-webhook'))
app.add_url_rule('/api/friends', view_func=FriendsView.as_view('friends-view'))
