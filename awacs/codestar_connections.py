# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeStar Connections'
prefix = 'codestar-connections'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateConnection = Action('CreateConnection')
CreateHost = Action('CreateHost')
DeleteConnection = Action('DeleteConnection')
DeleteHost = Action('DeleteHost')
GetConnection = Action('GetConnection')
GetHost = Action('GetHost')
GetIndividualAccessToken = Action('GetIndividualAccessToken')
GetInstallationUrl = Action('GetInstallationUrl')
ListConnections = Action('ListConnections')
ListHosts = Action('ListHosts')
ListInstallationTargets = Action('ListInstallationTargets')
ListTagsForResource = Action('ListTagsForResource')
PassConnection = Action('PassConnection')
RegisterAppCode = Action('RegisterAppCode')
StartAppRegistrationHandshake = Action('StartAppRegistrationHandshake')
StartOAuthHandshake = Action('StartOAuthHandshake')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateConnectionInstallation = Action('UpdateConnectionInstallation')
UpdateHost = Action('UpdateHost')
UseConnection = Action('UseConnection')
