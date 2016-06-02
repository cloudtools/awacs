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


CancelExportTask = Action('CancelExportTask')
CreateExportTask = Action('CreateExportTask')
CreateLogGroup = Action('CreateLogGroup')
CreateLogStream = Action('CreateLogStream')
DeleteDestination = Action('DeleteDestination')
DeleteLogGroup = Action('DeleteLogGroup')
DeleteLogStream = Action('DeleteLogStream')
DeleteMetricFilter = Action('DeleteMetricFilter')
DeleteRetentionPolicy = Action('DeleteRetentionPolicy')
DeleteSubscriptionFilter = Action('DeleteSubscriptionFilter')
DescribeDestinations = Action('DescribeDestinations')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeLogGroups = Action('DescribeLogGroups')
DescribeLogStreams = Action('DescribeLogStreams')
DescribeMetricFilters = Action('DescribeMetricFilters')
DescribeSubscriptionFilters = Action('DescribeSubscriptionFilters')
FilterLogEvents = Action('FilterLogEvents')
GetLogEvents = Action('GetLogEvents')
PutDestination = Action('PutDestination')
PutDestinationPolicy = Action('PutDestinationPolicy')
PutLogEvents = Action('PutLogEvents')
PutMetricFilter = Action('PutMetricFilter')
PutRetentionPolicy = Action('PutRetentionPolicy')
PutSubscriptionFilter = Action('PutSubscriptionFilter')
TestMetricFilter = Action('TestMetricFilter')
