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
CreateGuardrail = Action("CreateGuardrail")
CreateGuardrailVersion = Action("CreateGuardrailVersion")
CreateKnowledgeBase = Action("CreateKnowledgeBase")
CreateModelCustomizationJob = Action("CreateModelCustomizationJob")
CreateModelEvaluationJob = Action("CreateModelEvaluationJob")
CreateModelInvocationJob = Action("CreateModelInvocationJob")
CreateProvisionedModelThroughput = Action("CreateProvisionedModelThroughput")
DeleteAgent = Action("DeleteAgent")
DeleteAgentActionGroup = Action("DeleteAgentActionGroup")
DeleteAgentAlias = Action("DeleteAgentAlias")
DeleteAgentVersion = Action("DeleteAgentVersion")
DeleteCustomModel = Action("DeleteCustomModel")
DeleteDataSource = Action("DeleteDataSource")
DeleteFoundationModelAgreement = Action("DeleteFoundationModelAgreement")
DeleteGuardrail = Action("DeleteGuardrail")
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
GetGuardrail = Action("GetGuardrail")
GetIngestionJob = Action("GetIngestionJob")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetModelCustomizationJob = Action("GetModelCustomizationJob")
GetModelEvaluationJob = Action("GetModelEvaluationJob")
GetModelInvocationJob = Action("GetModelInvocationJob")
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
ListGuardrails = Action("ListGuardrails")
ListIngestionJobs = Action("ListIngestionJobs")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListModelCustomizationJobs = Action("ListModelCustomizationJobs")
ListModelEvaluationJobs = Action("ListModelEvaluationJobs")
ListModelInvocationJobs = Action("ListModelInvocationJobs")
ListPrompts = Action("ListPrompts")
ListProvisionedModelThroughputs = Action("ListProvisionedModelThroughputs")
ListTagsForResource = Action("ListTagsForResource")
PrepareAgent = Action("PrepareAgent")
PutFoundationModelEntitlement = Action("PutFoundationModelEntitlement")
PutModelInvocationLoggingConfiguration = Action(
    "PutModelInvocationLoggingConfiguration"
)
PutUseCaseForModelAccess = Action("PutUseCaseForModelAccess")
QueryKnowledgeBase = Action("QueryKnowledgeBase")
Retrieve = Action("Retrieve")
RetrieveAndGenerate = Action("RetrieveAndGenerate")
StartIngestionJob = Action("StartIngestionJob")
StopModelCustomizationJob = Action("StopModelCustomizationJob")
StopModelInvocationJob = Action("StopModelInvocationJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateAgentActionGroup = Action("UpdateAgentActionGroup")
UpdateAgentAlias = Action("UpdateAgentAlias")
UpdateAgentKnowledgeBase = Action("UpdateAgentKnowledgeBase")
UpdateDataSource = Action("UpdateDataSource")
UpdateGuardrail = Action("UpdateGuardrail")
UpdateKnowledgeBase = Action("UpdateKnowledgeBase")
UpdatePrompt = Action("UpdatePrompt")
UpdateProvisionedModelThroughput = Action("UpdateProvisionedModelThroughput")
