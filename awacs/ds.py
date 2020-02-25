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


AcceptSharedDirectory = Action('AcceptSharedDirectory')
AddIpRoutes = Action('AddIpRoutes')
AddTagsToResource = Action('AddTagsToResource')
AuthorizeApplication = Action('AuthorizeApplication')
CancelSchemaExtension = Action('CancelSchemaExtension')
CheckAlias = Action('CheckAlias')
ConnectDirectory = Action('ConnectDirectory')
CreateAlias = Action('CreateAlias')
CreateComputer = Action('CreateComputer')
CreateConditionalForwarder = Action('CreateConditionalForwarder')
CreateDirectory = Action('CreateDirectory')
CreateIdentityPoolDirectory = Action('CreateIdentityPoolDirectory')
CreateLogSubscription = Action('CreateLogSubscription')
CreateMicrosoftAD = Action('CreateMicrosoftAD')
CreateSnapshot = Action('CreateSnapshot')
CreateTrust = Action('CreateTrust')
DeleteConditionalForwarder = Action('DeleteConditionalForwarder')
DeleteDirectory = Action('DeleteDirectory')
DeleteLogSubscription = Action('DeleteLogSubscription')
DeleteSnapshot = Action('DeleteSnapshot')
DeleteTrust = Action('DeleteTrust')
DeregisterCertificate = Action('DeregisterCertificate')
DeregisterEventTopic = Action('DeregisterEventTopic')
DescribeCertificate = Action('DescribeCertificate')
DescribeConditionalForwarders = Action('DescribeConditionalForwarders')
DescribeDirectories = Action('DescribeDirectories')
DescribeDomainControllers = Action('DescribeDomainControllers')
DescribeEventTopics = Action('DescribeEventTopics')
DescribeLDAPSSettings = Action('DescribeLDAPSSettings')
DescribeSharedDirectories = Action('DescribeSharedDirectories')
DescribeSnapshots = Action('DescribeSnapshots')
DescribeTrusts = Action('DescribeTrusts')
DisableLDAPS = Action('DisableLDAPS')
DisableRadius = Action('DisableRadius')
DisableSso = Action('DisableSso')
EnableLDAPS = Action('EnableLDAPS')
EnableRadius = Action('EnableRadius')
EnableSso = Action('EnableSso')
GetAuthorizedApplicationDetails = \
    Action('GetAuthorizedApplicationDetails')
GetDirectoryLimits = Action('GetDirectoryLimits')
GetSnapshotLimits = Action('GetSnapshotLimits')
ListAuthorizedApplications = Action('ListAuthorizedApplications')
ListCertificates = Action('ListCertificates')
ListIpRoutes = Action('ListIpRoutes')
ListLogSubscriptions = Action('ListLogSubscriptions')
ListSchemaExtensions = Action('ListSchemaExtensions')
ListTagsForResource = Action('ListTagsForResource')
RegisterCertificate = Action('RegisterCertificate')
RegisterEventTopic = Action('RegisterEventTopic')
RejectSharedDirectory = Action('RejectSharedDirectory')
RemoveIpRoutes = Action('RemoveIpRoutes')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
ResetUserPassword = Action('ResetUserPassword')
RestoreFromSnapshot = Action('RestoreFromSnapshot')
ShareDirectory = Action('ShareDirectory')
StartSchemaExtension = Action('StartSchemaExtension')
UnauthorizeApplication = Action('UnauthorizeApplication')
UnshareDirectory = Action('UnshareDirectory')
UpdateConditionalForwarder = Action('UpdateConditionalForwarder')
UpdateNumberOfDomainControllers = \
    Action('UpdateNumberOfDomainControllers')
UpdateRadius = Action('UpdateRadius')
UpdateTrust = Action('UpdateTrust')
VerifyTrust = Action('VerifyTrust')
