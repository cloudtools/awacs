# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'QuickSight'
prefix = 'quicksight'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAdmin = Action('CreateAdmin')
CreateGroup = Action('CreateGroup')
CreateGroupMembership = Action('CreateGroupMembership')
CreateReader = Action('CreateReader')
CreateUser = Action('CreateUser')
DeleteGroup = Action('DeleteGroup')
DeleteGroupMembership = Action('DeleteGroupMembership')
DeleteUser = Action('DeleteUser')
DescribeGroup = Action('DescribeGroup')
DescribeUser = Action('DescribeUser')
GetGroupMapping = Action('GetGroupMapping')
ListGroupMemberships = Action('ListGroupMemberships')
ListGroups = Action('ListGroups')
ListUserGroups = Action('ListUserGroups')
ListUsers = Action('ListUsers')
RegisterUser = Action('RegisterUser')
SearchDirectoryGroups = Action('SearchDirectoryGroups')
SetGroupMapping = Action('SetGroupMapping')
Subscribe = Action('Subscribe')
Unsubscribe = Action('Unsubscribe')
UpdateGroup = Action('UpdateGroup')
