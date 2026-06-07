# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS FinOps Agent"
prefix = "finops-agent"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAgentRequest = Action("AcceptAgentRequest")
CancelTask = Action("CancelTask")
CancelTurn = Action("CancelTurn")
CreateAgentSpace = Action("CreateAgentSpace")
CreateAutomation = Action("CreateAutomation")
CreateConnection = Action("CreateConnection")
CreateConversation = Action("CreateConversation")
CreateDocument = Action("CreateDocument")
CreateIntegration = Action("CreateIntegration")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
CreateTask = Action("CreateTask")
CreateTurn = Action("CreateTurn")
DeleteAgentSpace = Action("DeleteAgentSpace")
DeleteArtifact = Action("DeleteArtifact")
DeleteAutomation = Action("DeleteAutomation")
DeleteConnection = Action("DeleteConnection")
DeleteDocument = Action("DeleteDocument")
DeleteIntegration = Action("DeleteIntegration")
GetAgentRequest = Action("GetAgentRequest")
GetAgentSpace = Action("GetAgentSpace")
GetArtifactContent = Action("GetArtifactContent")
GetArtifactMetadata = Action("GetArtifactMetadata")
GetAutomation = Action("GetAutomation")
GetConnection = Action("GetConnection")
GetDocumentContent = Action("GetDocumentContent")
GetDocumentMetadata = Action("GetDocumentMetadata")
GetIntegration = Action("GetIntegration")
GetTask = Action("GetTask")
GetTurn = Action("GetTurn")
ListAgentSpaces = Action("ListAgentSpaces")
ListArtifacts = Action("ListArtifacts")
ListAutomations = Action("ListAutomations")
ListConnections = Action("ListConnections")
ListConversations = Action("ListConversations")
ListDocuments = Action("ListDocuments")
ListIntegrations = Action("ListIntegrations")
ListRecords = Action("ListRecords")
ListTasks = Action("ListTasks")
ListTurns = Action("ListTurns")
RejectAgentRequest = Action("RejectAgentRequest")
RestoreDocument = Action("RestoreDocument")
SendFeedback = Action("SendFeedback")
UpdateAgentSpace = Action("UpdateAgentSpace")
UpdateAutomation = Action("UpdateAutomation")
UpdateConnection = Action("UpdateConnection")
UpdateDocument = Action("UpdateDocument")
