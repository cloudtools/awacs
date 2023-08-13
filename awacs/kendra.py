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
BatchDeleteFeaturedResultsSet = Action("BatchDeleteFeaturedResultsSet")
BatchGetDocumentStatus = Action("BatchGetDocumentStatus")
BatchPutDocument = Action("BatchPutDocument")
ClearQuerySuggestions = Action("ClearQuerySuggestions")
CreateAccessControlConfiguration = Action("CreateAccessControlConfiguration")
CreateDataSource = Action("CreateDataSource")
CreateExperience = Action("CreateExperience")
CreateFaq = Action("CreateFaq")
CreateFeaturedResultsSet = Action("CreateFeaturedResultsSet")
CreateIndex = Action("CreateIndex")
CreateQuerySuggestionsBlockList = Action("CreateQuerySuggestionsBlockList")
CreateThesaurus = Action("CreateThesaurus")
DeleteAccessControlConfiguration = Action("DeleteAccessControlConfiguration")
DeleteDataSource = Action("DeleteDataSource")
DeleteExperience = Action("DeleteExperience")
DeleteFaq = Action("DeleteFaq")
DeleteIndex = Action("DeleteIndex")
DeletePrincipalMapping = Action("DeletePrincipalMapping")
DeleteQuerySuggestionsBlockList = Action("DeleteQuerySuggestionsBlockList")
DeleteThesaurus = Action("DeleteThesaurus")
DescribeAccessControlConfiguration = Action("DescribeAccessControlConfiguration")
DescribeDataSource = Action("DescribeDataSource")
DescribeExperience = Action("DescribeExperience")
DescribeFaq = Action("DescribeFaq")
DescribeFeaturedResultsSet = Action("DescribeFeaturedResultsSet")
DescribeIndex = Action("DescribeIndex")
DescribePrincipalMapping = Action("DescribePrincipalMapping")
DescribeQuerySuggestionsBlockList = Action("DescribeQuerySuggestionsBlockList")
DescribeQuerySuggestionsConfig = Action("DescribeQuerySuggestionsConfig")
DescribeThesaurus = Action("DescribeThesaurus")
DisassociateEntitiesFromExperience = Action("DisassociateEntitiesFromExperience")
DisassociatePersonasFromEntities = Action("DisassociatePersonasFromEntities")
GetQuerySuggestions = Action("GetQuerySuggestions")
GetSnapshots = Action("GetSnapshots")
ListAccessControlConfigurations = Action("ListAccessControlConfigurations")
ListDataSourceSyncJobs = Action("ListDataSourceSyncJobs")
ListDataSources = Action("ListDataSources")
ListEntityPersonas = Action("ListEntityPersonas")
ListExperienceEntities = Action("ListExperienceEntities")
ListExperiences = Action("ListExperiences")
ListFaqs = Action("ListFaqs")
ListFeaturedResultsSets = Action("ListFeaturedResultsSets")
ListGroupsOlderThanOrderingId = Action("ListGroupsOlderThanOrderingId")
ListIndices = Action("ListIndices")
ListQuerySuggestionsBlockLists = Action("ListQuerySuggestionsBlockLists")
ListTagsForResource = Action("ListTagsForResource")
ListThesauri = Action("ListThesauri")
PutPrincipalMapping = Action("PutPrincipalMapping")
Query = Action("Query")
Retrieve = Action("Retrieve")
StartDataSourceSyncJob = Action("StartDataSourceSyncJob")
StopDataSourceSyncJob = Action("StopDataSourceSyncJob")
SubmitFeedback = Action("SubmitFeedback")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessControlConfiguration = Action("UpdateAccessControlConfiguration")
UpdateDataSource = Action("UpdateDataSource")
UpdateExperience = Action("UpdateExperience")
UpdateFeaturedResultsSet = Action("UpdateFeaturedResultsSet")
UpdateIndex = Action("UpdateIndex")
UpdateQuerySuggestionsBlockList = Action("UpdateQuerySuggestionsBlockList")
UpdateQuerySuggestionsConfig = Action("UpdateQuerySuggestionsConfig")
UpdateThesaurus = Action("UpdateThesaurus")
