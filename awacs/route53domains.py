# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Route53 Domains'
prefix = 'route53domains'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CheckDomainAvailability = Action('CheckDomainAvailability')
DeleteDomain = Action('DeleteDomain')
DeleteTagsForDomain = Action('DeleteTagsForDomain')
DisableDomainAutoRenew = Action('DisableDomainAutoRenew')
DisableDomainTransferLock = Action('DisableDomainTransferLock')
EnableDomainAutoRenew = Action('EnableDomainAutoRenew')
EnableDomainTransferLock = Action('EnableDomainTransferLock')
GetContactReachabilityStatus = Action('GetContactReachabilityStatus')
GetDomainDetail = Action('GetDomainDetail')
GetDomainSuggestions = Action('GetDomainSuggestions')
GetOperationDetail = Action('GetOperationDetail')
ListDomains = Action('ListDomains')
ListOperations = Action('ListOperations')
ListTagsForDomain = Action('ListTagsForDomain')
RegisterDomain = Action('RegisterDomain')
RenewDomain = Action('RenewDomain')
ResendContactReachabilityEmail = Action('ResendContactReachabilityEmail')
RetrieveDomainAuthCode = Action('RetrieveDomainAuthCode')
TransferDomain = Action('TransferDomain')
UpdateDomainContact = Action('UpdateDomainContact')
UpdateDomainContactPrivacy = Action('UpdateDomainContactPrivacy')
UpdateDomainNameservers = Action('UpdateDomainNameservers')
UpdateTagsForDomain = Action('UpdateTagsForDomain')
ViewBilling = Action('ViewBilling')
