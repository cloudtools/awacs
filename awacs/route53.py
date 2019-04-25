# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Route 53'
prefix = 'route53'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateVPCWithHostedZone = Action('AssociateVPCWithHostedZone')
ChangeResourceRecordSets = Action('ChangeResourceRecordSets')
ChangeTagsForResource = Action('ChangeTagsForResource')
CreateHealthCheck = Action('CreateHealthCheck')
CreateHostedZone = Action('CreateHostedZone')
CreateQueryLoggingConfig = Action('CreateQueryLoggingConfig')
CreateReusableDelegationSet = Action('CreateReusableDelegationSet')
CreateTrafficPolicy = Action('CreateTrafficPolicy')
CreateTrafficPolicyInstance = Action('CreateTrafficPolicyInstance')
CreateTrafficPolicyVersion = Action('CreateTrafficPolicyVersion')
CreateVPCAssociationAuthorization = \
    Action('CreateVPCAssociationAuthorization')
DeleteHealthCheck = Action('DeleteHealthCheck')
DeleteHostedZone = Action('DeleteHostedZone')
DeleteQueryLoggingConfig = Action('DeleteQueryLoggingConfig')
DeleteReusableDelegationSet = Action('DeleteReusableDelegationSet')
DeleteTrafficPolicy = Action('DeleteTrafficPolicy')
DeleteTrafficPolicyInstance = Action('DeleteTrafficPolicyInstance')
DeleteVPCAssociationAuthorization = \
    Action('DeleteVPCAssociationAuthorization')
DisableDomainAutoRenew = Action('DisableDomainAutoRenew')
DisassociateVPCFromHostedZone = Action('DisassociateVPCFromHostedZone')
EnableDomainAutoRenew = Action('EnableDomainAutoRenew')
GetAccountLimit = Action('GetAccountLimit')
GetChange = Action('GetChange')
GetCheckerIpRanges = Action('GetCheckerIpRanges')
GetGeoLocation = Action('GetGeoLocation')
GetHealthCheck = Action('GetHealthCheck')
GetHealthCheckCount = Action('GetHealthCheckCount')
GetHealthCheckLastFailureReason = \
    Action('GetHealthCheckLastFailureReason')
GetHealthCheckStatus = Action('GetHealthCheckStatus')
GetHostedZone = Action('GetHostedZone')
GetHostedZoneCount = Action('GetHostedZoneCount')
GetHostedZoneLimit = Action('GetHostedZoneLimit')
GetQueryLoggingConfig = Action('GetQueryLoggingConfig')
GetReusableDelegationSet = Action('GetReusableDelegationSet')
GetReusableDelegationSetLimit = Action('GetReusableDelegationSetLimit')
GetTrafficPolicy = Action('GetTrafficPolicy')
GetTrafficPolicyInstance = Action('GetTrafficPolicyInstance')
GetTrafficPolicyInstanceCount = Action('GetTrafficPolicyInstanceCount')
ListGeoLocations = Action('ListGeoLocations')
ListHealthChecks = Action('ListHealthChecks')
ListHostedZones = Action('ListHostedZones')
ListHostedZonesByName = Action('ListHostedZonesByName')
ListQueryLoggingConfigs = Action('ListQueryLoggingConfigs')
ListResourceRecordSets = Action('ListResourceRecordSets')
ListReusableDelegationSets = Action('ListReusableDelegationSets')
ListTagsForResource = Action('ListTagsForResource')
ListTagsForResources = Action('ListTagsForResources')
ListTrafficPolicies = Action('ListTrafficPolicies')
ListTrafficPolicyInstances = Action('ListTrafficPolicyInstances')
ListTrafficPolicyInstancesByHostedZone = \
    Action('ListTrafficPolicyInstancesByHostedZone')
ListTrafficPolicyInstancesByPolicy = \
    Action('ListTrafficPolicyInstancesByPolicy')
ListTrafficPolicyVersions = Action('ListTrafficPolicyVersions')
ListVPCAssociationAuthorizations = \
    Action('ListVPCAssociationAuthorizations')
TestDNSAnswer = Action('TestDNSAnswer')
UpdateHealthCheck = Action('UpdateHealthCheck')
UpdateHostedZoneComment = Action('UpdateHostedZoneComment')
UpdateTrafficPolicyComment = Action('UpdateTrafficPolicyComment')
UpdateTrafficPolicyInstance = Action('UpdateTrafficPolicyInstance')
