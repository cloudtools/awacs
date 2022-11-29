# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT RoboRunner"
prefix = "iotroborunner"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAction = Action("CreateAction")
CreateActionTemplate = Action("CreateActionTemplate")
CreateActionTemplateDependency = Action("CreateActionTemplateDependency")
CreateActivity = Action("CreateActivity")
CreateActivityDependency = Action("CreateActivityDependency")
CreateDestination = Action("CreateDestination")
CreateDestinationRelationship = Action("CreateDestinationRelationship")
CreateSite = Action("CreateSite")
CreateTask = Action("CreateTask")
CreateTaskDependency = Action("CreateTaskDependency")
CreateWorker = Action("CreateWorker")
CreateWorkerFleet = Action("CreateWorkerFleet")
DeleteAction = Action("DeleteAction")
DeleteActionTemplate = Action("DeleteActionTemplate")
DeleteActionTemplateDependency = Action("DeleteActionTemplateDependency")
DeleteActivity = Action("DeleteActivity")
DeleteActivityDependency = Action("DeleteActivityDependency")
DeleteDestination = Action("DeleteDestination")
DeleteDestinationRelationship = Action("DeleteDestinationRelationship")
DeleteSite = Action("DeleteSite")
DeleteTask = Action("DeleteTask")
DeleteTaskDependency = Action("DeleteTaskDependency")
DeleteWorker = Action("DeleteWorker")
DeleteWorkerFleet = Action("DeleteWorkerFleet")
GetAction = Action("GetAction")
GetActionTemplate = Action("GetActionTemplate")
GetActivity = Action("GetActivity")
GetDestination = Action("GetDestination")
GetDestinationRelationship = Action("GetDestinationRelationship")
GetSite = Action("GetSite")
GetTask = Action("GetTask")
GetWorker = Action("GetWorker")
GetWorkerFleet = Action("GetWorkerFleet")
ListActionTemplates = Action("ListActionTemplates")
ListActions = Action("ListActions")
ListActivities = Action("ListActivities")
ListDestinationRelationships = Action("ListDestinationRelationships")
ListDestinations = Action("ListDestinations")
ListSites = Action("ListSites")
ListTasks = Action("ListTasks")
ListWorkerFleets = Action("ListWorkerFleets")
ListWorkers = Action("ListWorkers")
UpdateActionState = Action("UpdateActionState")
UpdateActivity = Action("UpdateActivity")
UpdateDestination = Action("UpdateDestination")
UpdateSite = Action("UpdateSite")
UpdateTask = Action("UpdateTask")
UpdateWorker = Action("UpdateWorker")
UpdateWorkerFleet = Action("UpdateWorkerFleet")
