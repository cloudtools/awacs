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


BatchGetSchema = Action("BatchGetSchema")
CreateCollaboration = Action("CreateCollaboration")
CreateConfiguredTable = Action("CreateConfiguredTable")
CreateConfiguredTableAnalysisRule = Action("CreateConfiguredTableAnalysisRule")
CreateConfiguredTableAssociation = Action("CreateConfiguredTableAssociation")
CreateMembership = Action("CreateMembership")
DeleteCollaboration = Action("DeleteCollaboration")
DeleteConfiguredTable = Action("DeleteConfiguredTable")
DeleteConfiguredTableAnalysisRule = Action("DeleteConfiguredTableAnalysisRule")
DeleteConfiguredTableAssociation = Action("DeleteConfiguredTableAssociation")
DeleteMember = Action("DeleteMember")
DeleteMembership = Action("DeleteMembership")
GetCollaboration = Action("GetCollaboration")
GetConfiguredTable = Action("GetConfiguredTable")
GetConfiguredTableAnalysisRule = Action("GetConfiguredTableAnalysisRule")
GetConfiguredTableAssociation = Action("GetConfiguredTableAssociation")
GetMembership = Action("GetMembership")
GetProtectedQuery = Action("GetProtectedQuery")
GetSchema = Action("GetSchema")
GetSchemaAnalysisRule = Action("GetSchemaAnalysisRule")
ListCollaborations = Action("ListCollaborations")
ListConfiguredTableAssociations = Action("ListConfiguredTableAssociations")
ListConfiguredTables = Action("ListConfiguredTables")
ListMembers = Action("ListMembers")
ListMemberships = Action("ListMemberships")
ListProtectedQueries = Action("ListProtectedQueries")
ListSchemas = Action("ListSchemas")
StartProtectedQuery = Action("StartProtectedQuery")
UpdateCollaboration = Action("UpdateCollaboration")
UpdateConfiguredTable = Action("UpdateConfiguredTable")
UpdateConfiguredTableAnalysisRule = Action("UpdateConfiguredTableAnalysisRule")
UpdateConfiguredTableAssociation = Action("UpdateConfiguredTableAssociation")
UpdateMembership = Action("UpdateMembership")
UpdateProtectedQuery = Action("UpdateProtectedQuery")
