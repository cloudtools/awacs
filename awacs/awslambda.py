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


AddLayerVersionPermission = Action('AddLayerVersionPermission')
AddPermission = Action('AddPermission')
CreateAlias = Action('CreateAlias')
CreateEventSourceMapping = Action('CreateEventSourceMapping')
CreateFunction = Action('CreateFunction')
DeleteAlias = Action('DeleteAlias')
DeleteEventSourceMapping = Action('DeleteEventSourceMapping')
DeleteFunction = Action('DeleteFunction')
DeleteFunctionConcurrency = Action('DeleteFunctionConcurrency')
DeleteLayerVersion = Action('DeleteLayerVersion')
EnableReplication = Action('EnableReplication')
GetAccountSettings = Action('GetAccountSettings')
GetAlias = Action('GetAlias')
GetEventSourceMapping = Action('GetEventSourceMapping')
GetFunction = Action('GetFunction')
GetFunctionConfiguration = Action('GetFunctionConfiguration')
GetLayerVersion = Action('GetLayerVersion')
GetLayerVersionPolicy = Action('GetLayerVersionPolicy')
GetPolicy = Action('GetPolicy')
InvokeAsync = Action('InvokeAsync')
InvokeFunction = Action('InvokeFunction')
ListAliases = Action('ListAliases')
ListEventSourceMappings = Action('ListEventSourceMappings')
ListFunctions = Action('ListFunctions')
ListLayerVersions = Action('ListLayerVersions')
ListLayers = Action('ListLayers')
ListTags = Action('ListTags')
ListVersionsByFunction = Action('ListVersionsByFunction')
PublishLayerVersion = Action('PublishLayerVersion')
PublishVersion = Action('PublishVersion')
PutFunctionConcurrency = Action('PutFunctionConcurrency')
RemoveLayerVersionPermission = Action('RemoveLayerVersionPermission')
RemovePermission = Action('RemovePermission')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAlias = Action('UpdateAlias')
UpdateEventSourceMapping = Action('UpdateEventSourceMapping')
UpdateFunctionCode = Action('UpdateFunctionCode')
UpdateFunctionConfiguration = Action('UpdateFunctionConfiguration')
