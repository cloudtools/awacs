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


CreateBotVersion = Action('CreateBotVersion')
CreateIntentVersion = Action('CreateIntentVersion')
CreateSlotTypeVersion = Action('CreateSlotTypeVersion')
DeleteBot = Action('DeleteBot')
DeleteBotAlias = Action('DeleteBotAlias')
DeleteBotChannelAssociation = Action('DeleteBotChannelAssociation')
DeleteBotVersion = Action('DeleteBotVersion')
DeleteIntent = Action('DeleteIntent')
DeleteIntentVersion = Action('DeleteIntentVersion')
DeleteSlotType = Action('DeleteSlotType')
DeleteSlotTypeVersion = Action('DeleteSlotTypeVersion')
DeleteUtterances = Action('DeleteUtterances')
GetBot = Action('GetBot')
GetBotAlias = Action('GetBotAlias')
GetBotAliases = Action('GetBotAliases')
GetBotChannelAssociation = Action('GetBotChannelAssociation')
GetBotChannelAssociations = Action('GetBotChannelAssociations')
GetBotVersions = Action('GetBotVersions')
GetBots = Action('GetBots')
GetBuiltinIntent = Action('GetBuiltinIntent')
GetBuiltinIntents = Action('GetBuiltinIntents')
GetBuiltinSlotTypes = Action('GetBuiltinSlotTypes')
GetIntent = Action('GetIntent')
GetIntentVersions = Action('GetIntentVersions')
GetIntents = Action('GetIntents')
GetSlotType = Action('GetSlotType')
GetSlotTypeVersions = Action('GetSlotTypeVersions')
GetSlotTypes = Action('GetSlotTypes')
GetUtterancesView = Action('GetUtterancesView')
PostContent = Action('PostContent')
PostText = Action('PostText')
PutBot = Action('PutBot')
PutBotAlias = Action('PutBotAlias')
PutIntent = Action('PutIntent')
PutSlotType = Action('PutSlotType')
