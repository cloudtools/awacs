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
DeleteDashboards = Action('DeleteDashboards')
DescribeAlarmHistory = Action('DescribeAlarmHistory')
DescribeAlarms = Action('DescribeAlarms')
DescribeAlarmsForMetric = Action('DescribeAlarmsForMetric')
DisableAlarmActions = Action('DisableAlarmActions')
EnableAlarmActions = Action('EnableAlarmActions')
GetDashboard = Action('GetDashboard')
GetMetricData = Action('GetMetricData')
GetMetricStatistics = Action('GetMetricStatistics')
GetMetricWidgetImage = Action('GetMetricWidgetImage')
ListDashboards = Action('ListDashboards')
ListMetrics = Action('ListMetrics')
ListTagsForResource = Action('ListTagsForResource')
PutDashboard = Action('PutDashboard')
PutMetricAlarm = Action('PutMetricAlarm')
PutMetricData = Action('PutMetricData')
SetAlarmState = Action('SetAlarmState')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
