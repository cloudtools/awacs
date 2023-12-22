# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Application Transformation Service"
prefix = "application-transformation"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetContainerization = Action("GetContainerization")
GetDeployment = Action("GetDeployment")
GetGroupingAssessment = Action("GetGroupingAssessment")
GetPortingCompatibilityAssessment = Action("GetPortingCompatibilityAssessment")
GetPortingRecommendationAssessment = Action("GetPortingRecommendationAssessment")
GetRuntimeAssessment = Action("GetRuntimeAssessment")
PutLogData = Action("PutLogData")
PutMetricData = Action("PutMetricData")
StartContainerization = Action("StartContainerization")
StartDeployment = Action("StartDeployment")
StartGroupingAssessment = Action("StartGroupingAssessment")
StartPortingCompatibilityAssessment = Action("StartPortingCompatibilityAssessment")
StartPortingRecommendationAssessment = Action("StartPortingRecommendationAssessment")
StartRuntimeAssessment = Action("StartRuntimeAssessment")
