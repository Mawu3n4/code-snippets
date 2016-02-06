from flask import Response
from flask.views import MethodView


class HelloWorldView(MethodView):

    def get(self):
        return Response('Hello world!', status=200)
