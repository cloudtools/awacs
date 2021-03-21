# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Fault Injection Simulator"
prefix = "fis"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateExperimentTemplate = Action("CreateExperimentTemplate")
DeleteExperimentTemplate = Action("DeleteExperimentTemplate")
GetAction = Action("GetAction")
GetExperiment = Action("GetExperiment")
GetExperimentTemplate = Action("GetExperimentTemplate")
InjectApiInternalError = Action("InjectApiInternalError")
InjectApiThrottleError = Action("InjectApiThrottleError")
InjectApiUnavailableError = Action("InjectApiUnavailableError")
ListActions = Action("ListActions")
ListExperimentTemplates = Action("ListExperimentTemplates")
ListExperiments = Action("ListExperiments")
ListTagsForResource = Action("ListTagsForResource")
StartExperiment = Action("StartExperiment")
StopExperiment = Action("StopExperiment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateExperimentTemplate = Action("UpdateExperimentTemplate")
