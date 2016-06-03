# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudWatch'
prefix = 'cloudwatch'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DeleteAlarms = Action('DeleteAlarms')
DescribeAlarmHistory = Action('DescribeAlarmHistory')
DescribeAlarms = Action('DescribeAlarms')
DescribeAlarmsForMetric = Action('DescribeAlarmsForMetric')
DisableAlarmActions = Action('DisableAlarmActions')
EnableAlarmActions = Action('EnableAlarmActions')
GetMetricData = Action('GetMetricData')
GetMetricStatistics = Action('GetMetricStatistics')
ListMetrics = Action('ListMetrics')
PutMetricAlarm = Action('PutMetricAlarm')
PutMetricData = Action('PutMetricData')
SetAlarmState = Action('SetAlarmState')
