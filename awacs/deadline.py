# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Deadline Cloud"
prefix = "deadline"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateMemberToFarm = Action("AssociateMemberToFarm")
AssociateMemberToFleet = Action("AssociateMemberToFleet")
AssociateMemberToJob = Action("AssociateMemberToJob")
AssociateMemberToQueue = Action("AssociateMemberToQueue")
AssumeFleetRoleForRead = Action("AssumeFleetRoleForRead")
AssumeFleetRoleForWorker = Action("AssumeFleetRoleForWorker")
AssumeQueueRoleForRead = Action("AssumeQueueRoleForRead")
AssumeQueueRoleForUser = Action("AssumeQueueRoleForUser")
AssumeQueueRoleForWorker = Action("AssumeQueueRoleForWorker")
BatchGetJobEntity = Action("BatchGetJobEntity")
CopyJobTemplate = Action("CopyJobTemplate")
CreateBudget = Action("CreateBudget")
CreateFarm = Action("CreateFarm")
CreateFleet = Action("CreateFleet")
CreateJob = Action("CreateJob")
CreateLicenseEndpoint = Action("CreateLicenseEndpoint")
CreateMonitor = Action("CreateMonitor")
CreateQueue = Action("CreateQueue")
CreateQueueEnvironment = Action("CreateQueueEnvironment")
CreateQueueFleetAssociation = Action("CreateQueueFleetAssociation")
CreateStorageProfile = Action("CreateStorageProfile")
CreateWorker = Action("CreateWorker")
DeleteBudget = Action("DeleteBudget")
DeleteFarm = Action("DeleteFarm")
DeleteFleet = Action("DeleteFleet")
DeleteLicenseEndpoint = Action("DeleteLicenseEndpoint")
DeleteMeteredProduct = Action("DeleteMeteredProduct")
DeleteMonitor = Action("DeleteMonitor")
DeleteQueue = Action("DeleteQueue")
DeleteQueueEnvironment = Action("DeleteQueueEnvironment")
DeleteQueueFleetAssociation = Action("DeleteQueueFleetAssociation")
DeleteStorageProfile = Action("DeleteStorageProfile")
DeleteWorker = Action("DeleteWorker")
DisassociateMemberFromFarm = Action("DisassociateMemberFromFarm")
DisassociateMemberFromFleet = Action("DisassociateMemberFromFleet")
DisassociateMemberFromJob = Action("DisassociateMemberFromJob")
DisassociateMemberFromQueue = Action("DisassociateMemberFromQueue")
GetApplicationVersion = Action("GetApplicationVersion")
GetBudget = Action("GetBudget")
GetFarm = Action("GetFarm")
GetFleet = Action("GetFleet")
GetJob = Action("GetJob")
GetLicenseEndpoint = Action("GetLicenseEndpoint")
GetMonitor = Action("GetMonitor")
GetQueue = Action("GetQueue")
GetQueueEnvironment = Action("GetQueueEnvironment")
GetQueueFleetAssociation = Action("GetQueueFleetAssociation")
GetSession = Action("GetSession")
GetSessionAction = Action("GetSessionAction")
GetSessionsStatisticsAggregation = Action("GetSessionsStatisticsAggregation")
GetStep = Action("GetStep")
GetStorageProfile = Action("GetStorageProfile")
GetStorageProfileForQueue = Action("GetStorageProfileForQueue")
GetTask = Action("GetTask")
GetWorker = Action("GetWorker")
ListAvailableMeteredProducts = Action("ListAvailableMeteredProducts")
ListBudgets = Action("ListBudgets")
ListFarmMembers = Action("ListFarmMembers")
ListFarms = Action("ListFarms")
ListFleetMembers = Action("ListFleetMembers")
ListFleets = Action("ListFleets")
ListJobMembers = Action("ListJobMembers")
ListJobs = Action("ListJobs")
ListLicenseEndpoints = Action("ListLicenseEndpoints")
ListMeteredProducts = Action("ListMeteredProducts")
ListMonitors = Action("ListMonitors")
ListQueueEnvironments = Action("ListQueueEnvironments")
ListQueueFleetAssociations = Action("ListQueueFleetAssociations")
ListQueueMembers = Action("ListQueueMembers")
ListQueues = Action("ListQueues")
ListSessionActions = Action("ListSessionActions")
ListSessions = Action("ListSessions")
ListSessionsForWorker = Action("ListSessionsForWorker")
ListStepConsumers = Action("ListStepConsumers")
ListStepDependencies = Action("ListStepDependencies")
ListSteps = Action("ListSteps")
ListStorageProfiles = Action("ListStorageProfiles")
ListStorageProfilesForQueue = Action("ListStorageProfilesForQueue")
ListTagsForResource = Action("ListTagsForResource")
ListTasks = Action("ListTasks")
ListWorkers = Action("ListWorkers")
PutMeteredProduct = Action("PutMeteredProduct")
SearchJobs = Action("SearchJobs")
SearchSteps = Action("SearchSteps")
SearchTasks = Action("SearchTasks")
SearchWorkers = Action("SearchWorkers")
StartSessionsStatisticsAggregation = Action("StartSessionsStatisticsAggregation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBudget = Action("UpdateBudget")
UpdateFarm = Action("UpdateFarm")
UpdateFleet = Action("UpdateFleet")
UpdateJob = Action("UpdateJob")
UpdateMonitor = Action("UpdateMonitor")
UpdateQueue = Action("UpdateQueue")
UpdateQueueEnvironment = Action("UpdateQueueEnvironment")
UpdateQueueFleetAssociation = Action("UpdateQueueFleetAssociation")
UpdateSession = Action("UpdateSession")
UpdateStep = Action("UpdateStep")
UpdateStorageProfile = Action("UpdateStorageProfile")
UpdateTask = Action("UpdateTask")
UpdateWorker = Action("UpdateWorker")
UpdateWorkerSchedule = Action("UpdateWorkerSchedule")
