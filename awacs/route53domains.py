# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Route53 Domains'
prefix = 'route53domains'

CheckDomainAvailability = Action(prefix, 'CheckDomainAvailability')
DeleteDomain = Action(prefix, 'DeleteDomain')
DisableDomainTransferLock = Action(prefix, 'DisableDomainTransferLock')
EnableDomainTransferLock = Action(prefix, 'EnableDomainTransferLock')
GetDomainDetail = Action(prefix, 'GetDomainDetail')
GetOperationDetail = Action(prefix, 'GetOperationDetail')
ListDomains = Action(prefix, 'ListDomains')
ListOperations = Action(prefix, 'ListOperations')
RegisterDomain = Action(prefix, 'RegisterDomain')
RetrieveDomainAuthCode = Action(prefix, 'RetrieveDomainAuthCode')
TransferDomain = Action(prefix, 'TransferDomain')
UpdateDomainContact = Action(prefix, 'UpdateDomainContact')
UpdateDomainContactPrivacy = \
    Action(prefix, 'UpdateDomainContactPrivacy')
UpdateDomainNameservers = Action(prefix, 'UpdateDomainNameservers')
