# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Auto Scaling'
prefix = 'autoscaling'

AttachInstances = Action(prefix, 'AttachInstances')
CompleteLifecycleAction = Action(prefix, 'CompleteLifecycleAction')
CreateAutoScalingGroup = Action(prefix, 'CreateAutoScalingGroup')
CreateLaunchConfiguration = Action(prefix, 'CreateLaunchConfiguration')
CreateOrUpdateScalingTrigger = \
    Action(prefix, 'CreateOrUpdateScalingTrigger')
CreateOrUpdateTags = Action(prefix, 'CreateOrUpdateTags')
DeleteAutoScalingGroup = Action(prefix, 'DeleteAutoScalingGroup')
DeleteLaunchConfiguration = Action(prefix, 'DeleteLaunchConfiguration')
DeleteLifecycleHook = Action(prefix, 'DeleteLifecycleHook')
DeleteNotificationConfiguration = \
    Action(prefix, 'DeleteNotificationConfiguration')
DeletePolicy = Action(prefix, 'DeletePolicy')
DeleteScheduledAction = Action(prefix, 'DeleteScheduledAction')
DeleteTags = Action(prefix, 'DeleteTags')
DeleteTrigger = Action(prefix, 'DeleteTrigger')
DescribeAccountLimits = Action(prefix, 'DescribeAccountLimits')
DescribeAdjustmentTypes = Action(prefix, 'DescribeAdjustmentTypes')
DescribeAutoScalingGroups = Action(prefix, 'DescribeAutoScalingGroups')
DescribeAutoScalingInstances = \
    Action(prefix, 'DescribeAutoScalingInstances')
DescribeAutoScalingNotificationTypes = \
    Action(prefix, 'DescribeAutoScalingNotificationTypes')
DescribeLaunchConfigurations = \
    Action(prefix, 'DescribeLaunchConfigurations')
DescribeLifecycleHookTypes = \
    Action(prefix, 'DescribeLifecycleHookTypes')
DescribeLifecycleHooks = Action(prefix, 'DescribeLifecycleHooks')
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
DescribeTerminationPolicyTypes = \
    Action(prefix, 'DescribeTerminationPolicyTypes')
DescribeTriggers = Action(prefix, 'DescribeTriggers')
DetachInstances = Action(prefix, 'DetachInstances')
DisableMetricsCollection = Action(prefix, 'DisableMetricsCollection')
EnableMetricsCollection = Action(prefix, 'EnableMetricsCollection')
EnterPolicy = Action(prefix, 'EnterPolicy')
EnterStandby = Action(prefix, 'EnterStandby')
ExecutePolicy = Action(prefix, 'ExecutePolicy')
ExitPolicy = Action(prefix, 'ExitPolicy')
ExitStandby = Action(prefix, 'ExitStandby')
PutLifecycleHook = Action(prefix, 'PutLifecycleHook')
PutNotificationConfiguration = \
    Action(prefix, 'PutNotificationConfiguration')
PutScalingPolicy = Action(prefix, 'PutScalingPolicy')
PutScheduledUpdateGroupAction = \
    Action(prefix, 'PutScheduledUpdateGroupAction')
RecordLifecycleActionHeartbeat = \
    Action(prefix, 'RecordLifecycleActionHeartbeat')
ResumeProcesses = Action(prefix, 'ResumeProcesses')
SetDesiredCapacity = Action(prefix, 'SetDesiredCapacity')
SetInstanceHealth = Action(prefix, 'SetInstanceHealth')
SuspendProcesses = Action(prefix, 'SuspendProcesses')
TerminateInstanceInAutoScalingGroup = \
    Action(prefix, 'TerminateInstanceInAutoScalingGroup')
UpdateAutoScalingGroup = Action(prefix, 'UpdateAutoScalingGroup')
