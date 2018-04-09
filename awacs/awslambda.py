# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Lambda'
prefix = 'lambda'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddPermission = Action('AddPermission')
CreateAlias = Action('CreateAlias')
CreateEventSourceMapping = Action('CreateEventSourceMapping')
CreateFunction = Action('CreateFunction')
DeleteAlias = Action('DeleteAlias')
DeleteEventSourceMapping = Action('DeleteEventSourceMapping')
DeleteFunction = Action('DeleteFunction')
DeleteFunctionConcurrency = Action('DeleteFunctionConcurrency')
EnableReplication = Action('EnableReplication')
GetAccountSettings = Action('GetAccountSettings')
GetAlias = Action('GetAlias')
GetEventSourceMapping = Action('GetEventSourceMapping')
GetFunction = Action('GetFunction')
GetFunctionConfiguration = Action('GetFunctionConfiguration')
GetPolicy = Action('GetPolicy')
InvokeAsync = Action('InvokeAsync')
InvokeFunction = Action('InvokeFunction')
ListAliases = Action('ListAliases')
ListEventSourceMappings = Action('ListEventSourceMappings')
ListFunctions = Action('ListFunctions')
ListTags = Action('ListTags')
ListVersionsByFunction = Action('ListVersionsByFunction')
PublishVersion = Action('PublishVersion')
PutFunctionConcurrency = Action('PutFunctionConcurrency')
RemovePermission = Action('RemovePermission')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAlias = Action('UpdateAlias')
UpdateEventSourceMapping = Action('UpdateEventSourceMapping')
UpdateFunctionCode = Action('UpdateFunctionCode')
UpdateFunctionConfiguration = Action('UpdateFunctionConfiguration')
