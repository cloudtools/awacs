# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Directory Service'
prefix = 'ds'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateComputer = Action('CreateComputer')
CreateDirectory = Action('CreateDirectory')
CreateSnapshot = Action('CreateSnapshot')
CheckAlias = Action('CheckAlias')
ConnectDirectory = Action('ConnectDirectory')
DeleteDirectory = Action('DeleteDirectory')
DeleteSnapshot = Action('DeleteSnapshot')
DescribeDirectories = Action('DescribeDirectories')
DescribeSnapshots = Action('DescribeSnapshots')
GetDirectoryLimits = Action('GetDirectoryLimits')
GetSnapshotLimits = Action('GetSnapshotLimits')
ListAuthorizedApplications = Action('ListAuthorizedApplications')
RepairDirectory = Action('RepairDirectory')
RestoreFromSnapshot = Action('RestoreFromSnapshot')
UpdateDirectory = Action('UpdateDirectory')
