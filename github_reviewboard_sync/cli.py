import click

from github_reviewboard_sync.repo import merge_base_into_branch_and_push
from github_reviewboard_sync.reviewboard import open_review_board_submission
from github_reviewboard_sync.pullrequest import create_pull_request


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
@click.option('--base', '-b', type=unicode, default='master',
              help='The branch you want to compare against')
@click.option('--remote', '-r', type=unicode, default='origin',
              help='The remote that you wish create the pull request on')
@click.option('--path', '-p', type=unicode, default=None,
              help='The path to the local git repository.   '
                   'Defaults to the current working directory')
@click.option('--update', '-u', is_flag=True, default=False,
              help='Updates an existing ')
@click.option('--github-username', '-g', default=None, help='Your github username')
def open(branch, base, remote, path, update, github_username):
    """
    Opens a new pull request and review board submission for the
    branch against the base.

    Also, merges the base branch into the branch before
    creating the pull request
    """
    merge_base_into_branch_and_push(path, branch, base, remote)
    if not update:
        create_pull_request(path, branch, base, github_username, remote)
    open_review_board_submission(branch, base, remote, update=update)


if __name__ == '__main__':
    cli()
