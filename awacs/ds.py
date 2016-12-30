# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Directory Service'
prefix = 'ds'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddIpRoutes = Action('AddIpRoutes')
AddTagsToResource = Action('AddTagsToResource')
CancelSchemaExtension = Action('CancelSchemaExtension')
ConnectDirectory = Action('ConnectDirectory')
CreateAlias = Action('CreateAlias')
CreateComputer = Action('CreateComputer')
CreateConditionalForwarder = Action('CreateConditionalForwarder')
CreateDirectory = Action('CreateDirectory')
CreateMicrosoftAD = Action('CreateMicrosoftAD')
CreateSnapshot = Action('CreateSnapshot')
CreateTrust = Action('CreateTrust')
DeleteConditionalForwarder = Action('DeleteConditionalForwarder')
DeleteDirectory = Action('DeleteDirectory')
DeleteSnapshot = Action('DeleteSnapshot')
DeleteTrust = Action('DeleteTrust')
DeregisterEventTopic = Action('DeregisterEventTopic')
DescribeConditionalForwarders = Action('DescribeConditionalForwarders')
DescribeDirectories = Action('DescribeDirectories')
DescribeEventTopics = Action('DescribeEventTopics')
DescribeSnapshots = Action('DescribeSnapshots')
DescribeTrusts = Action('DescribeTrusts')
DisableRadius = Action('DisableRadius')
DisableSso = Action('DisableSso')
EnableRadius = Action('EnableRadius')
EnableSso = Action('EnableSso')
GetDirectoryLimits = Action('GetDirectoryLimits')
GetSnapshotLimits = Action('GetSnapshotLimits')
ListIpRoutes = Action('ListIpRoutes')
ListTagsForResource = Action('ListTagsForResource')
ListSchemaExtensions = Action('ListSchemaExtensions')
RegisterEventTopic = Action('RegisterEventTopic')
RemoveIpRoutes = Action('RemoveIpRoutes')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
RestoreFromSnapshot = Action('RestoreFromSnapshot')
StartSchemaExtension = Action('StartSchemaExtension')
UpdateConditionalForwarder = Action('UpdateConditionalForwarder')
UpdateRadius = Action('UpdateRadius')
VerifyTrust = Action('VerifyTrust')
