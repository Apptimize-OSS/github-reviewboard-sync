from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess


def open_review_board_submission(branch, base, remote, update=False):
    """
    Opens or updates a review board submission

    :param unicode branch:
    :param unicode base:
    :param unicode remote:
    :param bool update:
    """
    args = _create_args(branch, base, remote, update=update)
    subprocess.call(args)


def _create_args(branch, base, remote, update=False):
    """
    Creates the necessary arguments for the subprocess call
    """
    base = '{0}/{1}'.format(remote, base)
    branch = '{0}/{1}'.format(remote, branch)
    args = ['rbt', 'post', '-o']
    if update:
        args.append('-u')
    return args + ['--tracking-branch', base, '{0}..{1}'.format(base, branch)]
