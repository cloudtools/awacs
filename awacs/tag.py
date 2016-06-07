# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction

service_name = 'AWS Tag Editor'
prefix = 'tag'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


AddResourceTags = Action('AddResourceTags')
GetResources = Action('GetResources')
GetTags = Action('GetTags')
GetTagKeys = Action('GetTagKeys')
GetTagValues = Action('GetTagValues')
RemoveResourceTags = Action('RemoveResourceTags')
