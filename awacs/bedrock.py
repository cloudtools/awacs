# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Bedrock"
prefix = "bedrock"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAgentKnowledgeBase = Action("AssociateAgentKnowledgeBase")
AssociateThirdPartyKnowledgeBase = Action("AssociateThirdPartyKnowledgeBase")
CreateAgent = Action("CreateAgent")
CreateAgentActionGroup = Action("CreateAgentActionGroup")
CreateAgentAlias = Action("CreateAgentAlias")
CreateAgentDraftSnapshot = Action("CreateAgentDraftSnapshot")
CreateDataSource = Action("CreateDataSource")
CreateFoundationModelAgreement = Action("CreateFoundationModelAgreement")
CreateKnowledgeBase = Action("CreateKnowledgeBase")
CreateModelCustomizationJob = Action("CreateModelCustomizationJob")
CreateProvisionedModelThroughput = Action("CreateProvisionedModelThroughput")
DeleteCustomModel = Action("DeleteCustomModel")
DeleteDataSource = Action("DeleteDataSource")
DeleteFoundationModelAgreement = Action("DeleteFoundationModelAgreement")
DeleteKnowledgeBase = Action("DeleteKnowledgeBase")
DeleteModelInvocationLoggingConfiguration = Action(
    "DeleteModelInvocationLoggingConfiguration"
)
DeletePrompt = Action("DeletePrompt")
DeleteProvisionedModelThroughput = Action("DeleteProvisionedModelThroughput")
DisassociateAgentKnowledgeBase = Action("DisassociateAgentKnowledgeBase")
GetAgent = Action("GetAgent")
GetAgentActionGroup = Action("GetAgentActionGroup")
GetAgentAlias = Action("GetAgentAlias")
GetAgentKnowledgeBase = Action("GetAgentKnowledgeBase")
GetAgentVersion = Action("GetAgentVersion")
GetCustomModel = Action("GetCustomModel")
GetDataSource = Action("GetDataSource")
GetFoundationModel = Action("GetFoundationModel")
GetFoundationModelAvailability = Action("GetFoundationModelAvailability")
GetIngestionJob = Action("GetIngestionJob")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetModelCustomizationJob = Action("GetModelCustomizationJob")
GetModelInvocationLoggingConfiguration = Action(
    "GetModelInvocationLoggingConfiguration"
)
GetPrompt = Action("GetPrompt")
GetProvisionedModelThroughput = Action("GetProvisionedModelThroughput")
GetUseCaseForModelAccess = Action("GetUseCaseForModelAccess")
InvokeAgent = Action("InvokeAgent")
InvokeModel = Action("InvokeModel")
InvokeModelWithResponseStream = Action("InvokeModelWithResponseStream")
ListAgentActionGroups = Action("ListAgentActionGroups")
ListAgentAliases = Action("ListAgentAliases")
ListAgentKnowledgeBases = Action("ListAgentKnowledgeBases")
ListAgentVersions = Action("ListAgentVersions")
ListAgents = Action("ListAgents")
ListCustomModels = Action("ListCustomModels")
ListDataSources = Action("ListDataSources")
ListFoundationModelAgreementOffers = Action("ListFoundationModelAgreementOffers")
ListFoundationModels = Action("ListFoundationModels")
ListIngestionJobs = Action("ListIngestionJobs")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListModelCustomizationJobs = Action("ListModelCustomizationJobs")
ListPrompts = Action("ListPrompts")
ListProvisionedModelThroughputs = Action("ListProvisionedModelThroughputs")
ListTagsForResource = Action("ListTagsForResource")
PutFoundationModelEntitlement = Action("PutFoundationModelEntitlement")
PutModelInvocationLoggingConfiguration = Action(
    "PutModelInvocationLoggingConfiguration"
)
PutUseCaseForModelAccess = Action("PutUseCaseForModelAccess")
QueryKnowledgeBase = Action("QueryKnowledgeBase")
StartIngestionJob = Action("StartIngestionJob")
StopModelCustomizationJob = Action("StopModelCustomizationJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateAgentActionGroup = Action("UpdateAgentActionGroup")
UpdateAgentAlias = Action("UpdateAgentAlias")
UpdateAgentKnowledgeBase = Action("UpdateAgentKnowledgeBase")
UpdateDataSource = Action("UpdateDataSource")
UpdateKnowledgeBase = Action("UpdateKnowledgeBase")
UpdatePrompt = Action("UpdatePrompt")
UpdateProvisionedModelThroughput = Action("UpdateProvisionedModelThroughput")
