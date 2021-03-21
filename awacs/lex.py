# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lex"
prefix = "lex"


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource="", region="", account=""):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region, account=account)


BuildBotLocale = Action("BuildBotLocale")
CreateBot = Action("CreateBot")
CreateBotAlias = Action("CreateBotAlias")
CreateBotChannel = Action("CreateBotChannel")
CreateBotLocale = Action("CreateBotLocale")
CreateBotVersion = Action("CreateBotVersion")
CreateIntent = Action("CreateIntent")
CreateIntentVersion = Action("CreateIntentVersion")
CreateSlot = Action("CreateSlot")
CreateSlotType = Action("CreateSlotType")
CreateSlotTypeVersion = Action("CreateSlotTypeVersion")
DeleteBot = Action("DeleteBot")
DeleteBotAlias = Action("DeleteBotAlias")
DeleteBotChannel = Action("DeleteBotChannel")
DeleteBotChannelAssociation = Action("DeleteBotChannelAssociation")
DeleteBotLocale = Action("DeleteBotLocale")
DeleteBotVersion = Action("DeleteBotVersion")
DeleteIntent = Action("DeleteIntent")
DeleteIntentVersion = Action("DeleteIntentVersion")
DeleteSession = Action("DeleteSession")
DeleteSlot = Action("DeleteSlot")
DeleteSlotType = Action("DeleteSlotType")
DeleteSlotTypeVersion = Action("DeleteSlotTypeVersion")
DeleteUtterances = Action("DeleteUtterances")
DescribeBot = Action("DescribeBot")
DescribeBotAlias = Action("DescribeBotAlias")
DescribeBotChannel = Action("DescribeBotChannel")
DescribeBotLocale = Action("DescribeBotLocale")
DescribeBotVersion = Action("DescribeBotVersion")
DescribeIntent = Action("DescribeIntent")
DescribeSlot = Action("DescribeSlot")
DescribeSlotType = Action("DescribeSlotType")
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
GetSession = Action("GetSession")
GetSlotType = Action("GetSlotType")
GetSlotTypeVersions = Action("GetSlotTypeVersions")
GetSlotTypes = Action("GetSlotTypes")
GetUtterancesView = Action("GetUtterancesView")
ListBotAliases = Action("ListBotAliases")
ListBotChannels = Action("ListBotChannels")
ListBotLocales = Action("ListBotLocales")
ListBotVersions = Action("ListBotVersions")
ListBots = Action("ListBots")
ListIntents = Action("ListIntents")
ListSlotTypes = Action("ListSlotTypes")
ListSlots = Action("ListSlots")
ListTagsForResource = Action("ListTagsForResource")
PostContent = Action("PostContent")
PostText = Action("PostText")
PutBot = Action("PutBot")
PutBotAlias = Action("PutBotAlias")
PutIntent = Action("PutIntent")
PutSession = Action("PutSession")
PutSlotType = Action("PutSlotType")
RecognizeSpeech = Action("RecognizeSpeech")
RecognizeText = Action("RecognizeText")
StartConversation = Action("StartConversation")
StartImport = Action("StartImport")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBot = Action("UpdateBot")
UpdateBotAlias = Action("UpdateBotAlias")
UpdateBotLocale = Action("UpdateBotLocale")
UpdateIntent = Action("UpdateIntent")
UpdateSlot = Action("UpdateSlot")
UpdateSlotType = Action("UpdateSlotType")
