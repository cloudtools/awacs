# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EventBridge Schemas'
prefix = 'schemas'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDiscoverer = Action('CreateDiscoverer')
CreateRegistry = Action('CreateRegistry')
CreateSchema = Action('CreateSchema')
DeleteDiscoverer = Action('DeleteDiscoverer')
DeleteRegistry = Action('DeleteRegistry')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteSchema = Action('DeleteSchema')
DeleteSchemaVersion = Action('DeleteSchemaVersion')
DescribeCodeBinding = Action('DescribeCodeBinding')
DescribeDiscoverer = Action('DescribeDiscoverer')
DescribeRegistry = Action('DescribeRegistry')
DescribeSchema = Action('DescribeSchema')
GetCodeBindingSource = Action('GetCodeBindingSource')
GetDiscoveredSchema = Action('GetDiscoveredSchema')
GetResourcePolicy = Action('GetResourcePolicy')
ListDiscoverers = Action('ListDiscoverers')
ListRegistries = Action('ListRegistries')
ListSchemaVersions = Action('ListSchemaVersions')
ListSchemas = Action('ListSchemas')
ListTagsForResource = Action('ListTagsForResource')
PutCodeBinding = Action('PutCodeBinding')
PutResourcePolicy = Action('PutResourcePolicy')
SearchSchemas = Action('SearchSchemas')
StartDiscoverer = Action('StartDiscoverer')
StopDiscoverer = Action('StopDiscoverer')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDiscoverer = Action('UpdateDiscoverer')
UpdateRegistry = Action('UpdateRegistry')
UpdateSchema = Action('UpdateSchema')
