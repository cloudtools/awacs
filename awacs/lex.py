# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lex"
prefix = "lex"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreateCustomVocabularyItem = Action("BatchCreateCustomVocabularyItem")
BatchDeleteCustomVocabularyItem = Action("BatchDeleteCustomVocabularyItem")
BatchUpdateCustomVocabularyItem = Action("BatchUpdateCustomVocabularyItem")
BuildBotLocale = Action("BuildBotLocale")
CreateBot = Action("CreateBot")
CreateBotAlias = Action("CreateBotAlias")
CreateBotChannel = Action("CreateBotChannel")
CreateBotLocale = Action("CreateBotLocale")
CreateBotReplica = Action("CreateBotReplica")
CreateBotVersion = Action("CreateBotVersion")
CreateCustomVocabulary = Action("CreateCustomVocabulary")
CreateExport = Action("CreateExport")
CreateIntent = Action("CreateIntent")
CreateIntentVersion = Action("CreateIntentVersion")
CreateResourcePolicy = Action("CreateResourcePolicy")
CreateResourcePolicyStatement = Action("CreateResourcePolicyStatement")
CreateSlot = Action("CreateSlot")
CreateSlotType = Action("CreateSlotType")
CreateSlotTypeVersion = Action("CreateSlotTypeVersion")
CreateTestSet = Action("CreateTestSet")
CreateTestSetDiscrepancyReport = Action("CreateTestSetDiscrepancyReport")
CreateUploadUrl = Action("CreateUploadUrl")
DeleteBot = Action("DeleteBot")
DeleteBotAlias = Action("DeleteBotAlias")
DeleteBotChannel = Action("DeleteBotChannel")
DeleteBotChannelAssociation = Action("DeleteBotChannelAssociation")
DeleteBotLocale = Action("DeleteBotLocale")
DeleteBotReplica = Action("DeleteBotReplica")
DeleteBotVersion = Action("DeleteBotVersion")
DeleteCustomVocabulary = Action("DeleteCustomVocabulary")
DeleteExport = Action("DeleteExport")
DeleteImport = Action("DeleteImport")
DeleteIntent = Action("DeleteIntent")
DeleteIntentVersion = Action("DeleteIntentVersion")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteResourcePolicyStatement = Action("DeleteResourcePolicyStatement")
DeleteSession = Action("DeleteSession")
DeleteSlot = Action("DeleteSlot")
DeleteSlotType = Action("DeleteSlotType")
DeleteSlotTypeVersion = Action("DeleteSlotTypeVersion")
DeleteTestSet = Action("DeleteTestSet")
DeleteUtterances = Action("DeleteUtterances")
DescribeBot = Action("DescribeBot")
DescribeBotAlias = Action("DescribeBotAlias")
DescribeBotChannel = Action("DescribeBotChannel")
DescribeBotLocale = Action("DescribeBotLocale")
DescribeBotRecommendation = Action("DescribeBotRecommendation")
DescribeBotReplica = Action("DescribeBotReplica")
DescribeBotResourceGeneration = Action("DescribeBotResourceGeneration")
DescribeBotVersion = Action("DescribeBotVersion")
DescribeCustomVocabulary = Action("DescribeCustomVocabulary")
DescribeCustomVocabularyMetadata = Action("DescribeCustomVocabularyMetadata")
DescribeExport = Action("DescribeExport")
DescribeImport = Action("DescribeImport")
DescribeIntent = Action("DescribeIntent")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeSlot = Action("DescribeSlot")
DescribeSlotType = Action("DescribeSlotType")
DescribeTestExecution = Action("DescribeTestExecution")
DescribeTestSet = Action("DescribeTestSet")
DescribeTestSetDiscrepancyReport = Action("DescribeTestSetDiscrepancyReport")
DescribeTestSetGeneration = Action("DescribeTestSetGeneration")
GenerateBotElement = Action("GenerateBotElement")
GetBot = Action("GetBot")
GetBotAlias = Action("GetBotAlias")
GetBotAliases = Action("GetBotAliases")
GetBotChannelAssociation = Action("GetBotChannelAssociation")
GetBotChannelAssociations = Action("GetBotChannelAssociations")
GetBotVersions = Action("GetBotVersions")
GetBots = Action("GetBots")
GetBuiltinIntent = Action("GetBuiltinIntent")
GetBuiltinIntents = Action("GetBuiltinIntents")
GetBuiltinSlotTypes = Action("GetBuiltinSlotTypes")
GetExport = Action("GetExport")
GetImport = Action("GetImport")
GetIntent = Action("GetIntent")
GetIntentVersions = Action("GetIntentVersions")
GetIntents = Action("GetIntents")
GetMigration = Action("GetMigration")
GetMigrations = Action("GetMigrations")
GetSession = Action("GetSession")
GetSlotType = Action("GetSlotType")
GetSlotTypeVersions = Action("GetSlotTypeVersions")
GetSlotTypes = Action("GetSlotTypes")
GetTestExecutionArtifactsUrl = Action("GetTestExecutionArtifactsUrl")
GetUtterancesView = Action("GetUtterancesView")
ListAggregatedUtterances = Action("ListAggregatedUtterances")
ListBotAliasReplicas = Action("ListBotAliasReplicas")
ListBotAliases = Action("ListBotAliases")
ListBotChannels = Action("ListBotChannels")
ListBotLocales = Action("ListBotLocales")
ListBotRecommendations = Action("ListBotRecommendations")
ListBotReplicas = Action("ListBotReplicas")
ListBotResourceGenerations = Action("ListBotResourceGenerations")
ListBotVersionReplicas = Action("ListBotVersionReplicas")
ListBotVersions = Action("ListBotVersions")
ListBots = Action("ListBots")
ListBuiltInIntents = Action("ListBuiltInIntents")
ListBuiltInSlotTypes = Action("ListBuiltInSlotTypes")
ListCustomVocabularyItems = Action("ListCustomVocabularyItems")
ListExports = Action("ListExports")
ListImports = Action("ListImports")
ListIntentMetrics = Action("ListIntentMetrics")
ListIntentPaths = Action("ListIntentPaths")
ListIntentStageMetrics = Action("ListIntentStageMetrics")
ListIntents = Action("ListIntents")
ListRecommendedIntents = Action("ListRecommendedIntents")
ListSessionAnalyticsData = Action("ListSessionAnalyticsData")
ListSessionMetrics = Action("ListSessionMetrics")
ListSlotTypes = Action("ListSlotTypes")
ListSlots = Action("ListSlots")
ListTagsForResource = Action("ListTagsForResource")
ListTestExecutionResultItems = Action("ListTestExecutionResultItems")
ListTestExecutions = Action("ListTestExecutions")
ListTestSetRecords = Action("ListTestSetRecords")
ListTestSets = Action("ListTestSets")
PostContent = Action("PostContent")
PostText = Action("PostText")
PutBot = Action("PutBot")
PutBotAlias = Action("PutBotAlias")
PutIntent = Action("PutIntent")
PutSession = Action("PutSession")
PutSlotType = Action("PutSlotType")
RecognizeSpeech = Action("RecognizeSpeech")
RecognizeText = Action("RecognizeText")
RecognizeUtterance = Action("RecognizeUtterance")
SearchAssociatedTranscripts = Action("SearchAssociatedTranscripts")
StartBotRecommendation = Action("StartBotRecommendation")
StartBotResourceGeneration = Action("StartBotResourceGeneration")
StartConversation = Action("StartConversation")
StartImport = Action("StartImport")
StartMigration = Action("StartMigration")
StartTestExecution = Action("StartTestExecution")
StartTestSetGeneration = Action("StartTestSetGeneration")
StopBotRecommendation = Action("StopBotRecommendation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBot = Action("UpdateBot")
UpdateBotAlias = Action("UpdateBotAlias")
UpdateBotLocale = Action("UpdateBotLocale")
UpdateBotRecommendation = Action("UpdateBotRecommendation")
UpdateCustomVocabulary = Action("UpdateCustomVocabulary")
UpdateExport = Action("UpdateExport")
UpdateIntent = Action("UpdateIntent")
UpdateResourcePolicy = Action("UpdateResourcePolicy")
UpdateSlot = Action("UpdateSlot")
UpdateSlotType = Action("UpdateSlotType")
UpdateTestSet = Action("UpdateTestSet")
