# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Application Auto Scaling'
prefix = 'application-autoscaling'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DeleteScalingPolicy = Action('DeleteScalingPolicy')
DeleteScheduledAction = Action('DeleteScheduledAction')
DeregisterScalableTarget = Action('DeregisterScalableTarget')
DescribeScalableTargets = Action('DescribeScalableTargets')
DescribeScalingActivities = Action('DescribeScalingActivities')
DescribeScalingPolicies = Action('DescribeScalingPolicies')
DescribeScheduledActions = Action('DescribeScheduledActions')
PutScalingPolicy = Action('PutScalingPolicy')
PutScheduledAction = Action('PutScheduledAction')
RegisterScalableTarget = Action('RegisterScalableTarget')
