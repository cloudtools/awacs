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


CreateAssignment = Action("CreateAssignment")
CreatePlugin = Action("CreatePlugin")
DeleteAssignment = Action("DeleteAssignment")
DeletePlugin = Action("DeletePlugin")
GenerateCodeFromCommands = Action("GenerateCodeFromCommands")
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
SendMessage = Action("SendMessage")
StartConversation = Action("StartConversation")
StartTroubleshootingAnalysis = Action("StartTroubleshootingAnalysis")
StartTroubleshootingResolutionExplanation = Action(
    "StartTroubleshootingResolutionExplanation"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTroubleshootingCommandResult = Action("UpdateTroubleshootingCommandResult")
UsePlugin = Action("UsePlugin")
