# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon DynamoDB Accelerator (DAX)'
prefix = 'dax'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetItem = Action('BatchGetItem')
BatchWriteItem = Action('BatchWriteItem')
ConditionCheckItem = Action('ConditionCheckItem')
CreateCluster = Action('CreateCluster')
CreateParameterGroup = Action('CreateParameterGroup')
CreateSubnetGroup = Action('CreateSubnetGroup')
DecreaseReplicationFactor = Action('DecreaseReplicationFactor')
DefineAttributeList = Action('DefineAttributeList')
DefineAttributeListId = Action('DefineAttributeListId')
DefineKeySchema = Action('DefineKeySchema')
DeleteCluster = Action('DeleteCluster')
DeleteItem = Action('DeleteItem')
DeleteParameterGroup = Action('DeleteParameterGroup')
DeleteSubnetGroup = Action('DeleteSubnetGroup')
DescribeClusters = Action('DescribeClusters')
DescribeDefaultParameters = Action('DescribeDefaultParameters')
DescribeEvents = Action('DescribeEvents')
DescribeParameterGroups = Action('DescribeParameterGroups')
DescribeParameters = Action('DescribeParameters')
DescribeSubnetGroups = Action('DescribeSubnetGroups')
DescribeTable = Action('DescribeTable')
GetItem = Action('GetItem')
IncreaseReplicationFactor = Action('IncreaseReplicationFactor')
ListTables = Action('ListTables')
ListTags = Action('ListTags')
PutItem = Action('PutItem')
Query = Action('Query')
RebootNode = Action('RebootNode')
Scan = Action('Scan')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateCluster = Action('UpdateCluster')
UpdateItem = Action('UpdateItem')
UpdateParameterGroup = Action('UpdateParameterGroup')
UpdateSubnetGroup = Action('UpdateSubnetGroup')
