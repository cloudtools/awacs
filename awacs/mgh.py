# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Migration Hub"
prefix = "mgh"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptConnection = Action("AcceptConnection")
AssociateAutomationUnitRole = Action("AssociateAutomationUnitRole")
AssociateCreatedArtifact = Action("AssociateCreatedArtifact")
AssociateDiscoveredResource = Action("AssociateDiscoveredResource")
AssociateSourceResource = Action("AssociateSourceResource")
BatchAssociateIamRoleWithConnection = Action("BatchAssociateIamRoleWithConnection")
BatchDisassociateIamRoleFromConnection = Action(
    "BatchDisassociateIamRoleFromConnection"
)
CreateAutomationRun = Action("CreateAutomationRun")
CreateAutomationUnit = Action("CreateAutomationUnit")
CreateHomeRegionControl = Action("CreateHomeRegionControl")
CreateProgressUpdateStream = Action("CreateProgressUpdateStream")
DeleteAutomationRun = Action("DeleteAutomationRun")
DeleteAutomationUnit = Action("DeleteAutomationUnit")
DeleteConnection = Action("DeleteConnection")
DeleteHomeRegionControl = Action("DeleteHomeRegionControl")
DeleteProgressUpdateStream = Action("DeleteProgressUpdateStream")
DescribeApplicationState = Action("DescribeApplicationState")
DescribeAutomationRun = Action("DescribeAutomationRun")
DescribeAutomationUnit = Action("DescribeAutomationUnit")
DescribeHomeRegionControls = Action("DescribeHomeRegionControls")
DescribeMigrationTask = Action("DescribeMigrationTask")
DisassociateAutomationUnitRole = Action("DisassociateAutomationUnitRole")
DisassociateCreatedArtifact = Action("DisassociateCreatedArtifact")
DisassociateDiscoveredResource = Action("DisassociateDiscoveredResource")
DisassociateSourceResource = Action("DisassociateSourceResource")
GetConnection = Action("GetConnection")
GetHomeRegion = Action("GetHomeRegion")
ImportMigrationTask = Action("ImportMigrationTask")
ListApplicationStates = Action("ListApplicationStates")
ListAutomationRuns = Action("ListAutomationRuns")
ListAutomationUnits = Action("ListAutomationUnits")
ListConnectionRoles = Action("ListConnectionRoles")
ListConnections = Action("ListConnections")
ListCreatedArtifacts = Action("ListCreatedArtifacts")
ListDiscoveredResources = Action("ListDiscoveredResources")
ListMigrationTaskUpdates = Action("ListMigrationTaskUpdates")
ListMigrationTasks = Action("ListMigrationTasks")
ListProgressUpdateStreams = Action("ListProgressUpdateStreams")
ListSourceResources = Action("ListSourceResources")
ListTagsForResource = Action("ListTagsForResource")
NotifyApplicationState = Action("NotifyApplicationState")
NotifyMigrationTaskState = Action("NotifyMigrationTaskState")
PutResourceAttributes = Action("PutResourceAttributes")
RejectConnection = Action("RejectConnection")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
