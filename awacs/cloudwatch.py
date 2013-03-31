# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon CloudWatch'
prefix = 'cloudwatch'

DeleteAlarms = Action(prefix, 'DeleteAlarms')
DescribeAlarmHistory = Action(prefix, 'DescribeAlarmHistory')
DescribeAlarms = Action(prefix, 'DescribeAlarms')
DescribeAlarmsForMetric = Action(prefix, 'DescribeAlarmsForMetric')
DisableAlarmActions = Action(prefix, 'DisableAlarmActions')
EnableAlarmActions = Action(prefix, 'EnableAlarmActions')
GetMetricStatistics = Action(prefix, 'GetMetricStatistics')
ListMetrics = Action(prefix, 'ListMetrics')
PutMetricAlarm = Action(prefix, 'PutMetricAlarm')
PutMetricData = Action(prefix, 'PutMetricData')
SetAlarmState = Action(prefix, 'SetAlarmState')
