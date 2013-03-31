# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Auto Scaling'
prefix = 'autoscaling'

CreateAutoScalingGroup = Action(prefix, 'CreateAutoScalingGroup')
CreateLaunchConfiguration = Action(prefix, 'CreateLaunchConfiguration')
CreateOrUpdateScalingTrigger = \
    Action(prefix, 'CreateOrUpdateScalingTrigger')
CreateOrUpdateTags = Action(prefix, 'CreateOrUpdateTags')
DeleteAutoScalingGroup = Action(prefix, 'DeleteAutoScalingGroup')
DeleteLaunchConfiguration = Action(prefix, 'DeleteLaunchConfiguration')
DeleteNotificationConfiguration = \
    Action(prefix, 'DeleteNotificationConfiguration')
DeletePolicy = Action(prefix, 'DeletePolicy')
DeleteScheduledAction = Action(prefix, 'DeleteScheduledAction')
DeleteTags = Action(prefix, 'DeleteTags')
DeleteTrigger = Action(prefix, 'DeleteTrigger')
DescribeAdjustmentTypes = Action(prefix, 'DescribeAdjustmentTypes')
DescribeAutoScalingGroups = Action(prefix, 'DescribeAutoScalingGroups')
DescribeAutoScalingInstances = \
    Action(prefix, 'DescribeAutoScalingInstances')
DescribeAutoScalingNotificationTypes = \
    Action(prefix, 'DescribeAutoScalingNotificationTypes')
DescribeLaunchConfigurations = \
    Action(prefix, 'DescribeLaunchConfigurations')
DescribeMetricCollectionTypes = \
    Action(prefix, 'DescribeMetricCollectionTypes')
DescribeNotificationConfigurations = \
    Action(prefix, 'DescribeNotificationConfigurations')
DescribePolicies = Action(prefix, 'DescribePolicies')
DescribeScalingActivities = Action(prefix, 'DescribeScalingActivities')
DescribeScalingProcessTypes = \
    Action(prefix, 'DescribeScalingProcessTypes')
DescribeScheduledActions = Action(prefix, 'DescribeScheduledActions')
DescribeTags = Action(prefix, 'DescribeTags')
DescribeTriggers = Action(prefix, 'DescribeTriggers')
DisableMetricsCollection = Action(prefix, 'DisableMetricsCollection')
EnableMetricsCollection = Action(prefix, 'EnableMetricsCollection')
ExecutePolicy = Action(prefix, 'ExecutePolicy')
PutNotificationConfiguration = \
    Action(prefix, 'PutNotificationConfiguration')
PutScalingPolicy = Action(prefix, 'PutScalingPolicy')
PutScheduledUpdateGroupAction = \
    Action(prefix, 'PutScheduledUpdateGroupAction')
ResumeProcesses = Action(prefix, 'ResumeProcesses')
SetDesiredCapacity = Action(prefix, 'SetDesiredCapacity')
SetInstanceHealth = Action(prefix, 'SetInstanceHealth')
SuspendProcesses = Action(prefix, 'SuspendProcesses')
TerminateInstanceInAutoScalingGroup = \
    Action(prefix, 'TerminateInstanceInAutoScalingGroup')
UpdateAutoScalingGroup = Action(prefix, 'UpdateAutoScalingGroup')
