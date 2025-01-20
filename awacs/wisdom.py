# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Q in Connect"
prefix = "wisdom"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateMessageTemplate = Action("ActivateMessageTemplate")
AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
CreateAIAgent = Action("CreateAIAgent")
CreateAIAgentVersion = Action("CreateAIAgentVersion")
CreateAIGuardrail = Action("CreateAIGuardrail")
CreateAIGuardrailVersion = Action("CreateAIGuardrailVersion")
CreateAIPrompt = Action("CreateAIPrompt")
CreateAIPromptVersion = Action("CreateAIPromptVersion")
CreateAssistant = Action("CreateAssistant")
CreateAssistantAssociation = Action("CreateAssistantAssociation")
CreateContent = Action("CreateContent")
CreateContentAssociation = Action("CreateContentAssociation")
CreateKnowledgeBase = Action("CreateKnowledgeBase")
CreateMessageTemplate = Action("CreateMessageTemplate")
CreateMessageTemplateAttachment = Action("CreateMessageTemplateAttachment")
CreateMessageTemplateVersion = Action("CreateMessageTemplateVersion")
CreateQuickResponse = Action("CreateQuickResponse")
CreateSession = Action("CreateSession")
DeactivateMessageTemplate = Action("DeactivateMessageTemplate")
DeleteAIAgent = Action("DeleteAIAgent")
DeleteAIAgentVersion = Action("DeleteAIAgentVersion")
DeleteAIGuardrail = Action("DeleteAIGuardrail")
DeleteAIGuardrailVersion = Action("DeleteAIGuardrailVersion")
DeleteAIPrompt = Action("DeleteAIPrompt")
DeleteAIPromptVersion = Action("DeleteAIPromptVersion")
DeleteAssistant = Action("DeleteAssistant")
DeleteAssistantAssociation = Action("DeleteAssistantAssociation")
DeleteContent = Action("DeleteContent")
DeleteContentAssociation = Action("DeleteContentAssociation")
DeleteImportJob = Action("DeleteImportJob")
DeleteKnowledgeBase = Action("DeleteKnowledgeBase")
DeleteMessageTemplate = Action("DeleteMessageTemplate")
DeleteMessageTemplateAttachment = Action("DeleteMessageTemplateAttachment")
DeleteQuickResponse = Action("DeleteQuickResponse")
GetAIAgent = Action("GetAIAgent")
GetAIGuardrail = Action("GetAIGuardrail")
GetAIPrompt = Action("GetAIPrompt")
GetAssistant = Action("GetAssistant")
GetAssistantAssociation = Action("GetAssistantAssociation")
GetContent = Action("GetContent")
GetContentAssociation = Action("GetContentAssociation")
GetContentSummary = Action("GetContentSummary")
GetImportJob = Action("GetImportJob")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetMessageTemplate = Action("GetMessageTemplate")
GetNextMessage = Action("GetNextMessage")
GetQuickResponse = Action("GetQuickResponse")
GetRecommendations = Action("GetRecommendations")
GetSession = Action("GetSession")
ListAIAgentVersions = Action("ListAIAgentVersions")
ListAIAgents = Action("ListAIAgents")
ListAIGuardrailVersions = Action("ListAIGuardrailVersions")
ListAIGuardrails = Action("ListAIGuardrails")
ListAIPromptVersions = Action("ListAIPromptVersions")
ListAIPrompts = Action("ListAIPrompts")
ListAssistantAssociations = Action("ListAssistantAssociations")
ListAssistants = Action("ListAssistants")
ListContentAssociations = Action("ListContentAssociations")
ListContents = Action("ListContents")
ListImportJobs = Action("ListImportJobs")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListMessageTemplateVersions = Action("ListMessageTemplateVersions")
ListMessageTemplates = Action("ListMessageTemplates")
ListMessages = Action("ListMessages")
ListQuickResponses = Action("ListQuickResponses")
ListTagsForResource = Action("ListTagsForResource")
NotifyRecommendationsReceived = Action("NotifyRecommendationsReceived")
PutFeedback = Action("PutFeedback")
QueryAssistant = Action("QueryAssistant")
RemoveAssistantAIAgent = Action("RemoveAssistantAIAgent")
RemoveKnowledgeBaseTemplateUri = Action("RemoveKnowledgeBaseTemplateUri")
RenderMessageTemplate = Action("RenderMessageTemplate")
SearchContent = Action("SearchContent")
SearchMessageTemplates = Action("SearchMessageTemplates")
SearchQuickResponses = Action("SearchQuickResponses")
SearchSessions = Action("SearchSessions")
SendMessage = Action("SendMessage")
StartContentUpload = Action("StartContentUpload")
StartImportJob = Action("StartImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAIAgent = Action("UpdateAIAgent")
UpdateAIGuardrail = Action("UpdateAIGuardrail")
UpdateAIPrompt = Action("UpdateAIPrompt")
UpdateAssistantAIAgent = Action("UpdateAssistantAIAgent")
UpdateContent = Action("UpdateContent")
UpdateKnowledgeBaseTemplateUri = Action("UpdateKnowledgeBaseTemplateUri")
UpdateMessageTemplate = Action("UpdateMessageTemplate")
UpdateMessageTemplateMetadata = Action("UpdateMessageTemplateMetadata")
UpdateQuickResponse = Action("UpdateQuickResponse")
UpdateSession = Action("UpdateSession")
UpdateSessionData = Action("UpdateSessionData")
