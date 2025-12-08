# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DevOps Agent Service"
prefix = "aidevops"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateService = Action("AssociateService")
CreateAgentSpace = Action("CreateAgentSpace")
CreateBacklogTask = Action("CreateBacklogTask")
CreateKnowledgeItem = Action("CreateKnowledgeItem")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
DeleteAgentSpace = Action("DeleteAgentSpace")
DeleteKnowledgeItem = Action("DeleteKnowledgeItem")
DeregisterService = Action("DeregisterService")
DescribeSupportLevel = Action("DescribeSupportLevel")
DisableOperatorApp = Action("DisableOperatorApp")
DisassociateService = Action("DisassociateService")
DiscoverTopology = Action("DiscoverTopology")
EnableOperatorApp = Action("EnableOperatorApp")
EndChatForCase = Action("EndChatForCase")
GetAccountUsage = Action("GetAccountUsage")
GetAgentSpace = Action("GetAgentSpace")
GetAssociation = Action("GetAssociation")
GetBacklogTask = Action("GetBacklogTask")
GetKnowledgeItem = Action("GetKnowledgeItem")
GetOperatorAppTeams = Action("GetOperatorAppTeams")
GetRecommendation = Action("GetRecommendation")
GetService = Action("GetService")
HandleServiceRegistrationCallback = Action("HandleServiceRegistrationCallback")
InitiateChatForCase = Action("InitiateChatForCase")
InitiateServiceRegistration = Action("InitiateServiceRegistration")
InvokeAgent = Action("InvokeAgent")
ListAgentSpaces = Action("ListAgentSpaces")
ListAssociations = Action("ListAssociations")
ListBacklogTasks = Action("ListBacklogTasks")
ListExecutions = Action("ListExecutions")
ListGoals = Action("ListGoals")
ListJournalRecords = Action("ListJournalRecords")
ListKnowledgeItems = Action("ListKnowledgeItems")
ListPendingMessages = Action("ListPendingMessages")
ListRecommendations = Action("ListRecommendations")
ListServices = Action("ListServices")
ListWebhooks = Action("ListWebhooks")
RegisterService = Action("RegisterService")
SearchServiceAccessibleResource = Action("SearchServiceAccessibleResource")
SendChatMessage = Action("SendChatMessage")
UpdateAgentSpace = Action("UpdateAgentSpace")
UpdateAssociation = Action("UpdateAssociation")
UpdateBacklogTask = Action("UpdateBacklogTask")
UpdateKnowledgeItem = Action("UpdateKnowledgeItem")
UpdateOperatorAppTeams = Action("UpdateOperatorAppTeams")
UpdateRecommendation = Action("UpdateRecommendation")
