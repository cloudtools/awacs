# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Fault Injection Service"
prefix = "fis"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateExperimentTemplate = Action("CreateExperimentTemplate")
CreateTargetAccountConfiguration = Action("CreateTargetAccountConfiguration")
DeleteExperimentTemplate = Action("DeleteExperimentTemplate")
DeleteTargetAccountConfiguration = Action("DeleteTargetAccountConfiguration")
GetAction = Action("GetAction")
GetExperiment = Action("GetExperiment")
GetExperimentTargetAccountConfiguration = Action(
    "GetExperimentTargetAccountConfiguration"
)
GetExperimentTemplate = Action("GetExperimentTemplate")
GetSafetyLever = Action("GetSafetyLever")
GetTargetAccountConfiguration = Action("GetTargetAccountConfiguration")
GetTargetResourceType = Action("GetTargetResourceType")
InjectApiInternalError = Action("InjectApiInternalError")
InjectApiThrottleError = Action("InjectApiThrottleError")
InjectApiUnavailableError = Action("InjectApiUnavailableError")
ListActions = Action("ListActions")
ListExperimentResolvedTargets = Action("ListExperimentResolvedTargets")
ListExperimentTargetAccountConfigurations = Action(
    "ListExperimentTargetAccountConfigurations"
)
ListExperimentTemplates = Action("ListExperimentTemplates")
ListExperiments = Action("ListExperiments")
ListTagsForResource = Action("ListTagsForResource")
ListTargetAccountConfigurations = Action("ListTargetAccountConfigurations")
ListTargetResourceTypes = Action("ListTargetResourceTypes")
StartExperiment = Action("StartExperiment")
StopExperiment = Action("StopExperiment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateExperimentTemplate = Action("UpdateExperimentTemplate")
UpdateSafetyLeverState = Action("UpdateSafetyLeverState")
UpdateTargetAccountConfiguration = Action("UpdateTargetAccountConfiguration")
