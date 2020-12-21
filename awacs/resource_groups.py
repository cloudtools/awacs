# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Resource Groups'
prefix = 'resource-groups'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateGroup = Action('CreateGroup')
DeleteGroup = Action('DeleteGroup')
GetGroup = Action('GetGroup')
GetGroupConfiguration = Action('GetGroupConfiguration')
GetGroupQuery = Action('GetGroupQuery')
GetTags = Action('GetTags')
GroupResources = Action('GroupResources')
ListGroupResources = Action('ListGroupResources')
ListGroups = Action('ListGroups')
PutGroupPolicy = Action('PutGroupPolicy')
SearchResources = Action('SearchResources')
Tag = Action('Tag')
UngroupResources = Action('UngroupResources')
Untag = Action('Untag')
UpdateGroup = Action('UpdateGroup')
UpdateGroupQuery = Action('UpdateGroupQuery')
