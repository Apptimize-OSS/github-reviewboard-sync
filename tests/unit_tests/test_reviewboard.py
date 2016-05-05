from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import mock
import unittest2

from github_reviewboard_sync.reviewboard import _create_args


class TestCreateArgs(unittest2.TestCase):
    @mock.patch('github_reviewboard_sync.reviewboard.construct_message')
    def test__when_update_false__no_updates_arg(self, construct_message):
        title = 'title',
        description = 'description'
        construct_message.return_value = title, description
        expected = [
            'rbt',
            'post',
            '-o',
            '--description',
            "'{0}'".format(description),
            '--summary',
            "'{0}'".format(title),
            '--tracking-branch',
            'remote/base',
            'remote/base..remote/branch'
        ]
        resp = _create_args(mock.Mock(), 'branch', 'base', 'remote')
        self.assertListEqual(expected, resp)

    @mock.patch('github_reviewboard_sync.reviewboard.construct_message')
    def test__when_update_true__update_arg_included(self, construct_message):
        title = 'title',
        description = 'description'
        construct_message.return_value = title, description
        expected = [
            'rbt',
            'post',
            '-o',
            '-u',
            '--description',
            "'{0}'".format(description),
            '--summary',
            "'{0}'".format(title),
            '--tracking-branch',
            'remote/base',
            'remote/base..remote/branch'
        ]
        resp = _create_args(mock.Mock(), 'branch', 'base', 'remote', update=True)
        self.assertListEqual(expected, resp)
