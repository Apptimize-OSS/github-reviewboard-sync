from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from mock import Mock, patch
import unittest2

from github_reviewboard_sync.credentials import _get_password


class TestGetPassword(unittest2.TestCase):
    @patch('github_reviewboard_sync.credentials.keyring')
    def test__when_password_available__returns_existing_password(self, keyring):
        expected = 'P@ssw0rd'
        keyring.get_password = Mock(return_value=expected)
        resp = _get_password('fake', 'user')
        self.assertEqual(expected, resp)
        self.assertFalse(keyring.set_password.called)

    @patch('github_reviewboard_sync.credentials.keyring')
    @patch('github_reviewboard_sync.credentials.getpass')
    def test__when_password_not_set__gets_from_user_and_sets(self, getpass, keyring):
        expected = 'P@ssw0rd'
        keyring.get_password = Mock(return_value=None)
        getpass.return_value = expected
        resp = _get_password('fake', 'user')
        self.assertEqual(resp, expected)
        self.assertTrue(getpass.called)
        self.assertTrue(keyring.set_password.called)
        self.assertTupleEqual(('sync-fake', 'user', expected), keyring.set_password.call_args[0])

    @patch('github_reviewboard_sync.credentials.keyring')
    @patch('github_reviewboard_sync.credentials.getpass')
    def test__when_refreshing__gets_from_user_and_sets(self, getpass, keyring):
        expected = 'P@ssw0rd'
        getpass.return_value = expected
        resp = _get_password('fake', 'user', refresh=True)
        self.assertFalse(keyring.get_password.called)
        self.assertEqual(resp, expected)
        self.assertTrue(getpass.called)
        self.assertTrue(keyring.set_password.called)
        self.assertTupleEqual(('sync-fake', 'user', expected), keyring.set_password.call_args[0])
