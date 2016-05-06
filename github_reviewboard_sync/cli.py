import logging
import logging.config

import click

from github_reviewboard_sync.repo import merge_base_into_branch_and_push
from github_reviewboard_sync.reviewboard import post_to_review_board
from github_reviewboard_sync.pullrequest import create_pull_request
from github_reviewboard_sync.exceptions import SyncException
from github_reviewboard_sync.credentials import get_github_username


_LOG = logging.getLogger(__name__)


@click.group()
def cli():
    """
    A tool for integrating github pull requests
    and review board submissions
    :return:
    """
    pass


@cli.command()
@click.argument('branch', type=unicode)
@click.option('--base-branch', '-b', type=unicode, default='master',
              help='The branch you want to compare against')
@click.option('--remote', '-r', type=unicode, default='origin',
              help='The remote that you wish create the pull request on')
@click.option('--path', '-p', type=unicode, default=None,
              help='The path to the local git repository.   '
                   'Defaults to the current working directory')
@click.option('--update', '-u', is_flag=True, default=False,
              help='Updates an existing review board submission')
@click.option('--github-username', '-g', default=None,
              help='Your github username')
@click.option('--verbose', '-v', is_flag=True, default=False,
              help='Verbose output')
def open(branch, base_branch, remote, path, update, github_username, verbose):
    """
    Opens a new pull request and review board submission for the
    branch against the base.

    Also, merges the base branch into the branch before
    creating the pull request
    """
    github_username = github_username or get_github_username()
    if not github_username:
        _LOG.error('Either the `--github-username` option must be passed '
                   'or an environment variable called `GITHUB_USERNAME` must '
                   'be set.')
    _setup_logging(debug=verbose)
    try:
        merge_base_into_branch_and_push(branch,
                                        base_name=base_branch,
                                        remote_name=remote,
                                        path=path)
        url = None
        pull_request = None
        if not update:
            pull_request = create_pull_request(path, branch, base_branch, github_username, remote)
            if pull_request:
                url = pull_request.html_url
        review_url = post_to_review_board(path, branch, base_branch, remote, update=update, pull_url=url)
        if pull_request and review_url:
            pull_request.create_issue_comment('Review Board URL: {0}'.format(review_url))
    except SyncException as e:
        if verbose:
            raise e
        else:
            _LOG.error(str(e))


def _setup_logging(debug=False):
    loggers = {}

    if debug:
        loggers['github_reviewboard_sync'] = {
            'handlers': 'default',
            'level': 'DEBUG',
            'propagate': True
        }
    else:
        loggers['github_reviewboard_sync'] = {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(levelname)s] %(name)s: %(message)s'
            }
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': loggers
    })


if __name__ == '__main__':
    cli()
