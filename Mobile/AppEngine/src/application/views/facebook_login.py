"""
.. module:: application.settings
    :synopsis: Provides views for the facebook authentication
"""


from flask import url_for, request, session, redirect
from flask_oauth import OAuth
from google.appengine.ext import ndb
from google.appengine.api import users

from application import app
from application.models import User


__all__ = ['facebook_login', 'facebook_authorized', 'logout']


oauth = OAuth()


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config['FACEBOOK_APP_ID'],
    consumer_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params={'scope': ('email, user_friends, ')}
)


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


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')


@app.route('/facebook_login')
def facebook_login():
    return facebook.authorize(
        callback=url_for('facebook_authorized',
                         next=request.args.get('next'),
                         _external=True))


@app.route('/facebook_authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    # Make use of the connection to retrieves the user's info
    profile = facebook.get('/me').data
    profile_id = profile['id'].decode('utf-8')
    user_entry = ndb.Key('User', profile_id).get()

    if not user_entry:
        friends = facebook.get('/me/friends').data
        add_user(profile, friends)

    # Add new token to the user entry
    user = User.get_by_id(profile_id)
    user.token = resp['access_token']
    user.put()

    session['profile_id'] = profile['id'].decode('utf-8')

    return redirect('/#/friends')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)
    session.pop('profile_id', None)
    return redirect(url_for('index'))
