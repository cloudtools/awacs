# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Lex'
prefix = 'lex'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateBotChannelAssociation = Action('CreateBotChannelAssociation')
CreateBotVersion = Action('CreateBotVersion')
CreateIntentVersion = Action('CreateIntentVersion')
CreateSlotTypeVersion = Action('CreateSlotTypeVersion')
DeleteBot = Action('DeleteBot')
DeleteBotAlias = Action('DeleteBotAlias')
DeleteBotChannelAssociation = Action('DeleteBotChannelAssociation')
DeleteIntent = Action('DeleteIntent')
DeleteSlotType = Action('DeleteSlotType')
DeleteUtterances = Action('DeleteUtterances')
GetBot = Action('GetBot')
GetBotAlias = Action('GetBotAlias')
GetBotAliases = Action('GetBotAliases')
GetBotChannelAssociation = Action('GetBotChannelAssociation')
GetBotChannelAssociations = Action('GetBotChannelAssociations')
GetBuiltinIntent = Action('GetBuiltinIntent')
GetBuiltinIntents = Action('GetBuiltinIntents')
GetBuiltinSlotTypes = Action('GetBuiltinSlotTypes')
GetBots = Action('GetBots')
GetBotVersions = Action('GetBotVersions')
GetIntent = Action('GetIntent')
GetIntents = Action('GetIntents')
GetIntentVersions = Action('GetIntentVersions')
GetSlotType = Action('GetSlotType')
GetSlotTypes = Action('GetSlotTypes')
GetSlotTypeVersions = Action('GetSlotTypeVersions')
GetUtterancesView = Action('GetUtterancesView')
PostContent = Action('PostContent')
PostText = Action('PostText')
PutBot = Action('PutBot')
PutBotAlias = Action('PutBotAlias')
PutIntent = Action('PutIntent')
PutSlotType = Action('PutSlotType')
