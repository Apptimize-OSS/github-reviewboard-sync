from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import re
import subprocess

from github_reviewboard_sync.repo import construct_message, get_repo

_LOG = logging.getLogger(__name__)


def post_to_review_board(path, branch, base, remote, update=False, pull_url=None):
    """
    Opens or updates a review board submission

    :param unicode branch:
    :param unicode base:
    :param unicode remote:
    :param bool update:
    :param unicode pull_url: The url of the pull request
    """
    repo = get_repo(path)
    if update:
        _LOG.info('Updating Reviewboard submission for {0}'.format(branch))
    else:
        _LOG.info('Creating new ReviewBoard submission for "{0}"'.format(branch))
    args = _create_args(repo, branch, base, remote, update=update, pull_url=pull_url)
    _LOG.debug('RBT arguments: {0}'.format(args))

    subprocess.call(args)


def _create_args(repo, branch, base, remote, update=False, pull_url=None):
    """
    Creates the necessary arguments for the subprocess call
    """
    args = ['rbt', 'post', '-o']
    if update:
        args.append('-u')
    else:
        summary, description = construct_message(repo, base, branch)
        if pull_url:
            description = '{0}\n\nPull Request: {1}'.format(description, pull_url)
        args += ['--description', "Autogenerated: {0}".format(description), '--summary', summary]

    return args + ['--tracking-branch', base, '{0}..{1}'.format(base, branch)]


def _parse_output(output):
    url_finder = re.compile(r'Review request #[0-9]+ posted.\n\n(http[^\n]+/)\n')
    output = re.search(url_finder, output)
    if not output:
        _LOG.error('Couldn\'t find the url, There may have been a failure')
    else:
        _LOG.debug('Successfully found submitted review request')
        return output.group(1)
