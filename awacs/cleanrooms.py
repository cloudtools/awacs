# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Clean Rooms"
prefix = "cleanrooms"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetCollaborationAnalysisTemplate = Action("BatchGetCollaborationAnalysisTemplate")
BatchGetSchema = Action("BatchGetSchema")
CreateAnalysisTemplate = Action("CreateAnalysisTemplate")
CreateCollaboration = Action("CreateCollaboration")
CreateConfiguredTable = Action("CreateConfiguredTable")
CreateConfiguredTableAnalysisRule = Action("CreateConfiguredTableAnalysisRule")
CreateConfiguredTableAssociation = Action("CreateConfiguredTableAssociation")
CreateMembership = Action("CreateMembership")
DeleteAnalysisTemplate = Action("DeleteAnalysisTemplate")
DeleteCollaboration = Action("DeleteCollaboration")
DeleteConfiguredTable = Action("DeleteConfiguredTable")
DeleteConfiguredTableAnalysisRule = Action("DeleteConfiguredTableAnalysisRule")
DeleteConfiguredTableAssociation = Action("DeleteConfiguredTableAssociation")
DeleteMember = Action("DeleteMember")
DeleteMembership = Action("DeleteMembership")
GetAnalysisTemplate = Action("GetAnalysisTemplate")
GetCollaboration = Action("GetCollaboration")
GetCollaborationAnalysisTemplate = Action("GetCollaborationAnalysisTemplate")
GetConfiguredTable = Action("GetConfiguredTable")
GetConfiguredTableAnalysisRule = Action("GetConfiguredTableAnalysisRule")
GetConfiguredTableAssociation = Action("GetConfiguredTableAssociation")
GetMembership = Action("GetMembership")
GetProtectedQuery = Action("GetProtectedQuery")
GetSchema = Action("GetSchema")
GetSchemaAnalysisRule = Action("GetSchemaAnalysisRule")
ListAnalysisTemplates = Action("ListAnalysisTemplates")
ListCollaborationAnalysisTemplates = Action("ListCollaborationAnalysisTemplates")
ListCollaborations = Action("ListCollaborations")
ListConfiguredTableAssociations = Action("ListConfiguredTableAssociations")
ListConfiguredTables = Action("ListConfiguredTables")
ListMembers = Action("ListMembers")
ListMemberships = Action("ListMemberships")
ListProtectedQueries = Action("ListProtectedQueries")
ListSchemas = Action("ListSchemas")
ListTagsForResource = Action("ListTagsForResource")
StartProtectedQuery = Action("StartProtectedQuery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnalysisTemplate = Action("UpdateAnalysisTemplate")
UpdateCollaboration = Action("UpdateCollaboration")
UpdateConfiguredTable = Action("UpdateConfiguredTable")
UpdateConfiguredTableAnalysisRule = Action("UpdateConfiguredTableAnalysisRule")
UpdateConfiguredTableAssociation = Action("UpdateConfiguredTableAssociation")
UpdateMembership = Action("UpdateMembership")
UpdateProtectedQuery = Action("UpdateProtectedQuery")
