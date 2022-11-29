# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Customer Profiles"
prefix = "profile"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddProfileKey = Action("AddProfileKey")
CreateDomain = Action("CreateDomain")
CreateIntegrationWorkflow = Action("CreateIntegrationWorkflow")
CreateProfile = Action("CreateProfile")
DeleteDomain = Action("DeleteDomain")
DeleteIntegration = Action("DeleteIntegration")
DeleteProfile = Action("DeleteProfile")
DeleteProfileKey = Action("DeleteProfileKey")
DeleteProfileObject = Action("DeleteProfileObject")
DeleteProfileObjectType = Action("DeleteProfileObjectType")
DeleteWorkflow = Action("DeleteWorkflow")
GetAutoMergingPreview = Action("GetAutoMergingPreview")
GetDomain = Action("GetDomain")
GetIdentityResolutionJob = Action("GetIdentityResolutionJob")
GetIntegration = Action("GetIntegration")
GetMatches = Action("GetMatches")
GetProfileObjectType = Action("GetProfileObjectType")
GetProfileObjectTypeTemplate = Action("GetProfileObjectTypeTemplate")
GetWorkflow = Action("GetWorkflow")
GetWorkflowSteps = Action("GetWorkflowSteps")
ListAccountIntegrations = Action("ListAccountIntegrations")
ListDomains = Action("ListDomains")
ListIdentityResolutionJobs = Action("ListIdentityResolutionJobs")
ListIntegrations = Action("ListIntegrations")
ListProfileObjectTypeTemplates = Action("ListProfileObjectTypeTemplates")
ListProfileObjectTypes = Action("ListProfileObjectTypes")
ListProfileObjects = Action("ListProfileObjects")
ListTagsForResource = Action("ListTagsForResource")
ListWorkflows = Action("ListWorkflows")
MergeProfiles = Action("MergeProfiles")
PutIntegration = Action("PutIntegration")
PutProfileObject = Action("PutProfileObject")
PutProfileObjectType = Action("PutProfileObjectType")
SearchProfiles = Action("SearchProfiles")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDomain = Action("UpdateDomain")
UpdateProfile = Action("UpdateProfile")
