# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudWatch Logs'
prefix = 'logs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateKmsKey = Action('AssociateKmsKey')
CancelExportTask = Action('CancelExportTask')
CreateExportTask = Action('CreateExportTask')
CreateLogGroup = Action('CreateLogGroup')
CreateLogStream = Action('CreateLogStream')
DeleteDestination = Action('DeleteDestination')
DeleteLogGroup = Action('DeleteLogGroup')
DeleteLogStream = Action('DeleteLogStream')
DeleteMetricFilter = Action('DeleteMetricFilter')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteRetentionPolicy = Action('DeleteRetentionPolicy')
DeleteSubscriptionFilter = Action('DeleteSubscriptionFilter')
DescribeDestinations = Action('DescribeDestinations')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeLogGroups = Action('DescribeLogGroups')
DescribeLogStreams = Action('DescribeLogStreams')
DescribeMetricFilters = Action('DescribeMetricFilters')
DescribeResourcePolicies = Action('DescribeResourcePolicies')
DescribeSubscriptionFilters = Action('DescribeSubscriptionFilters')
DisassociateKmsKey = Action('DisassociateKmsKey')
FilterLogEvents = Action('FilterLogEvents')
GetLogEvents = Action('GetLogEvents')
ListTagsLogGroup = Action('ListTagsLogGroup')
PutDestination = Action('PutDestination')
PutDestinationPolicy = Action('PutDestinationPolicy')
PutLogEvents = Action('PutLogEvents')
PutMetricFilter = Action('PutMetricFilter')
PutResourcePolicy = Action('PutResourcePolicy')
PutRetentionPolicy = Action('PutRetentionPolicy')
PutSubscriptionFilter = Action('PutSubscriptionFilter')
TagLogGroup = Action('TagLogGroup')
TestMetricFilter = Action('TestMetricFilter')
UntagLogGroup = Action('UntagLogGroup')
