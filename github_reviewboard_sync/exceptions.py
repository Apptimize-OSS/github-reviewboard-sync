from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class SyncException(Exception):
    pass


class MissingRemoteException(SyncException):
    pass


class MissingBranchExcpetion(SyncException):
    pass


class PushFailedException(SyncException):
    pass


class AuthenticationException(SyncException):
    pass
