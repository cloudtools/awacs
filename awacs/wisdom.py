# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Wisdom"
prefix = "wisdom"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CreateSession = Action("CreateSession")
DeleteAssistant = Action("DeleteAssistant")
DeleteAssistantAssociation = Action("DeleteAssistantAssociation")
DeleteContent = Action("DeleteContent")
DeleteKnowledgeBase = Action("DeleteKnowledgeBase")
GetAssistant = Action("GetAssistant")
GetAssistantAssociation = Action("GetAssistantAssociation")
GetContent = Action("GetContent")
GetContentSummary = Action("GetContentSummary")
GetKnowledgeBase = Action("GetKnowledgeBase")
GetRecommendations = Action("GetRecommendations")
GetSession = Action("GetSession")
ListAssistantAssociations = Action("ListAssistantAssociations")
ListAssistants = Action("ListAssistants")
ListContents = Action("ListContents")
ListKnowledgeBases = Action("ListKnowledgeBases")
ListTagsForResource = Action("ListTagsForResource")
NotifyRecommendationsReceived = Action("NotifyRecommendationsReceived")
QueryAssistant = Action("QueryAssistant")
RemoveKnowledgeBaseTemplateUri = Action("RemoveKnowledgeBaseTemplateUri")
SearchContent = Action("SearchContent")
SearchSessions = Action("SearchSessions")
StartContentUpload = Action("StartContentUpload")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateContent = Action("UpdateContent")
UpdateKnowledgeBaseTemplateUri = Action("UpdateKnowledgeBaseTemplateUri")
