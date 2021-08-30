# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EC2 Auto Scaling"
prefix = "autoscaling"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AttachInstances = Action("AttachInstances")
AttachLoadBalancerTargetGroups = Action("AttachLoadBalancerTargetGroups")
AttachLoadBalancers = Action("AttachLoadBalancers")
BatchDeleteScheduledAction = Action("BatchDeleteScheduledAction")
BatchPutScheduledUpdateGroupAction = Action("BatchPutScheduledUpdateGroupAction")
CancelInstanceRefresh = Action("CancelInstanceRefresh")
CompleteLifecycleAction = Action("CompleteLifecycleAction")
CreateAutoScalingGroup = Action("CreateAutoScalingGroup")
CreateLaunchConfiguration = Action("CreateLaunchConfiguration")
CreateOrUpdateTags = Action("CreateOrUpdateTags")
DeleteAutoScalingGroup = Action("DeleteAutoScalingGroup")
DeleteLaunchConfiguration = Action("DeleteLaunchConfiguration")
DeleteLifecycleHook = Action("DeleteLifecycleHook")
DeleteNotificationConfiguration = Action("DeleteNotificationConfiguration")
DeletePolicy = Action("DeletePolicy")
DeleteScheduledAction = Action("DeleteScheduledAction")
DeleteTags = Action("DeleteTags")
DeleteWarmPool = Action("DeleteWarmPool")
DescribeAccountLimits = Action("DescribeAccountLimits")
DescribeAdjustmentTypes = Action("DescribeAdjustmentTypes")
DescribeAutoScalingGroups = Action("DescribeAutoScalingGroups")
DescribeAutoScalingInstances = Action("DescribeAutoScalingInstances")
DescribeAutoScalingNotificationTypes = Action("DescribeAutoScalingNotificationTypes")
DescribeInstanceRefreshes = Action("DescribeInstanceRefreshes")
DescribeLaunchConfigurations = Action("DescribeLaunchConfigurations")
DescribeLifecycleHookTypes = Action("DescribeLifecycleHookTypes")
DescribeLifecycleHooks = Action("DescribeLifecycleHooks")
DescribeLoadBalancerTargetGroups = Action("DescribeLoadBalancerTargetGroups")
DescribeLoadBalancers = Action("DescribeLoadBalancers")
DescribeMetricCollectionTypes = Action("DescribeMetricCollectionTypes")
DescribeNotificationConfigurations = Action("DescribeNotificationConfigurations")
DescribePolicies = Action("DescribePolicies")
DescribeScalingActivities = Action("DescribeScalingActivities")
DescribeScalingProcessTypes = Action("DescribeScalingProcessTypes")
DescribeScheduledActions = Action("DescribeScheduledActions")
DescribeTags = Action("DescribeTags")
DescribeTerminationPolicyTypes = Action("DescribeTerminationPolicyTypes")
DescribeWarmPool = Action("DescribeWarmPool")
DetachInstances = Action("DetachInstances")
DetachLoadBalancerTargetGroups = Action("DetachLoadBalancerTargetGroups")
DetachLoadBalancers = Action("DetachLoadBalancers")
DisableMetricsCollection = Action("DisableMetricsCollection")
EnableMetricsCollection = Action("EnableMetricsCollection")
EnterStandby = Action("EnterStandby")
ExecutePolicy = Action("ExecutePolicy")
ExitStandby = Action("ExitStandby")
GetPredictiveScalingForecast = Action("GetPredictiveScalingForecast")
PutLifecycleHook = Action("PutLifecycleHook")
PutNotificationConfiguration = Action("PutNotificationConfiguration")
PutScalingPolicy = Action("PutScalingPolicy")
PutScheduledUpdateGroupAction = Action("PutScheduledUpdateGroupAction")
PutWarmPool = Action("PutWarmPool")
RecordLifecycleActionHeartbeat = Action("RecordLifecycleActionHeartbeat")
ResumeProcesses = Action("ResumeProcesses")
SetDesiredCapacity = Action("SetDesiredCapacity")
SetInstanceHealth = Action("SetInstanceHealth")
SetInstanceProtection = Action("SetInstanceProtection")
StartInstanceRefresh = Action("StartInstanceRefresh")
SuspendProcesses = Action("SuspendProcesses")
TerminateInstanceInAutoScalingGroup = Action("TerminateInstanceInAutoScalingGroup")
UpdateAutoScalingGroup = Action("UpdateAutoScalingGroup")
