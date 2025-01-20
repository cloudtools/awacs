# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elastic Load Balancing"
prefix = "elasticloadbalancing"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddListenerCertificates = Action("AddListenerCertificates")
AddTags = Action("AddTags")
AddTrustStoreRevocations = Action("AddTrustStoreRevocations")
ApplySecurityGroupsToLoadBalancer = Action("ApplySecurityGroupsToLoadBalancer")
AttachLoadBalancerToSubnets = Action("AttachLoadBalancerToSubnets")
ConfigureHealthCheck = Action("ConfigureHealthCheck")
CreateAppCookieStickinessPolicy = Action("CreateAppCookieStickinessPolicy")
CreateLBCookieStickinessPolicy = Action("CreateLBCookieStickinessPolicy")
CreateListener = Action("CreateListener")
CreateLoadBalancer = Action("CreateLoadBalancer")
CreateLoadBalancerListeners = Action("CreateLoadBalancerListeners")
CreateLoadBalancerPolicy = Action("CreateLoadBalancerPolicy")
CreateRule = Action("CreateRule")
CreateTargetGroup = Action("CreateTargetGroup")
CreateTrustStore = Action("CreateTrustStore")
DeleteListener = Action("DeleteListener")
DeleteLoadBalancer = Action("DeleteLoadBalancer")
DeleteLoadBalancerListeners = Action("DeleteLoadBalancerListeners")
DeleteLoadBalancerPolicy = Action("DeleteLoadBalancerPolicy")
DeleteRule = Action("DeleteRule")
DeleteSharedTrustStoreAssociation = Action("DeleteSharedTrustStoreAssociation")
DeleteTargetGroup = Action("DeleteTargetGroup")
DeleteTrustStore = Action("DeleteTrustStore")
DeregisterInstancesFromLoadBalancer = Action("DeregisterInstancesFromLoadBalancer")
DeregisterTargets = Action("DeregisterTargets")
DescribeAccountLimits = Action("DescribeAccountLimits")
DescribeCapacityReservation = Action("DescribeCapacityReservation")
DescribeInstanceHealth = Action("DescribeInstanceHealth")
DescribeListenerAttributes = Action("DescribeListenerAttributes")
DescribeListenerCertificates = Action("DescribeListenerCertificates")
DescribeListeners = Action("DescribeListeners")
DescribeLoadBalancerAttributes = Action("DescribeLoadBalancerAttributes")
DescribeLoadBalancerPolicies = Action("DescribeLoadBalancerPolicies")
DescribeLoadBalancerPolicyTypes = Action("DescribeLoadBalancerPolicyTypes")
DescribeLoadBalancers = Action("DescribeLoadBalancers")
DescribeRules = Action("DescribeRules")
DescribeSSLPolicies = Action("DescribeSSLPolicies")
DescribeTags = Action("DescribeTags")
DescribeTargetGroupAttributes = Action("DescribeTargetGroupAttributes")
DescribeTargetGroups = Action("DescribeTargetGroups")
DescribeTargetHealth = Action("DescribeTargetHealth")
DescribeTrustStoreAssociations = Action("DescribeTrustStoreAssociations")
DescribeTrustStoreRevocations = Action("DescribeTrustStoreRevocations")
DescribeTrustStores = Action("DescribeTrustStores")
DetachLoadBalancerFromSubnets = Action("DetachLoadBalancerFromSubnets")
DisableAvailabilityZonesForLoadBalancer = Action(
    "DisableAvailabilityZonesForLoadBalancer"
)
EnableAvailabilityZonesForLoadBalancer = Action(
    "EnableAvailabilityZonesForLoadBalancer"
)
GetResourcePolicy = Action("GetResourcePolicy")
GetTrustStoreCaCertificatesBundle = Action("GetTrustStoreCaCertificatesBundle")
GetTrustStoreRevocationContent = Action("GetTrustStoreRevocationContent")
ModifyCapacityReservation = Action("ModifyCapacityReservation")
ModifyListener = Action("ModifyListener")
ModifyListenerAttributes = Action("ModifyListenerAttributes")
ModifyLoadBalancerAttributes = Action("ModifyLoadBalancerAttributes")
ModifyRule = Action("ModifyRule")
ModifyTargetGroup = Action("ModifyTargetGroup")
ModifyTargetGroupAttributes = Action("ModifyTargetGroupAttributes")
ModifyTrustStore = Action("ModifyTrustStore")
RegisterInstancesWithLoadBalancer = Action("RegisterInstancesWithLoadBalancer")
RegisterTargets = Action("RegisterTargets")
RemoveListenerCertificates = Action("RemoveListenerCertificates")
RemoveTags = Action("RemoveTags")
RemoveTrustStoreRevocations = Action("RemoveTrustStoreRevocations")
SetIpAddressType = Action("SetIpAddressType")
SetLoadBalancerListenerSSLCertificate = Action("SetLoadBalancerListenerSSLCertificate")
SetLoadBalancerPoliciesForBackendServer = Action(
    "SetLoadBalancerPoliciesForBackendServer"
)
SetLoadBalancerPoliciesOfListener = Action("SetLoadBalancerPoliciesOfListener")
SetRulePriorities = Action("SetRulePriorities")
SetSecurityGroups = Action("SetSecurityGroups")
SetSubnets = Action("SetSubnets")
SetWebAcl = Action("SetWebAcl")
