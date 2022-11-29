# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS RoboMaker"
prefix = "robomaker"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchDeleteWorlds = Action("BatchDeleteWorlds")
BatchDescribeSimulationJob = Action("BatchDescribeSimulationJob")
CancelDeploymentJob = Action("CancelDeploymentJob")
CancelSimulationJob = Action("CancelSimulationJob")
CancelSimulationJobBatch = Action("CancelSimulationJobBatch")
CancelWorldExportJob = Action("CancelWorldExportJob")
CancelWorldGenerationJob = Action("CancelWorldGenerationJob")
CreateDeploymentJob = Action("CreateDeploymentJob")
CreateFleet = Action("CreateFleet")
CreateRobot = Action("CreateRobot")
CreateRobotApplication = Action("CreateRobotApplication")
CreateRobotApplicationVersion = Action("CreateRobotApplicationVersion")
CreateSimulationApplication = Action("CreateSimulationApplication")
CreateSimulationApplicationVersion = Action("CreateSimulationApplicationVersion")
CreateSimulationJob = Action("CreateSimulationJob")
CreateWorldExportJob = Action("CreateWorldExportJob")
CreateWorldGenerationJob = Action("CreateWorldGenerationJob")
CreateWorldTemplate = Action("CreateWorldTemplate")
DeleteFleet = Action("DeleteFleet")
DeleteRobot = Action("DeleteRobot")
DeleteRobotApplication = Action("DeleteRobotApplication")
DeleteSimulationApplication = Action("DeleteSimulationApplication")
DeleteWorldTemplate = Action("DeleteWorldTemplate")
DeregisterRobot = Action("DeregisterRobot")
DescribeDeploymentJob = Action("DescribeDeploymentJob")
DescribeFleet = Action("DescribeFleet")
DescribeRobot = Action("DescribeRobot")
DescribeRobotApplication = Action("DescribeRobotApplication")
DescribeSimulationApplication = Action("DescribeSimulationApplication")
DescribeSimulationJob = Action("DescribeSimulationJob")
DescribeSimulationJobBatch = Action("DescribeSimulationJobBatch")
DescribeWorld = Action("DescribeWorld")
DescribeWorldExportJob = Action("DescribeWorldExportJob")
DescribeWorldGenerationJob = Action("DescribeWorldGenerationJob")
DescribeWorldTemplate = Action("DescribeWorldTemplate")
GetWorldTemplateBody = Action("GetWorldTemplateBody")
ListDeploymentJobs = Action("ListDeploymentJobs")
ListFleets = Action("ListFleets")
ListRobotApplications = Action("ListRobotApplications")
ListRobots = Action("ListRobots")
ListSimulationApplications = Action("ListSimulationApplications")
ListSimulationJobBatches = Action("ListSimulationJobBatches")
ListSimulationJobs = Action("ListSimulationJobs")
ListSupportedAvailabilityZones = Action("ListSupportedAvailabilityZones")
ListTagsForResource = Action("ListTagsForResource")
ListWorldExportJobs = Action("ListWorldExportJobs")
ListWorldGenerationJobs = Action("ListWorldGenerationJobs")
ListWorldTemplates = Action("ListWorldTemplates")
ListWorlds = Action("ListWorlds")
RegisterRobot = Action("RegisterRobot")
RestartSimulationJob = Action("RestartSimulationJob")
StartSimulationJobBatch = Action("StartSimulationJobBatch")
SyncDeploymentJob = Action("SyncDeploymentJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateRobotApplication = Action("UpdateRobotApplication")
UpdateRobotDeployment = Action("UpdateRobotDeployment")
UpdateSimulationApplication = Action("UpdateSimulationApplication")
UpdateWorldTemplate = Action("UpdateWorldTemplate")
