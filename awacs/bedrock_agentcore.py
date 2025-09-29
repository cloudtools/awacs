# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Bedrock Agentcore"
prefix = "bedrock-agentcore"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
ConnectBrowserAutomationStream = Action("ConnectBrowserAutomationStream")
ConnectBrowserLiveViewStream = Action("ConnectBrowserLiveViewStream")
CreateAgentRuntime = Action("CreateAgentRuntime")
CreateAgentRuntimeEndpoint = Action("CreateAgentRuntimeEndpoint")
CreateApiKeyCredentialProvider = Action("CreateApiKeyCredentialProvider")
CreateBrowser = Action("CreateBrowser")
CreateCodeInterpreter = Action("CreateCodeInterpreter")
CreateEvent = Action("CreateEvent")
CreateGateway = Action("CreateGateway")
CreateGatewayTarget = Action("CreateGatewayTarget")
CreateMemory = Action("CreateMemory")
CreateOauth2CredentialProvider = Action("CreateOauth2CredentialProvider")
CreateWorkloadIdentity = Action("CreateWorkloadIdentity")
DeleteAgentRuntime = Action("DeleteAgentRuntime")
DeleteAgentRuntimeEndpoint = Action("DeleteAgentRuntimeEndpoint")
DeleteApiKeyCredentialProvider = Action("DeleteApiKeyCredentialProvider")
DeleteBrowser = Action("DeleteBrowser")
DeleteCodeInterpreter = Action("DeleteCodeInterpreter")
DeleteEvent = Action("DeleteEvent")
DeleteGateway = Action("DeleteGateway")
DeleteGatewayTarget = Action("DeleteGatewayTarget")
DeleteMemory = Action("DeleteMemory")
DeleteMemoryRecord = Action("DeleteMemoryRecord")
DeleteOauth2CredentialProvider = Action("DeleteOauth2CredentialProvider")
DeleteWorkloadIdentity = Action("DeleteWorkloadIdentity")
GetAgentRuntime = Action("GetAgentRuntime")
GetAgentRuntimeEndpoint = Action("GetAgentRuntimeEndpoint")
GetApiKeyCredentialProvider = Action("GetApiKeyCredentialProvider")
GetBrowser = Action("GetBrowser")
GetBrowserSession = Action("GetBrowserSession")
GetCodeInterpreter = Action("GetCodeInterpreter")
GetCodeInterpreterSession = Action("GetCodeInterpreterSession")
GetEvent = Action("GetEvent")
GetGateway = Action("GetGateway")
GetGatewayTarget = Action("GetGatewayTarget")
GetMemory = Action("GetMemory")
GetMemoryRecord = Action("GetMemoryRecord")
GetOauth2CredentialProvider = Action("GetOauth2CredentialProvider")
GetResourceApiKey = Action("GetResourceApiKey")
GetResourceOauth2Token = Action("GetResourceOauth2Token")
GetTokenVault = Action("GetTokenVault")
GetWorkloadAccessToken = Action("GetWorkloadAccessToken")
GetWorkloadAccessTokenForJWT = Action("GetWorkloadAccessTokenForJWT")
GetWorkloadAccessTokenForUserId = Action("GetWorkloadAccessTokenForUserId")
GetWorkloadIdentity = Action("GetWorkloadIdentity")
InvokeAgentRuntime = Action("InvokeAgentRuntime")
InvokeAgentRuntimeEndpoint = Action("InvokeAgentRuntimeEndpoint")
InvokeCodeInterpreter = Action("InvokeCodeInterpreter")
ListActors = Action("ListActors")
ListAgentRuntimeEndpoints = Action("ListAgentRuntimeEndpoints")
ListAgentRuntimeVersions = Action("ListAgentRuntimeVersions")
ListAgentRuntimes = Action("ListAgentRuntimes")
ListApiKeyCredentialProviders = Action("ListApiKeyCredentialProviders")
ListBrowserSessions = Action("ListBrowserSessions")
ListBrowsers = Action("ListBrowsers")
ListCodeInterpreterSessions = Action("ListCodeInterpreterSessions")
ListCodeInterpreters = Action("ListCodeInterpreters")
ListEvents = Action("ListEvents")
ListGatewayTargets = Action("ListGatewayTargets")
ListGateways = Action("ListGateways")
ListMemories = Action("ListMemories")
ListMemoryRecords = Action("ListMemoryRecords")
ListOauth2CredentialProviders = Action("ListOauth2CredentialProviders")
ListSessions = Action("ListSessions")
ListTagsForResource = Action("ListTagsForResource")
ListWorkloadIdentities = Action("ListWorkloadIdentities")
RetrieveMemoryRecords = Action("RetrieveMemoryRecords")
SetTokenVaultCMK = Action("SetTokenVaultCMK")
StartBrowserSession = Action("StartBrowserSession")
StartCodeInterpreterSession = Action("StartCodeInterpreterSession")
StopBrowserSession = Action("StopBrowserSession")
StopCodeInterpreterSession = Action("StopCodeInterpreterSession")
SynchronizeGatewayTargets = Action("SynchronizeGatewayTargets")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgentRuntime = Action("UpdateAgentRuntime")
UpdateAgentRuntimeEndpoint = Action("UpdateAgentRuntimeEndpoint")
UpdateApiKeyCredentialProvider = Action("UpdateApiKeyCredentialProvider")
UpdateBrowserStream = Action("UpdateBrowserStream")
UpdateGateway = Action("UpdateGateway")
UpdateGatewayTarget = Action("UpdateGatewayTarget")
UpdateMemory = Action("UpdateMemory")
UpdateOauth2CredentialProvider = Action("UpdateOauth2CredentialProvider")
UpdateWorkloadIdentity = Action("UpdateWorkloadIdentity")
