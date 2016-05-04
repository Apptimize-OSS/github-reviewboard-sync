from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from mock import Mock
import unittest2

from github_reviewboard_sync.pullrequest import _get_org_and_name_from_remote


class TestGetOrgAndNameFromRemote(unittest2.TestCase):
    def test__when_http__returns_valid(self):
        url = 'https://github.com/gitpython-developers/GitPython.git'
        self.assertReturnsValidOwnerAndRepo(url, 'gitpython-developers', 'GitPython')

    def test__when_ssh__returns_valid(self):
        url = 'git@github.com:gitpython-developers/GitPython.git'
        self.assertReturnsValidOwnerAndRepo(url, 'gitpython-developers', 'GitPython')

    def test__when_missing_git_extension_http__returns_valid(self):
        url = 'git@github.com:gitpython-developers/GitPython'
        self.assertReturnsValidOwnerAndRepo(url, 'gitpython-developers', 'GitPython')

    def test__when_missing_git_extension_ssh__returns_valid(self):
        url = 'https://github.com/gitpython-developers/GitPython'
        self.assertReturnsValidOwnerAndRepo(url, 'gitpython-developers', 'GitPython')

    def assertReturnsValidOwnerAndRepo(self, url, expected_owner, expected_repo):
        remote = self.instantiate_remote_mock(url)
        owner, repo = _get_org_and_name_from_remote(remote)
        self.assertEqual(expected_owner, owner)
        self.assertEqual(expected_repo, repo)

    @staticmethod
    def instantiate_remote_mock(url):
        get_method = Mock(return_value=url)
        config_read = Mock(get=get_method)
        return Mock(config_reader=config_read)
