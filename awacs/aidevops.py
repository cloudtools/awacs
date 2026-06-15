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
CreateAccessToken = Action("CreateAccessToken")
CreateAgentSpace = Action("CreateAgentSpace")
CreateAsset = Action("CreateAsset")
CreateAssetFile = Action("CreateAssetFile")
CreateBacklogTask = Action("CreateBacklogTask")
CreateChat = Action("CreateChat")
CreateKnowledgeItem = Action("CreateKnowledgeItem")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
CreatePrivateConnection = Action("CreatePrivateConnection")
CreateTrigger = Action("CreateTrigger")
DeleteAgentSpace = Action("DeleteAgentSpace")
DeleteAsset = Action("DeleteAsset")
DeleteAssetFile = Action("DeleteAssetFile")
DeleteKnowledgeItem = Action("DeleteKnowledgeItem")
DeletePrivateConnection = Action("DeletePrivateConnection")
DeleteTrigger = Action("DeleteTrigger")
DeregisterService = Action("DeregisterService")
DescribePrivateConnection = Action("DescribePrivateConnection")
DescribeServices = Action("DescribeServices")
DescribeSupportLevel = Action("DescribeSupportLevel")
DisableOperatorApp = Action("DisableOperatorApp")
DisassociateService = Action("DisassociateService")
DiscoverTopology = Action("DiscoverTopology")
EnableOperatorApp = Action("EnableOperatorApp")
EndChatForCase = Action("EndChatForCase")
GetAccessToken = Action("GetAccessToken")
GetAccountUsage = Action("GetAccountUsage")
GetAgentSpace = Action("GetAgentSpace")
GetAsset = Action("GetAsset")
GetAssetContent = Action("GetAssetContent")
GetAssetFile = Action("GetAssetFile")
GetAssociation = Action("GetAssociation")
GetBacklogTask = Action("GetBacklogTask")
GetKnowledgeItem = Action("GetKnowledgeItem")
GetOperatorApp = Action("GetOperatorApp")
GetOperatorAppTeams = Action("GetOperatorAppTeams")
GetRecommendation = Action("GetRecommendation")
GetService = Action("GetService")
GetTrigger = Action("GetTrigger")
HandleServiceRegistrationCallback = Action("HandleServiceRegistrationCallback")
InitiateChatForCase = Action("InitiateChatForCase")
InitiateServiceRegistration = Action("InitiateServiceRegistration")
InvokeAgent = Action("InvokeAgent")
ListAccessTokens = Action("ListAccessTokens")
ListAgentSpaces = Action("ListAgentSpaces")
ListAssetFiles = Action("ListAssetFiles")
ListAssetTypes = Action("ListAssetTypes")
ListAssetVersions = Action("ListAssetVersions")
ListAssets = Action("ListAssets")
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
ListTriggers = Action("ListTriggers")
ListWebhooks = Action("ListWebhooks")
RegisterService = Action("RegisterService")
RevokeAccessToken = Action("RevokeAccessToken")
RotateAccessToken = Action("RotateAccessToken")
SearchServiceAccessibleResource = Action("SearchServiceAccessibleResource")
SendChatMessage = Action("SendChatMessage")
SendMessage = Action("SendMessage")
StreamMessage = Action("StreamMessage")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgentSpace = Action("UpdateAgentSpace")
UpdateAsset = Action("UpdateAsset")
UpdateAssetFile = Action("UpdateAssetFile")
UpdateAssociation = Action("UpdateAssociation")
UpdateBacklogTask = Action("UpdateBacklogTask")
UpdateGoal = Action("UpdateGoal")
UpdateKnowledgeItem = Action("UpdateKnowledgeItem")
UpdateOperatorAppIdpConfig = Action("UpdateOperatorAppIdpConfig")
UpdateOperatorAppTeams = Action("UpdateOperatorAppTeams")
UpdatePrivateConnectionCertificate = Action("UpdatePrivateConnectionCertificate")
UpdateRecommendation = Action("UpdateRecommendation")
UpdateTrigger = Action("UpdateTrigger")
ValidateAwsAssociations = Action("ValidateAwsAssociations")
