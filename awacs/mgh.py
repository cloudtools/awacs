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


AssociateCreatedArtifact = Action("AssociateCreatedArtifact")
AssociateDiscoveredResource = Action("AssociateDiscoveredResource")
CreateHomeRegionControl = Action("CreateHomeRegionControl")
CreateProgressUpdateStream = Action("CreateProgressUpdateStream")
DeleteHomeRegionControl = Action("DeleteHomeRegionControl")
DeleteProgressUpdateStream = Action("DeleteProgressUpdateStream")
DescribeApplicationState = Action("DescribeApplicationState")
DescribeHomeRegionControls = Action("DescribeHomeRegionControls")
DescribeMigrationTask = Action("DescribeMigrationTask")
DisassociateCreatedArtifact = Action("DisassociateCreatedArtifact")
DisassociateDiscoveredResource = Action("DisassociateDiscoveredResource")
GetHomeRegion = Action("GetHomeRegion")
ImportMigrationTask = Action("ImportMigrationTask")
ListApplicationStates = Action("ListApplicationStates")
ListCreatedArtifacts = Action("ListCreatedArtifacts")
ListDiscoveredResources = Action("ListDiscoveredResources")
ListMigrationTasks = Action("ListMigrationTasks")
ListProgressUpdateStreams = Action("ListProgressUpdateStreams")
NotifyApplicationState = Action("NotifyApplicationState")
NotifyMigrationTaskState = Action("NotifyMigrationTaskState")
PutResourceAttributes = Action("PutResourceAttributes")
