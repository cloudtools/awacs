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


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
AssociateService = Action("AssociateService")
CreateAgentSpace = Action("CreateAgentSpace")
CreateBacklogTask = Action("CreateBacklogTask")
CreateChat = Action("CreateChat")
CreateKnowledgeItem = Action("CreateKnowledgeItem")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
CreatePrivateConnection = Action("CreatePrivateConnection")
DeleteAgentSpace = Action("DeleteAgentSpace")
DeleteKnowledgeItem = Action("DeleteKnowledgeItem")
DeletePrivateConnection = Action("DeletePrivateConnection")
DeregisterService = Action("DeregisterService")
DescribePrivateConnection = Action("DescribePrivateConnection")
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
GetOperatorApp = Action("GetOperatorApp")
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
ListChats = Action("ListChats")
ListExecutions = Action("ListExecutions")
ListGoals = Action("ListGoals")
ListJournalRecords = Action("ListJournalRecords")
ListKnowledgeItemVersions = Action("ListKnowledgeItemVersions")
ListKnowledgeItems = Action("ListKnowledgeItems")
ListPendingMessages = Action("ListPendingMessages")
ListPrivateConnections = Action("ListPrivateConnections")
ListRecommendations = Action("ListRecommendations")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
ListWebhooks = Action("ListWebhooks")
RegisterService = Action("RegisterService")
SearchServiceAccessibleResource = Action("SearchServiceAccessibleResource")
SendChatMessage = Action("SendChatMessage")
SendMessage = Action("SendMessage")
StreamMessage = Action("StreamMessage")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgentSpace = Action("UpdateAgentSpace")
UpdateAssociation = Action("UpdateAssociation")
UpdateBacklogTask = Action("UpdateBacklogTask")
UpdateGoal = Action("UpdateGoal")
UpdateKnowledgeItem = Action("UpdateKnowledgeItem")
UpdateOperatorAppIdpConfig = Action("UpdateOperatorAppIdpConfig")
UpdateOperatorAppTeams = Action("UpdateOperatorAppTeams")
UpdatePrivateConnectionCertificate = Action("UpdatePrivateConnectionCertificate")
UpdateRecommendation = Action("UpdateRecommendation")
ValidateAwsAssociations = Action("ValidateAwsAssociations")
