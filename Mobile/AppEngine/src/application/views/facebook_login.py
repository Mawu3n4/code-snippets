
from flask import url_for, request, session, redirect
from flask_oauth import OAuth

from application import app

__all__ = ['facebook_login', 'facebook_authorized', 'logout']

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config['FACEBOOK_APP_ID'],
    consumer_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

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

    return redirect('/friends')

@app.route('/logout')
def logout():
    pop_login_session()
    return redirect(url_for('index'))
