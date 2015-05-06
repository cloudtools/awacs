# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Route53 Domains'
prefix = 'route53domains'


class Route53DomainsAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


CheckDomainAvailability = Route53DomainsAction("CheckDomainAvailability")
DeleteTagsForDomain = Route53DomainsAction("DeleteTagsForDomain")
DisableDomainAutoRenew = Route53DomainsAction("DisableDomainAutoRenew")
DisableDomainTransferLock = Route53DomainsAction("DisableDomainTransferLock")
EnableDomainAutoRenew = Route53DomainsAction("EnableDomainAutoRenew")
EnableDomainTransferLock = Route53DomainsAction("EnableDomainTransferLock")
GetDomainDetail = Route53DomainsAction("GetDomainDetail")
GetOperationDetail = Route53DomainsAction("GetOperationDetail")
ListDomains = Route53DomainsAction("ListDomains")
ListOperations = Route53DomainsAction("ListOperations")
ListTagsForDomain = Route53DomainsAction("ListTagsForDomain")
RegisterDomain = Route53DomainsAction("RegisterDomain")
RetrieveDomainAuthCode = Route53DomainsAction("RetrieveDomainAuthCode")
TransferDomain = Route53DomainsAction("TransferDomain")
UpdateDomainContact = Route53DomainsAction("UpdateDomainContact")
UpdateDomainContactPrivacy = Route53DomainsAction("UpdateDomainContactPrivacy")
UpdateDomainNameservers = Route53DomainsAction("UpdateDomainNameservers")
UpdateTagsForDomains = Route53DomainsAction("UpdateTagsForDomains")
