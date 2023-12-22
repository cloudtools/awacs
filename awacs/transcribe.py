# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Transcribe"
prefix = "transcribe"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCallAnalyticsCategory = Action("CreateCallAnalyticsCategory")
CreateLanguageModel = Action("CreateLanguageModel")
CreateMedicalVocabulary = Action("CreateMedicalVocabulary")
CreateVocabulary = Action("CreateVocabulary")
CreateVocabularyFilter = Action("CreateVocabularyFilter")
DeleteCallAnalyticsCategory = Action("DeleteCallAnalyticsCategory")
DeleteCallAnalyticsJob = Action("DeleteCallAnalyticsJob")
DeleteLanguageModel = Action("DeleteLanguageModel")
DeleteMedicalScribeJob = Action("DeleteMedicalScribeJob")
DeleteMedicalTranscriptionJob = Action("DeleteMedicalTranscriptionJob")
DeleteMedicalVocabulary = Action("DeleteMedicalVocabulary")
DeleteTranscriptionJob = Action("DeleteTranscriptionJob")
DeleteVocabulary = Action("DeleteVocabulary")
DeleteVocabularyFilter = Action("DeleteVocabularyFilter")
DescribeLanguageModel = Action("DescribeLanguageModel")
GetCallAnalyticsCategory = Action("GetCallAnalyticsCategory")
GetCallAnalyticsJob = Action("GetCallAnalyticsJob")
GetMedicalScribeJob = Action("GetMedicalScribeJob")
GetMedicalTranscriptionJob = Action("GetMedicalTranscriptionJob")
GetMedicalVocabulary = Action("GetMedicalVocabulary")
GetTranscriptionJob = Action("GetTranscriptionJob")
GetVocabulary = Action("GetVocabulary")
GetVocabularyFilter = Action("GetVocabularyFilter")
ListCallAnalyticsCategories = Action("ListCallAnalyticsCategories")
ListCallAnalyticsJobs = Action("ListCallAnalyticsJobs")
ListLanguageModels = Action("ListLanguageModels")
ListMedicalScribeJobs = Action("ListMedicalScribeJobs")
ListMedicalTranscriptionJobs = Action("ListMedicalTranscriptionJobs")
ListMedicalVocabularies = Action("ListMedicalVocabularies")
ListTagsForResource = Action("ListTagsForResource")
ListTranscriptionJobs = Action("ListTranscriptionJobs")
ListVocabularies = Action("ListVocabularies")
ListVocabularyFilters = Action("ListVocabularyFilters")
StartCallAnalyticsJob = Action("StartCallAnalyticsJob")
StartCallAnalyticsStreamTranscription = Action("StartCallAnalyticsStreamTranscription")
StartCallAnalyticsStreamTranscriptionWebSocket = Action(
    "StartCallAnalyticsStreamTranscriptionWebSocket"
)
StartMedicalScribeJob = Action("StartMedicalScribeJob")
StartMedicalStreamTranscription = Action("StartMedicalStreamTranscription")
StartMedicalStreamTranscriptionWebSocket = Action(
    "StartMedicalStreamTranscriptionWebSocket"
)
StartMedicalTranscriptionJob = Action("StartMedicalTranscriptionJob")
StartStreamTranscription = Action("StartStreamTranscription")
StartStreamTranscriptionWebSocket = Action("StartStreamTranscriptionWebSocket")
StartTranscriptionJob = Action("StartTranscriptionJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCallAnalyticsCategory = Action("UpdateCallAnalyticsCategory")
UpdateMedicalVocabulary = Action("UpdateMedicalVocabulary")
UpdateVocabulary = Action("UpdateVocabulary")
UpdateVocabularyFilter = Action("UpdateVocabularyFilter")
