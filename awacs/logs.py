# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon CloudWatch Logs'
prefix = 'logs'

CreateLogGroup = Action(prefix, 'CreateLogGroup')
CreateLogStream = Action(prefix, 'CreateLogStream')
DeleteLogGroup = Action(prefix, 'DeleteLogGroup')
DeleteLogStream = Action(prefix, 'DeleteLogStream')
DeleteMetricFilter = Action(prefix, 'DeleteMetricFilter')
DeleteRetentionPolicy = Action(prefix, 'DeleteRetentionPolicy')
DescribeLogGroups = Action(prefix, 'DescribeLogGroups')
DescribeLogStreams = Action(prefix, 'DescribeLogStreams')
DescribeMetricFilters = Action(prefix, 'DescribeMetricFilters')
GetLogEvents = Action(prefix, 'GetLogEvents')
PutLogEvents = Action(prefix, 'PutLogEvents')
PutMetricFilter = Action(prefix, 'PutMetricFilter')
PutRetentionPolicy = Action(prefix, 'PutRetentionPolicy')
TestMetricFilter = Action(prefix, 'TestMetricFilter')
