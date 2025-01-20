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
BatchGetCalculatedAttributeForProfile = Action("BatchGetCalculatedAttributeForProfile")
BatchGetProfile = Action("BatchGetProfile")
CreateCalculatedAttributeDefinition = Action("CreateCalculatedAttributeDefinition")
CreateDomain = Action("CreateDomain")
CreateEventStream = Action("CreateEventStream")
CreateEventTrigger = Action("CreateEventTrigger")
CreateIntegrationWorkflow = Action("CreateIntegrationWorkflow")
CreateProfile = Action("CreateProfile")
CreateSegmentDefinition = Action("CreateSegmentDefinition")
CreateSegmentEstimate = Action("CreateSegmentEstimate")
CreateSegmentSnapshot = Action("CreateSegmentSnapshot")
CreateSnapshot = Action("CreateSnapshot")
DeleteCalculatedAttributeDefinition = Action("DeleteCalculatedAttributeDefinition")
DeleteDomain = Action("DeleteDomain")
DeleteEventStream = Action("DeleteEventStream")
DeleteEventTrigger = Action("DeleteEventTrigger")
DeleteIntegration = Action("DeleteIntegration")
DeleteProfile = Action("DeleteProfile")
DeleteProfileKey = Action("DeleteProfileKey")
DeleteProfileObject = Action("DeleteProfileObject")
DeleteProfileObjectType = Action("DeleteProfileObjectType")
DeleteSegmentDefinition = Action("DeleteSegmentDefinition")
DeleteWorkflow = Action("DeleteWorkflow")
DetectProfileObjectType = Action("DetectProfileObjectType")
GetAutoMergingPreview = Action("GetAutoMergingPreview")
GetCalculatedAttributeDefinition = Action("GetCalculatedAttributeDefinition")
GetCalculatedAttributeForProfile = Action("GetCalculatedAttributeForProfile")
GetDomain = Action("GetDomain")
GetEventStream = Action("GetEventStream")
GetEventTrigger = Action("GetEventTrigger")
GetIdentityResolutionJob = Action("GetIdentityResolutionJob")
GetIntegration = Action("GetIntegration")
GetMatches = Action("GetMatches")
GetProfileObjectType = Action("GetProfileObjectType")
GetProfileObjectTypeTemplate = Action("GetProfileObjectTypeTemplate")
GetSegmentDefinition = Action("GetSegmentDefinition")
GetSegmentEstimate = Action("GetSegmentEstimate")
GetSegmentMembership = Action("GetSegmentMembership")
GetSegmentSnapshot = Action("GetSegmentSnapshot")
GetSimilarProfiles = Action("GetSimilarProfiles")
GetSnapshot = Action("GetSnapshot")
GetWorkflow = Action("GetWorkflow")
GetWorkflowSteps = Action("GetWorkflowSteps")
ListAccountIntegrations = Action("ListAccountIntegrations")
ListCalculatedAttributeDefinitions = Action("ListCalculatedAttributeDefinitions")
ListCalculatedAttributesForProfile = Action("ListCalculatedAttributesForProfile")
ListDomains = Action("ListDomains")
ListEventStreams = Action("ListEventStreams")
ListEventTriggers = Action("ListEventTriggers")
ListIdentityResolutionJobs = Action("ListIdentityResolutionJobs")
ListIntegrations = Action("ListIntegrations")
ListObjectTypeAttributes = Action("ListObjectTypeAttributes")
ListProfileAttributeValues = Action("ListProfileAttributeValues")
ListProfileObjectTypeTemplates = Action("ListProfileObjectTypeTemplates")
ListProfileObjectTypes = Action("ListProfileObjectTypes")
ListProfileObjects = Action("ListProfileObjects")
ListRuleBasedMatches = Action("ListRuleBasedMatches")
ListSegmentDefinitions = Action("ListSegmentDefinitions")
ListTagsForResource = Action("ListTagsForResource")
ListWorkflows = Action("ListWorkflows")
MergeProfiles = Action("MergeProfiles")
PutIntegration = Action("PutIntegration")
PutProfileObject = Action("PutProfileObject")
PutProfileObjectType = Action("PutProfileObjectType")
SearchProfiles = Action("SearchProfiles")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCalculatedAttributeDefinition = Action("UpdateCalculatedAttributeDefinition")
UpdateDomain = Action("UpdateDomain")
UpdateEventTrigger = Action("UpdateEventTrigger")
UpdateProfile = Action("UpdateProfile")
