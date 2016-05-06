from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
import keyring
import os


def get_github_username():
    return os.environ.get('GITHUB_USERNAME')


def get_github_password(username, refresh=False):
    """
    Gets the password from the keyring for the given
    username.  Requests the user to input it if not found.
    If refresh is ``True`` requires the user to update
    the password.

    :param username:
    :param refresh:
    :return:
    """
    return _get_password('github', username, refresh=refresh)


def get_reviewboard_password(username, refresh=False):
    """
    Not currently used

    :param username:
    :param refresh:
    :return:
    """
    return _get_password('reviewboard', username, refresh=refresh)


def _get_password(system, username, refresh=False):
    system_store_name = 'sync-{0}'.format(system)
    password = None
    if not refresh:
        password = keyring.get_password(system_store_name, username)
    if password is None:
        password = getpass('{0} password for "{1}":'.format(system, username))
        keyring.set_password(system_store_name, username, password)
    return password
