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
CreateAssignment = Action("CreateAssignment")
CreateAuthGrant = Action("CreateAuthGrant")
CreateOAuthAppConnection = Action("CreateOAuthAppConnection")
CreatePlugin = Action("CreatePlugin")
DeleteAssignment = Action("DeleteAssignment")
DeleteConversation = Action("DeleteConversation")
DeleteOAuthAppConnection = Action("DeleteOAuthAppConnection")
DeletePlugin = Action("DeletePlugin")
GenerateCodeFromCommands = Action("GenerateCodeFromCommands")
GenerateCodeRecommendations = Action("GenerateCodeRecommendations")
GetConnector = Action("GetConnector")
GetConversation = Action("GetConversation")
GetIdentityMetadata = Action("GetIdentityMetadata")
GetPlugin = Action("GetPlugin")
GetTroubleshootingResults = Action("GetTroubleshootingResults")
ListConversations = Action("ListConversations")
ListDashboardMetrics = Action("ListDashboardMetrics")
ListPluginProviders = Action("ListPluginProviders")
ListPlugins = Action("ListPlugins")
ListTagsForResource = Action("ListTagsForResource")
PassRequest = Action("PassRequest")
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
UpdateAuthGrant = Action("UpdateAuthGrant")
UpdateConversation = Action("UpdateConversation")
UpdateOAuthAppConnection = Action("UpdateOAuthAppConnection")
UpdatePlugin = Action("UpdatePlugin")
UpdateTroubleshootingCommandResult = Action("UpdateTroubleshootingCommandResult")
UsePlugin = Action("UsePlugin")
VerifyOAuthAppConnection = Action("VerifyOAuthAppConnection")
