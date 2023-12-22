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


CreateAssistant = Action("CreateAssistant")
CreateAssistantAssociation = Action("CreateAssistantAssociation")
CreateContent = Action("CreateContent")
CreateKnowledgeBase = Action("CreateKnowledgeBase")
CreateQuickResponse = Action("CreateQuickResponse")
CreateSession = Action("CreateSession")
DeleteAssistant = Action("DeleteAssistant")
DeleteAssistantAssociation = Action("DeleteAssistantAssociation")
DeleteContent = Action("DeleteContent")
DeleteImportJob = Action("DeleteImportJob")
DeleteKnowledgeBase = Action("DeleteKnowledgeBase")
DeleteQuickResponse = Action("DeleteQuickResponse")
GetAssistant = Action("GetAssistant")
GetAssistantAssociation = Action("GetAssistantAssociation")
GetContent = Action("GetContent")
GetContentSummary = Action("GetContentSummary")
GetImportJob = Action("GetImportJob")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetQuickResponse = Action("GetQuickResponse")
GetRecommendations = Action("GetRecommendations")
GetSession = Action("GetSession")
ListAssistantAssociations = Action("ListAssistantAssociations")
ListAssistants = Action("ListAssistants")
ListContents = Action("ListContents")
ListImportJobs = Action("ListImportJobs")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListQuickResponses = Action("ListQuickResponses")
ListTagsForResource = Action("ListTagsForResource")
NotifyRecommendationsReceived = Action("NotifyRecommendationsReceived")
PutFeedback = Action("PutFeedback")
QueryAssistant = Action("QueryAssistant")
RemoveKnowledgeBaseTemplateUri = Action("RemoveKnowledgeBaseTemplateUri")
SearchContent = Action("SearchContent")
SearchQuickResponses = Action("SearchQuickResponses")
SearchSessions = Action("SearchSessions")
StartContentUpload = Action("StartContentUpload")
StartImportJob = Action("StartImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateContent = Action("UpdateContent")
UpdateKnowledgeBaseTemplateUri = Action("UpdateKnowledgeBaseTemplateUri")
UpdateQuickResponse = Action("UpdateQuickResponse")
