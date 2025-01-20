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
BatchGetSchemaAnalysisRule = Action("BatchGetSchemaAnalysisRule")
CreateAnalysisTemplate = Action("CreateAnalysisTemplate")
CreateCollaboration = Action("CreateCollaboration")
CreateConfiguredAudienceModelAssociation = Action(
    "CreateConfiguredAudienceModelAssociation"
)
CreateConfiguredTable = Action("CreateConfiguredTable")
CreateConfiguredTableAnalysisRule = Action("CreateConfiguredTableAnalysisRule")
CreateConfiguredTableAssociation = Action("CreateConfiguredTableAssociation")
CreateConfiguredTableAssociationAnalysisRule = Action(
    "CreateConfiguredTableAssociationAnalysisRule"
)
CreateIdMappingTable = Action("CreateIdMappingTable")
CreateIdNamespaceAssociation = Action("CreateIdNamespaceAssociation")
CreateMembership = Action("CreateMembership")
CreatePrivacyBudgetTemplate = Action("CreatePrivacyBudgetTemplate")
DeleteAnalysisTemplate = Action("DeleteAnalysisTemplate")
DeleteCollaboration = Action("DeleteCollaboration")
DeleteConfiguredAudienceModelAssociation = Action(
    "DeleteConfiguredAudienceModelAssociation"
)
DeleteConfiguredTable = Action("DeleteConfiguredTable")
DeleteConfiguredTableAnalysisRule = Action("DeleteConfiguredTableAnalysisRule")
DeleteConfiguredTableAssociation = Action("DeleteConfiguredTableAssociation")
DeleteConfiguredTableAssociationAnalysisRule = Action(
    "DeleteConfiguredTableAssociationAnalysisRule"
)
DeleteIdMappingTable = Action("DeleteIdMappingTable")
DeleteIdNamespaceAssociation = Action("DeleteIdNamespaceAssociation")
DeleteMember = Action("DeleteMember")
DeleteMembership = Action("DeleteMembership")
DeletePrivacyBudgetTemplate = Action("DeletePrivacyBudgetTemplate")
GetAnalysisTemplate = Action("GetAnalysisTemplate")
GetCollaboration = Action("GetCollaboration")
GetCollaborationAnalysisTemplate = Action("GetCollaborationAnalysisTemplate")
GetCollaborationConfiguredAudienceModelAssociation = Action(
    "GetCollaborationConfiguredAudienceModelAssociation"
)
GetCollaborationIdNamespaceAssociation = Action(
    "GetCollaborationIdNamespaceAssociation"
)
GetCollaborationPrivacyBudgetTemplate = Action("GetCollaborationPrivacyBudgetTemplate")
GetConfiguredAudienceModelAssociation = Action("GetConfiguredAudienceModelAssociation")
GetConfiguredTable = Action("GetConfiguredTable")
GetConfiguredTableAnalysisRule = Action("GetConfiguredTableAnalysisRule")
GetConfiguredTableAssociation = Action("GetConfiguredTableAssociation")
GetConfiguredTableAssociationAnalysisRule = Action(
    "GetConfiguredTableAssociationAnalysisRule"
)
GetIdMappingTable = Action("GetIdMappingTable")
GetIdNamespaceAssociation = Action("GetIdNamespaceAssociation")
GetMembership = Action("GetMembership")
GetPrivacyBudgetTemplate = Action("GetPrivacyBudgetTemplate")
GetProtectedQuery = Action("GetProtectedQuery")
GetSchema = Action("GetSchema")
GetSchemaAnalysisRule = Action("GetSchemaAnalysisRule")
ListAnalysisTemplates = Action("ListAnalysisTemplates")
ListCollaborationAnalysisTemplates = Action("ListCollaborationAnalysisTemplates")
ListCollaborationConfiguredAudienceModelAssociations = Action(
    "ListCollaborationConfiguredAudienceModelAssociations"
)
ListCollaborationIdNamespaceAssociations = Action(
    "ListCollaborationIdNamespaceAssociations"
)
ListCollaborationPrivacyBudgetTemplates = Action(
    "ListCollaborationPrivacyBudgetTemplates"
)
ListCollaborationPrivacyBudgets = Action("ListCollaborationPrivacyBudgets")
ListCollaborations = Action("ListCollaborations")
ListConfiguredAudienceModelAssociations = Action(
    "ListConfiguredAudienceModelAssociations"
)
ListConfiguredTableAssociations = Action("ListConfiguredTableAssociations")
ListConfiguredTables = Action("ListConfiguredTables")
ListIdMappingTables = Action("ListIdMappingTables")
ListIdNamespaceAssociations = Action("ListIdNamespaceAssociations")
ListMembers = Action("ListMembers")
ListMemberships = Action("ListMemberships")
ListPrivacyBudgetTemplates = Action("ListPrivacyBudgetTemplates")
ListPrivacyBudgets = Action("ListPrivacyBudgets")
ListProtectedQueries = Action("ListProtectedQueries")
ListSchemas = Action("ListSchemas")
ListTagsForResource = Action("ListTagsForResource")
PassCollaboration = Action("PassCollaboration")
PassMembership = Action("PassMembership")
PopulateIdMappingTable = Action("PopulateIdMappingTable")
PreviewPrivacyImpact = Action("PreviewPrivacyImpact")
StartProtectedQuery = Action("StartProtectedQuery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnalysisTemplate = Action("UpdateAnalysisTemplate")
UpdateCollaboration = Action("UpdateCollaboration")
UpdateConfiguredAudienceModelAssociation = Action(
    "UpdateConfiguredAudienceModelAssociation"
)
UpdateConfiguredTable = Action("UpdateConfiguredTable")
UpdateConfiguredTableAnalysisRule = Action("UpdateConfiguredTableAnalysisRule")
UpdateConfiguredTableAssociation = Action("UpdateConfiguredTableAssociation")
UpdateConfiguredTableAssociationAnalysisRule = Action(
    "UpdateConfiguredTableAssociationAnalysisRule"
)
UpdateIdMappingTable = Action("UpdateIdMappingTable")
UpdateIdNamespaceAssociation = Action("UpdateIdNamespaceAssociation")
UpdateMembership = Action("UpdateMembership")
UpdatePrivacyBudgetTemplate = Action("UpdatePrivacyBudgetTemplate")
UpdateProtectedQuery = Action("UpdateProtectedQuery")
