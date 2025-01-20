# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Application Auto Scaling"
prefix = "application-autoscaling"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeleteScalingPolicy = Action("DeleteScalingPolicy")
DeleteScheduledAction = Action("DeleteScheduledAction")
DeregisterScalableTarget = Action("DeregisterScalableTarget")
DescribeScalableTargets = Action("DescribeScalableTargets")
DescribeScalingActivities = Action("DescribeScalingActivities")
DescribeScalingPolicies = Action("DescribeScalingPolicies")
DescribeScheduledActions = Action("DescribeScheduledActions")
GetPredictiveScalingForecast = Action("GetPredictiveScalingForecast")
ListTagsForResource = Action("ListTagsForResource")
PutScalingPolicy = Action("PutScalingPolicy")
PutScheduledAction = Action("PutScheduledAction")
RegisterScalableTarget = Action("RegisterScalableTarget")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
