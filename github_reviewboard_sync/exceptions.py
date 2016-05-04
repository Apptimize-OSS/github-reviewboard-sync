from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class SyncException(Exception):
    pass


class MissingRemoteException(Exception):
    pass


class MissingBranchExcpetion(Exception):
    pass


class PushFailedException(Exception):
    pass
