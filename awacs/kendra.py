# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kendra"
prefix = "kendra"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateEntitiesToExperience = Action("AssociateEntitiesToExperience")
AssociatePersonasToEntities = Action("AssociatePersonasToEntities")
BatchDeleteDocument = Action("BatchDeleteDocument")
BatchGetDocumentStatus = Action("BatchGetDocumentStatus")
BatchPutDocument = Action("BatchPutDocument")
ClearQuerySuggestions = Action("ClearQuerySuggestions")
CreateDataSource = Action("CreateDataSource")
CreateExperience = Action("CreateExperience")
CreateFaq = Action("CreateFaq")
CreateIndex = Action("CreateIndex")
CreateQuerySuggestionsBlockList = Action("CreateQuerySuggestionsBlockList")
CreateThesaurus = Action("CreateThesaurus")
DeleteDataSource = Action("DeleteDataSource")
DeleteExperience = Action("DeleteExperience")
DeleteFaq = Action("DeleteFaq")
DeleteIndex = Action("DeleteIndex")
DeletePrincipalMapping = Action("DeletePrincipalMapping")
DeleteQuerySuggestionsBlockList = Action("DeleteQuerySuggestionsBlockList")
DeleteThesaurus = Action("DeleteThesaurus")
DescribeDataSource = Action("DescribeDataSource")
DescribeExperience = Action("DescribeExperience")
DescribeFaq = Action("DescribeFaq")
DescribeIndex = Action("DescribeIndex")
DescribePrincipalMapping = Action("DescribePrincipalMapping")
DescribeQuerySuggestionsBlockList = Action("DescribeQuerySuggestionsBlockList")
DescribeQuerySuggestionsConfig = Action("DescribeQuerySuggestionsConfig")
DescribeThesaurus = Action("DescribeThesaurus")
DisassociateEntitiesFromExperience = Action("DisassociateEntitiesFromExperience")
DisassociatePersonasFromEntities = Action("DisassociatePersonasFromEntities")
GetQuerySuggestions = Action("GetQuerySuggestions")
GetSnapshots = Action("GetSnapshots")
ListDataSourceSyncJobs = Action("ListDataSourceSyncJobs")
ListDataSources = Action("ListDataSources")
ListEntityPersonas = Action("ListEntityPersonas")
ListExperienceEntities = Action("ListExperienceEntities")
ListExperiences = Action("ListExperiences")
ListFaqs = Action("ListFaqs")
ListGroupsOlderThanOrderingId = Action("ListGroupsOlderThanOrderingId")
ListIndices = Action("ListIndices")
ListQuerySuggestionsBlockLists = Action("ListQuerySuggestionsBlockLists")
ListTagsForResource = Action("ListTagsForResource")
ListThesauri = Action("ListThesauri")
PutPrincipalMapping = Action("PutPrincipalMapping")
Query = Action("Query")
StartDataSourceSyncJob = Action("StartDataSourceSyncJob")
StopDataSourceSyncJob = Action("StopDataSourceSyncJob")
SubmitFeedback = Action("SubmitFeedback")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataSource = Action("UpdateDataSource")
UpdateExperience = Action("UpdateExperience")
UpdateIndex = Action("UpdateIndex")
UpdateQuerySuggestionsBlockList = Action("UpdateQuerySuggestionsBlockList")
UpdateQuerySuggestionsConfig = Action("UpdateQuerySuggestionsConfig")
UpdateThesaurus = Action("UpdateThesaurus")
