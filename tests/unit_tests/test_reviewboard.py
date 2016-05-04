from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest2

from github_reviewboard_sync.reviewboard import _create_args


class TestCreateArgs(unittest2.TestCase):
    def test__when_update_false__no_updates_arg(self):
        expected = [
            'rbt',
            'post',
            '-o',
            '--tracking-branch',
            'remote/base',
            'remote/base..remote/branch'
        ]
        resp = _create_args('branch', 'base', 'remote')
        self.assertListEqual(expected, resp)

    def test__when_update_true__update_arg_included(self):
        expected = [
            'rbt',
            'post',
            '-o',
            '-u',
            '--tracking-branch',
            'remote/base',
            'remote/base..remote/branch'
        ]
        resp = _create_args('branch', 'base', 'remote', update=True)
        self.assertListEqual(expected, resp)
