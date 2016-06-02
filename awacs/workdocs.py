# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon WorkDocs'
prefix = 'workdocs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ActivateUser = Action('ActivateUser')
AddUserToGroup = Action('AddUserToGroup')
CheckAlias = Action('CheckAlias')
CreateInstance = Action('CreateInstance')
DeactivateUser = Action('DeactivateUser')
DeleteInstance = Action('DeleteInstance')
DeregisterDirectory = Action('DeregisterDirectory')
DescribeAvailableDirectories = Action('DescribeAvailableDirectories')
DescribeInstances = Action('DescribeInstances')
RegisterDirectory = Action('RegisterDirectory')
RemoveUserFromGroup = Action('RemoveUserFromGroup')
UpdateInstanceAlias = Action('UpdateInstanceAlias')
