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


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
ApplyGuardrail = Action("ApplyGuardrail")
AssociateAgentCollaborator = Action("AssociateAgentCollaborator")
AssociateAgentKnowledgeBase = Action("AssociateAgentKnowledgeBase")
AssociateThirdPartyKnowledgeBase = Action("AssociateThirdPartyKnowledgeBase")
BatchDeleteEvaluationJob = Action("BatchDeleteEvaluationJob")
CreateAgent = Action("CreateAgent")
CreateAgentActionGroup = Action("CreateAgentActionGroup")
CreateAgentAlias = Action("CreateAgentAlias")
CreateAgentDraftSnapshot = Action("CreateAgentDraftSnapshot")
CreateBlueprint = Action("CreateBlueprint")
CreateBlueprintVersion = Action("CreateBlueprintVersion")
CreateDataAutomationProject = Action("CreateDataAutomationProject")
CreateDataSource = Action("CreateDataSource")
CreateEvaluationJob = Action("CreateEvaluationJob")
CreateFlow = Action("CreateFlow")
CreateFlowAlias = Action("CreateFlowAlias")
CreateFlowVersion = Action("CreateFlowVersion")
CreateFoundationModelAgreement = Action("CreateFoundationModelAgreement")
CreateGuardrail = Action("CreateGuardrail")
CreateGuardrailVersion = Action("CreateGuardrailVersion")
CreateInferenceProfile = Action("CreateInferenceProfile")
CreateInvocation = Action("CreateInvocation")
CreateKnowledgeBase = Action("CreateKnowledgeBase")
CreateMarketplaceModelEndpoint = Action("CreateMarketplaceModelEndpoint")
CreateModelCopyJob = Action("CreateModelCopyJob")
CreateModelCustomizationJob = Action("CreateModelCustomizationJob")
CreateModelEvaluationJob = Action("CreateModelEvaluationJob")
CreateModelImportJob = Action("CreateModelImportJob")
CreateModelInvocationJob = Action("CreateModelInvocationJob")
CreatePrompt = Action("CreatePrompt")
CreatePromptVersion = Action("CreatePromptVersion")
CreateProvisionedModelThroughput = Action("CreateProvisionedModelThroughput")
CreateSession = Action("CreateSession")
DeleteAgent = Action("DeleteAgent")
DeleteAgentActionGroup = Action("DeleteAgentActionGroup")
DeleteAgentAlias = Action("DeleteAgentAlias")
DeleteAgentMemory = Action("DeleteAgentMemory")
DeleteAgentVersion = Action("DeleteAgentVersion")
DeleteBlueprint = Action("DeleteBlueprint")
DeleteCustomModel = Action("DeleteCustomModel")
DeleteDataAutomationProject = Action("DeleteDataAutomationProject")
DeleteDataSource = Action("DeleteDataSource")
DeleteFlow = Action("DeleteFlow")
DeleteFlowAlias = Action("DeleteFlowAlias")
DeleteFlowVersion = Action("DeleteFlowVersion")
DeleteFoundationModelAgreement = Action("DeleteFoundationModelAgreement")
DeleteGuardrail = Action("DeleteGuardrail")
DeleteImportedModel = Action("DeleteImportedModel")
DeleteInferenceProfile = Action("DeleteInferenceProfile")
DeleteKnowledgeBase = Action("DeleteKnowledgeBase")
DeleteKnowledgeBaseDocuments = Action("DeleteKnowledgeBaseDocuments")
DeleteMarketplaceModelAgreement = Action("DeleteMarketplaceModelAgreement")
DeleteMarketplaceModelEndpoint = Action("DeleteMarketplaceModelEndpoint")
DeleteModelInvocationLoggingConfiguration = Action(
    "DeleteModelInvocationLoggingConfiguration"
)
DeletePrompt = Action("DeletePrompt")
DeleteProvisionedModelThroughput = Action("DeleteProvisionedModelThroughput")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSession = Action("DeleteSession")
DeregisterMarketplaceModelEndpoint = Action("DeregisterMarketplaceModelEndpoint")
DetectGeneratedContent = Action("DetectGeneratedContent")
DisassociateAgentCollaborator = Action("DisassociateAgentCollaborator")
DisassociateAgentKnowledgeBase = Action("DisassociateAgentKnowledgeBase")
EndSession = Action("EndSession")
GenerateQuery = Action("GenerateQuery")
GetAgent = Action("GetAgent")
GetAgentActionGroup = Action("GetAgentActionGroup")
GetAgentAlias = Action("GetAgentAlias")
GetAgentCollaborator = Action("GetAgentCollaborator")
GetAgentKnowledgeBase = Action("GetAgentKnowledgeBase")
GetAgentMemory = Action("GetAgentMemory")
GetAgentVersion = Action("GetAgentVersion")
GetAsyncInvoke = Action("GetAsyncInvoke")
GetBlueprint = Action("GetBlueprint")
GetBlueprintRecommendation = Action("GetBlueprintRecommendation")
GetCustomModel = Action("GetCustomModel")
GetDataAutomationProject = Action("GetDataAutomationProject")
GetDataAutomationStatus = Action("GetDataAutomationStatus")
GetDataSource = Action("GetDataSource")
GetEvaluationJob = Action("GetEvaluationJob")
GetFlow = Action("GetFlow")
GetFlowAlias = Action("GetFlowAlias")
GetFlowVersion = Action("GetFlowVersion")
GetFoundationModel = Action("GetFoundationModel")
GetFoundationModelAvailability = Action("GetFoundationModelAvailability")
GetGuardrail = Action("GetGuardrail")
GetImportedModel = Action("GetImportedModel")
GetInferenceProfile = Action("GetInferenceProfile")
GetIngestionJob = Action("GetIngestionJob")
GetInvocationStep = Action("GetInvocationStep")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetKnowledgeBaseDocuments = Action("GetKnowledgeBaseDocuments")
GetMarketplaceModelEndpoint = Action("GetMarketplaceModelEndpoint")
GetModelCopyJob = Action("GetModelCopyJob")
GetModelCustomizationJob = Action("GetModelCustomizationJob")
GetModelEvaluationJob = Action("GetModelEvaluationJob")
GetModelImportJob = Action("GetModelImportJob")
GetModelInvocationJob = Action("GetModelInvocationJob")
GetModelInvocationLoggingConfiguration = Action(
    "GetModelInvocationLoggingConfiguration"
)
GetPrompt = Action("GetPrompt")
GetPromptRouter = Action("GetPromptRouter")
GetProvisionedModelThroughput = Action("GetProvisionedModelThroughput")
GetResourcePolicy = Action("GetResourcePolicy")
GetSession = Action("GetSession")
GetUseCaseForModelAccess = Action("GetUseCaseForModelAccess")
IngestKnowledgeBaseDocuments = Action("IngestKnowledgeBaseDocuments")
InvokeAgent = Action("InvokeAgent")
InvokeBlueprintRecommendationAsync = Action("InvokeBlueprintRecommendationAsync")
InvokeBuilder = Action("InvokeBuilder")
InvokeDataAutomationAsync = Action("InvokeDataAutomationAsync")
InvokeFlow = Action("InvokeFlow")
InvokeInlineAgent = Action("InvokeInlineAgent")
InvokeModel = Action("InvokeModel")
InvokeModelWithResponseStream = Action("InvokeModelWithResponseStream")
ListAgentActionGroups = Action("ListAgentActionGroups")
ListAgentAliases = Action("ListAgentAliases")
ListAgentCollaborators = Action("ListAgentCollaborators")
ListAgentKnowledgeBases = Action("ListAgentKnowledgeBases")
ListAgentVersions = Action("ListAgentVersions")
ListAgents = Action("ListAgents")
ListAsyncInvokes = Action("ListAsyncInvokes")
ListBlueprints = Action("ListBlueprints")
ListCustomModels = Action("ListCustomModels")
ListDataAutomationProjects = Action("ListDataAutomationProjects")
ListDataSources = Action("ListDataSources")
ListEvaluationJobs = Action("ListEvaluationJobs")
ListFlowAliases = Action("ListFlowAliases")
ListFlowVersions = Action("ListFlowVersions")
ListFlows = Action("ListFlows")
ListFoundationModelAgreementOffers = Action("ListFoundationModelAgreementOffers")
ListFoundationModels = Action("ListFoundationModels")
ListGuardrails = Action("ListGuardrails")
ListImportedModels = Action("ListImportedModels")
ListInferenceProfiles = Action("ListInferenceProfiles")
ListIngestionJobs = Action("ListIngestionJobs")
ListInvocationSteps = Action("ListInvocationSteps")
ListInvocations = Action("ListInvocations")
ListKnowledgeBaseDocuments = Action("ListKnowledgeBaseDocuments")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListMarketplaceModelEndpoints = Action("ListMarketplaceModelEndpoints")
ListModelCopyJobs = Action("ListModelCopyJobs")
ListModelCustomizationJobs = Action("ListModelCustomizationJobs")
ListModelEvaluationJobs = Action("ListModelEvaluationJobs")
ListModelImportJobs = Action("ListModelImportJobs")
ListModelInvocationJobs = Action("ListModelInvocationJobs")
ListPromptRouters = Action("ListPromptRouters")
ListPrompts = Action("ListPrompts")
ListProvisionedModelThroughputs = Action("ListProvisionedModelThroughputs")
ListSessions = Action("ListSessions")
ListTagsForResource = Action("ListTagsForResource")
OptimizePrompt = Action("OptimizePrompt")
PrepareAgent = Action("PrepareAgent")
PrepareFlow = Action("PrepareFlow")
PutFoundationModelEntitlement = Action("PutFoundationModelEntitlement")
PutInvocationStep = Action("PutInvocationStep")
PutModelInvocationLoggingConfiguration = Action(
    "PutModelInvocationLoggingConfiguration"
)
PutResourcePolicy = Action("PutResourcePolicy")
PutUseCaseForModelAccess = Action("PutUseCaseForModelAccess")
QueryKnowledgeBase = Action("QueryKnowledgeBase")
RegisterMarketplaceModelEndpoint = Action("RegisterMarketplaceModelEndpoint")
RenderPrompt = Action("RenderPrompt")
Rerank = Action("Rerank")
Retrieve = Action("Retrieve")
RetrieveAndGenerate = Action("RetrieveAndGenerate")
StartIngestionJob = Action("StartIngestionJob")
StopEvaluationJob = Action("StopEvaluationJob")
StopIngestionJob = Action("StopIngestionJob")
StopModelCustomizationJob = Action("StopModelCustomizationJob")
StopModelInvocationJob = Action("StopModelInvocationJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateAgentActionGroup = Action("UpdateAgentActionGroup")
UpdateAgentAlias = Action("UpdateAgentAlias")
UpdateAgentCollaborator = Action("UpdateAgentCollaborator")
UpdateAgentKnowledgeBase = Action("UpdateAgentKnowledgeBase")
UpdateBlueprint = Action("UpdateBlueprint")
UpdateDataAutomationProject = Action("UpdateDataAutomationProject")
UpdateDataSource = Action("UpdateDataSource")
UpdateFlow = Action("UpdateFlow")
UpdateFlowAlias = Action("UpdateFlowAlias")
UpdateGuardrail = Action("UpdateGuardrail")
UpdateKnowledgeBase = Action("UpdateKnowledgeBase")
UpdateMarketplaceModelEndpoint = Action("UpdateMarketplaceModelEndpoint")
UpdatePrompt = Action("UpdatePrompt")
UpdateProvisionedModelThroughput = Action("UpdateProvisionedModelThroughput")
UpdateSession = Action("UpdateSession")
ValidateFlowDefinition = Action("ValidateFlowDefinition")
