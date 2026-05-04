# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Q"
prefix = "q"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConnectorResource = Action("AssociateConnectorResource")
AssociateLoginDomain = Action("AssociateLoginDomain")
BatchDescribeGroups = Action("BatchDescribeGroups")
BatchDescribeUsers = Action("BatchDescribeUsers")
BatchGetGroups = Action("BatchGetGroups")
BatchGetUsers = Action("BatchGetUsers")
CreateArtifact = Action("CreateArtifact")
CreateAssignment = Action("CreateAssignment")
CreateAuthGrant = Action("CreateAuthGrant")
CreateOAuthAppConnection = Action("CreateOAuthAppConnection")
CreatePlugin = Action("CreatePlugin")
CreateScimAccessToken = Action("CreateScimAccessToken")
DeleteAssignment = Action("DeleteAssignment")
DeleteConversation = Action("DeleteConversation")
DeleteOAuthAppConnection = Action("DeleteOAuthAppConnection")
DeletePlugin = Action("DeletePlugin")
DeleteScimAccessToken = Action("DeleteScimAccessToken")
DisassociateLoginDomain = Action("DisassociateLoginDomain")
GenerateCodeFromCommands = Action("GenerateCodeFromCommands")
GenerateCodeRecommendations = Action("GenerateCodeRecommendations")
GetArtifact = Action("GetArtifact")
GetArtifactActionResult = Action("GetArtifactActionResult")
GetConnector = Action("GetConnector")
GetConversation = Action("GetConversation")
GetIdentityMetadata = Action("GetIdentityMetadata")
GetPlugin = Action("GetPlugin")
GetTroubleshootingResults = Action("GetTroubleshootingResults")
ListConversations = Action("ListConversations")
ListDashboardMetrics = Action("ListDashboardMetrics")
ListGroups = Action("ListGroups")
ListLoginDomains = Action("ListLoginDomains")
ListPluginProviders = Action("ListPluginProviders")
ListPlugins = Action("ListPlugins")
ListScimAccessTokens = Action("ListScimAccessTokens")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
PassRequest = Action("PassRequest")
PerformArtifactAction = Action("PerformArtifactAction")
RejectConnector = Action("RejectConnector")
SendEvent = Action("SendEvent")
SendMessage = Action("SendMessage")
StartConversation = Action("StartConversation")
StartTroubleshootingAnalysis = Action("StartTroubleshootingAnalysis")
StartTroubleshootingResolutionExplanation = Action(
    "StartTroubleshootingResolutionExplanation"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAssignment = Action("UpdateAssignment")
UpdateAuthGrant = Action("UpdateAuthGrant")
UpdateConversation = Action("UpdateConversation")
UpdateOAuthAppConnection = Action("UpdateOAuthAppConnection")
UpdatePlugin = Action("UpdatePlugin")
UpdateTroubleshootingCommandResult = Action("UpdateTroubleshootingCommandResult")
UsePlugin = Action("UsePlugin")
VerifyOAuthAppConnection = Action("VerifyOAuthAppConnection")
