# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Evidently"
prefix = "evidently"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchEvaluateFeature = Action("BatchEvaluateFeature")
CreateExperiment = Action("CreateExperiment")
CreateFeature = Action("CreateFeature")
CreateLaunch = Action("CreateLaunch")
CreateProject = Action("CreateProject")
CreateSegment = Action("CreateSegment")
DeleteExperiment = Action("DeleteExperiment")
DeleteFeature = Action("DeleteFeature")
DeleteLaunch = Action("DeleteLaunch")
DeleteProject = Action("DeleteProject")
DeleteSegment = Action("DeleteSegment")
EvaluateFeature = Action("EvaluateFeature")
GetExperiment = Action("GetExperiment")
GetExperimentResults = Action("GetExperimentResults")
GetFeature = Action("GetFeature")
GetLaunch = Action("GetLaunch")
GetProject = Action("GetProject")
GetSegment = Action("GetSegment")
ListExperiments = Action("ListExperiments")
ListFeatures = Action("ListFeatures")
ListLaunches = Action("ListLaunches")
ListProjects = Action("ListProjects")
ListSegmentReferences = Action("ListSegmentReferences")
ListSegments = Action("ListSegments")
ListTagsForResource = Action("ListTagsForResource")
PutProjectEvents = Action("PutProjectEvents")
StartExperiment = Action("StartExperiment")
StartLaunch = Action("StartLaunch")
StopExperiment = Action("StopExperiment")
StopLaunch = Action("StopLaunch")
TagResource = Action("TagResource")
TestSegmentPattern = Action("TestSegmentPattern")
UntagResource = Action("UntagResource")
UpdateExperiment = Action("UpdateExperiment")
UpdateFeature = Action("UpdateFeature")
UpdateLaunch = Action("UpdateLaunch")
UpdateProject = Action("UpdateProject")
UpdateProjectDataDelivery = Action("UpdateProjectDataDelivery")
