# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53"
prefix = "route53"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateKeySigningKey = Action("ActivateKeySigningKey")
AssociateVPCWithHostedZone = Action("AssociateVPCWithHostedZone")
ChangeCidrCollection = Action("ChangeCidrCollection")
ChangeResourceRecordSets = Action("ChangeResourceRecordSets")
ChangeTagsForResource = Action("ChangeTagsForResource")
CreateCidrCollection = Action("CreateCidrCollection")
CreateHealthCheck = Action("CreateHealthCheck")
CreateHostedZone = Action("CreateHostedZone")
CreateKeySigningKey = Action("CreateKeySigningKey")
CreateQueryLoggingConfig = Action("CreateQueryLoggingConfig")
CreateReusableDelegationSet = Action("CreateReusableDelegationSet")
CreateTrafficPolicy = Action("CreateTrafficPolicy")
CreateTrafficPolicyInstance = Action("CreateTrafficPolicyInstance")
CreateTrafficPolicyVersion = Action("CreateTrafficPolicyVersion")
CreateVPCAssociationAuthorization = Action("CreateVPCAssociationAuthorization")
DeactivateKeySigningKey = Action("DeactivateKeySigningKey")
DeleteCidrCollection = Action("DeleteCidrCollection")
DeleteHealthCheck = Action("DeleteHealthCheck")
DeleteHostedZone = Action("DeleteHostedZone")
DeleteKeySigningKey = Action("DeleteKeySigningKey")
DeleteQueryLoggingConfig = Action("DeleteQueryLoggingConfig")
DeleteReusableDelegationSet = Action("DeleteReusableDelegationSet")
DeleteTrafficPolicy = Action("DeleteTrafficPolicy")
DeleteTrafficPolicyInstance = Action("DeleteTrafficPolicyInstance")
DeleteVPCAssociationAuthorization = Action("DeleteVPCAssociationAuthorization")
DisableDomainAutoRenew = Action("DisableDomainAutoRenew")
DisableHostedZoneDNSSEC = Action("DisableHostedZoneDNSSEC")
DisassociateVPCFromHostedZone = Action("DisassociateVPCFromHostedZone")
EnableDomainAutoRenew = Action("EnableDomainAutoRenew")
EnableHostedZoneDNSSEC = Action("EnableHostedZoneDNSSEC")
GetAccountLimit = Action("GetAccountLimit")
GetChange = Action("GetChange")
GetCheckerIpRanges = Action("GetCheckerIpRanges")
GetDNSSEC = Action("GetDNSSEC")
GetGeoLocation = Action("GetGeoLocation")
GetHealthCheck = Action("GetHealthCheck")
GetHealthCheckCount = Action("GetHealthCheckCount")
GetHealthCheckLastFailureReason = Action("GetHealthCheckLastFailureReason")
GetHealthCheckStatus = Action("GetHealthCheckStatus")
GetHostedZone = Action("GetHostedZone")
GetHostedZoneCount = Action("GetHostedZoneCount")
GetHostedZoneLimit = Action("GetHostedZoneLimit")
GetQueryLoggingConfig = Action("GetQueryLoggingConfig")
GetReusableDelegationSet = Action("GetReusableDelegationSet")
GetReusableDelegationSetLimit = Action("GetReusableDelegationSetLimit")
GetTrafficPolicy = Action("GetTrafficPolicy")
GetTrafficPolicyInstance = Action("GetTrafficPolicyInstance")
GetTrafficPolicyInstanceCount = Action("GetTrafficPolicyInstanceCount")
ListCidrBlocks = Action("ListCidrBlocks")
ListCidrCollections = Action("ListCidrCollections")
ListCidrLocations = Action("ListCidrLocations")
ListGeoLocations = Action("ListGeoLocations")
ListHealthChecks = Action("ListHealthChecks")
ListHostedZones = Action("ListHostedZones")
ListHostedZonesByName = Action("ListHostedZonesByName")
ListHostedZonesByVPC = Action("ListHostedZonesByVPC")
ListQueryLoggingConfigs = Action("ListQueryLoggingConfigs")
ListResourceRecordSets = Action("ListResourceRecordSets")
ListReusableDelegationSets = Action("ListReusableDelegationSets")
ListTagsForResource = Action("ListTagsForResource")
ListTagsForResources = Action("ListTagsForResources")
ListTrafficPolicies = Action("ListTrafficPolicies")
ListTrafficPolicyInstances = Action("ListTrafficPolicyInstances")
ListTrafficPolicyInstancesByHostedZone = Action(
    "ListTrafficPolicyInstancesByHostedZone"
)
ListTrafficPolicyInstancesByPolicy = Action("ListTrafficPolicyInstancesByPolicy")
ListTrafficPolicyVersions = Action("ListTrafficPolicyVersions")
ListVPCAssociationAuthorizations = Action("ListVPCAssociationAuthorizations")
TestDNSAnswer = Action("TestDNSAnswer")
UpdateHealthCheck = Action("UpdateHealthCheck")
UpdateHostedZoneComment = Action("UpdateHostedZoneComment")
UpdateTrafficPolicyComment = Action("UpdateTrafficPolicyComment")
UpdateTrafficPolicyInstance = Action("UpdateTrafficPolicyInstance")
