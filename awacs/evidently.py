# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Evidently"
prefix = "evidently"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateExperiment = Action("CreateExperiment")
CreateFeature = Action("CreateFeature")
CreateLaunch = Action("CreateLaunch")
CreateProject = Action("CreateProject")
DeleteExperiment = Action("DeleteExperiment")
DeleteFeature = Action("DeleteFeature")
DeleteLaunch = Action("DeleteLaunch")
DeleteProject = Action("DeleteProject")
GetExperiment = Action("GetExperiment")
GetExperimentResults = Action("GetExperimentResults")
GetFeature = Action("GetFeature")
GetLaunch = Action("GetLaunch")
GetProject = Action("GetProject")
ListExperiments = Action("ListExperiments")
ListFeatures = Action("ListFeatures")
ListLaunches = Action("ListLaunches")
ListProjects = Action("ListProjects")
StartExperiment = Action("StartExperiment")
StartLaunch = Action("StartLaunch")
StopExperiment = Action("StopExperiment")
StopLaunch = Action("StopLaunch")
UpdateExperiment = Action("UpdateExperiment")
UpdateFeature = Action("UpdateFeature")
UpdateLaunch = Action("UpdateLaunch")
UpdateProject = Action("UpdateProject")
UpdateProjectDataDelivery = Action("UpdateProjectDataDelivery")
