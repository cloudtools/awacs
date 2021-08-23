# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Database Migration Service"
prefix = "dms"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToResource = Action("AddTagsToResource")
ApplyPendingMaintenanceAction = Action("ApplyPendingMaintenanceAction")
CancelReplicationTaskAssessmentRun = Action("CancelReplicationTaskAssessmentRun")
CreateEndpoint = Action("CreateEndpoint")
CreateEventSubscription = Action("CreateEventSubscription")
CreateReplicationInstance = Action("CreateReplicationInstance")
CreateReplicationSubnetGroup = Action("CreateReplicationSubnetGroup")
CreateReplicationTask = Action("CreateReplicationTask")
DeleteCertificate = Action("DeleteCertificate")
DeleteConnection = Action("DeleteConnection")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEventSubscription = Action("DeleteEventSubscription")
DeleteReplicationInstance = Action("DeleteReplicationInstance")
DeleteReplicationSubnetGroup = Action("DeleteReplicationSubnetGroup")
DeleteReplicationTask = Action("DeleteReplicationTask")
DeleteReplicationTaskAssessmentRun = Action("DeleteReplicationTaskAssessmentRun")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeApplicableIndividualAssessments = Action(
    "DescribeApplicableIndividualAssessments"
)
DescribeCertificates = Action("DescribeCertificates")
DescribeConnections = Action("DescribeConnections")
DescribeEndpointSettings = Action("DescribeEndpointSettings")
DescribeEndpointTypes = Action("DescribeEndpointTypes")
DescribeEndpoints = Action("DescribeEndpoints")
DescribeEventCategories = Action("DescribeEventCategories")
DescribeEventSubscriptions = Action("DescribeEventSubscriptions")
DescribeEvents = Action("DescribeEvents")
DescribeOrderableReplicationInstances = Action("DescribeOrderableReplicationInstances")
DescribeRefreshSchemasStatus = Action("DescribeRefreshSchemasStatus")
DescribeReplicationInstanceTaskLogs = Action("DescribeReplicationInstanceTaskLogs")
DescribeReplicationInstances = Action("DescribeReplicationInstances")
DescribeReplicationSubnetGroups = Action("DescribeReplicationSubnetGroups")
DescribeReplicationTaskAssessmentResults = Action(
    "DescribeReplicationTaskAssessmentResults"
)
DescribeReplicationTaskAssessmentRuns = Action("DescribeReplicationTaskAssessmentRuns")
DescribeReplicationTaskIndividualAssessments = Action(
    "DescribeReplicationTaskIndividualAssessments"
)
DescribeReplicationTasks = Action("DescribeReplicationTasks")
DescribeSchemas = Action("DescribeSchemas")
DescribeTableStatistics = Action("DescribeTableStatistics")
ImportCertificate = Action("ImportCertificate")
ListTagsForResource = Action("ListTagsForResource")
ModifyEndpoint = Action("ModifyEndpoint")
ModifyEventSubscription = Action("ModifyEventSubscription")
ModifyReplicationInstance = Action("ModifyReplicationInstance")
ModifyReplicationSubnetGroup = Action("ModifyReplicationSubnetGroup")
ModifyReplicationTask = Action("ModifyReplicationTask")
MoveReplicationTask = Action("MoveReplicationTask")
RebootReplicationInstance = Action("RebootReplicationInstance")
RefreshSchemas = Action("RefreshSchemas")
ReloadTables = Action("ReloadTables")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
StartReplicationTask = Action("StartReplicationTask")
StartReplicationTaskAssessment = Action("StartReplicationTaskAssessment")
StartReplicationTaskAssessmentRun = Action("StartReplicationTaskAssessmentRun")
StopReplicationTask = Action("StopReplicationTask")
TestConnection = Action("TestConnection")
