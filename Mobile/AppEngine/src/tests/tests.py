import os
import json

import mock
import unittest
from google.appengine.ext import testbed, ndb

from application import app
from application.models import User
from application.views.friends import update_friendlists


class FlaskGAETestCase(unittest.TestCase):
    def setUp(self):
        # Flask apps testing. See: http://flask.pocoo.org/docs/testing/
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        self.app = app.test_client()

        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()


class FriendsWebhookTestCase(FlaskGAETestCase):
    def test_subscription(self):
        rv = self.app.get('/webhooks/friends')
        self.assertEqual(rv.status, '400 BAD REQUEST')

        app.config['WEBHOOK_TOKEN'] = 'foobar'
        rv = self.app.get('/webhooks/friends?hub.verify_token=foo')
        self.assertEqual(rv.status, '400 BAD REQUEST')

        rv = self.app.get('/webhooks/friends?hub.verify_token=foobar&hub.challenge=42')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, '42')

    @mock.patch('application.views.friends.update_friendlists')
    def test_update(self, update_friendlists_mock):
        rv = self.app.post('/webhooks/friends')
        self.assertEqual(rv.status, '400 BAD REQUEST')

        data = {
            'entry': [{
                'uid': 42,
                'changed_fields': ['user_post', 'changed']
            }]
        }
        rv = self.app.post('/webhooks/friends', data=json.dumps(data))
        self.assertFalse(update_friendlists_mock.called)

        data = {
            'entry': [{
                'uid': 42,
                'changed_fields': ['user_friends', 'changed']
            }]
        }
        rv = self.app.post('/webhooks/friends', data=json.dumps(data))
        self.assertTrue(update_friendlists_mock.called)


class FriendsAPITestCase(FlaskGAETestCase):
    def test_get_list_errors(self):
        rv = self.app.get('/api/friends')
        self.assertEqual(rv.status, '400 BAD REQUEST')
        self.assertEqual(rv.data, 'No profile specified. Please specify profile_id')

        rv = self.app.get('/api/friends?profile_id=42')
        self.assertEqual(rv.status, '400 BAD REQUEST')
        self.assertIn('No profile \'42\'', rv.data)

    def test_get_list(self):
        user_a = User(id='42', name='Foo Bar')
        user_b = User.get_or_insert('43', name='Knuth Donald')
        user_c = User.get_or_insert('44', name='Lovelace Ada')
        user_a.friends.append(user_b.key)
        user_a.friends.append(user_c.key)
        user_a.put()

        rv = self.app.get('/api/friends?profile_id=42')
        self.assertEqual(rv.status, '200 OK')

        data = json.loads(rv.data)
        self.assertEqual(data['count'], 2)
        self.assertItemsEqual({'Knuth Donald', 'Lovelace Ada'},
                              {f['name'] for f in data['friends']})


class UpdateFriendlistsTestCase(FlaskGAETestCase):
    @mock.patch('application.views.friends.facebook.GraphAPI')
    def test_friends_updated(self, mocked_graph):

        mocked_graph.return_value.get_object.return_value = {'id': '42'}
        mocked_graph.return_value.get_connections.return_value = {'data': []}

        user = User(id='42', name='Foo Bar', token='101010')
        user.put()
        User(id='43', name='Knuth Donald', token='101010').put()
        update_friendlists(user)
        knuth = User.get_by_id('43')
        self.assertEqual(len(knuth.friends), 0)

        mocked_graph.return_value.get_connections.return_value = {'data': [{
            'id': '43', 'name': 'Knuth Donald'
        }]}
        update_friendlists(user)
        knuth = User.get_by_id('43')
        self.assertEqual(len(knuth.friends), 1)
        self.assertEqual(knuth.friends[0], user.key)


if __name__ == '__main__':
    unittest.main()
