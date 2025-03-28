# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify"
prefix = "amplify"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateWebACL = Action("AssociateWebACL")
CreateApp = Action("CreateApp")
CreateBackendEnvironment = Action("CreateBackendEnvironment")
CreateBranch = Action("CreateBranch")
CreateDeployment = Action("CreateDeployment")
CreateDomainAssociation = Action("CreateDomainAssociation")
CreateWebHook = Action("CreateWebHook")
DeleteApp = Action("DeleteApp")
DeleteBackendEnvironment = Action("DeleteBackendEnvironment")
DeleteBranch = Action("DeleteBranch")
DeleteDomainAssociation = Action("DeleteDomainAssociation")
DeleteJob = Action("DeleteJob")
DeleteWebHook = Action("DeleteWebHook")
DisassociateWebACL = Action("DisassociateWebACL")
GenerateAccessLogs = Action("GenerateAccessLogs")
GetApp = Action("GetApp")
GetArtifactUrl = Action("GetArtifactUrl")
GetBackendEnvironment = Action("GetBackendEnvironment")
GetBranch = Action("GetBranch")
GetDomainAssociation = Action("GetDomainAssociation")
GetJob = Action("GetJob")
GetWebACLForResource = Action("GetWebACLForResource")
GetWebHook = Action("GetWebHook")
ListApps = Action("ListApps")
ListArtifacts = Action("ListArtifacts")
ListBackendEnvironments = Action("ListBackendEnvironments")
ListBranches = Action("ListBranches")
ListDomainAssociations = Action("ListDomainAssociations")
ListJobs = Action("ListJobs")
ListResourcesForWebACL = Action("ListResourcesForWebACL")
ListTagsForResource = Action("ListTagsForResource")
ListWebHooks = Action("ListWebHooks")
StartDeployment = Action("StartDeployment")
StartJob = Action("StartJob")
StopJob = Action("StopJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApp = Action("UpdateApp")
UpdateBranch = Action("UpdateBranch")
UpdateDomainAssociation = Action("UpdateDomainAssociation")
UpdateWebHook = Action("UpdateWebHook")
