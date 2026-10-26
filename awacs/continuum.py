# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Continuum"
prefix = "continuum"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateCollector = Action("AssociateCollector")
CreateCodeFinding = Action("CreateCodeFinding")
CreateCodeScan = Action("CreateCodeScan")
CreateCollector = Action("CreateCollector")
CreateEnvironment = Action("CreateEnvironment")
CreateIntegration = Action("CreateIntegration")
DeleteCollector = Action("DeleteCollector")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteIntegration = Action("DeleteIntegration")
DisassociateCollector = Action("DisassociateCollector")
GetCodeFinding = Action("GetCodeFinding")
GetCodeIssue = Action("GetCodeIssue")
GetCodeIssueArtifact = Action("GetCodeIssueArtifact")
GetCodeScan = Action("GetCodeScan")
GetCollector = Action("GetCollector")
GetCollectorDataAccessAuthorization = Action("GetCollectorDataAccessAuthorization")
GetEnvironment = Action("GetEnvironment")
GetIntegration = Action("GetIntegration")
GetResourcePolicy = Action("GetResourcePolicy")
ListAssociatedCollectors = Action("ListAssociatedCollectors")
ListAssociatedEnvironments = Action("ListAssociatedEnvironments")
ListCodeFindings = Action("ListCodeFindings")
ListCodeIssueArtifacts = Action("ListCodeIssueArtifacts")
ListCodeIssues = Action("ListCodeIssues")
ListCodeScans = Action("ListCodeScans")
ListCollectors = Action("ListCollectors")
ListEnvironments = Action("ListEnvironments")
ListIntegrations = Action("ListIntegrations")
PutResourcePolicy = Action("PutResourcePolicy")
StartIntegrationAuthorization = Action("StartIntegrationAuthorization")
UpdateCollector = Action("UpdateCollector")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateIntegration = Action("UpdateIntegration")
