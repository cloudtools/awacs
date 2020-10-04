# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Elastic Load Balancing'
prefix = 'elasticloadbalancing'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddListenerCertificates = Action('AddListenerCertificates')
AddTags = Action('AddTags')
ApplySecurityGroupsToLoadBalancer = \
    Action('ApplySecurityGroupsToLoadBalancer')
AttachLoadBalancerToSubnets = Action('AttachLoadBalancerToSubnets')
ConfigureHealthCheck = Action('ConfigureHealthCheck')
CreateAppCookieStickinessPolicy = \
    Action('CreateAppCookieStickinessPolicy')
CreateLBCookieStickinessPolicy = Action('CreateLBCookieStickinessPolicy')
CreateListener = Action('CreateListener')
CreateLoadBalancer = Action('CreateLoadBalancer')
CreateLoadBalancerListeners = Action('CreateLoadBalancerListeners')
CreateLoadBalancerPolicy = Action('CreateLoadBalancerPolicy')
CreateRule = Action('CreateRule')
CreateTargetGroup = Action('CreateTargetGroup')
DeleteListener = Action('DeleteListener')
DeleteLoadBalancer = Action('DeleteLoadBalancer')
DeleteLoadBalancerListeners = Action('DeleteLoadBalancerListeners')
DeleteLoadBalancerPolicy = Action('DeleteLoadBalancerPolicy')
DeleteRule = Action('DeleteRule')
DeleteTargetGroup = Action('DeleteTargetGroup')
DeregisterInstancesFromLoadBalancer = \
    Action('DeregisterInstancesFromLoadBalancer')
DeregisterTargets = Action('DeregisterTargets')
DescribeAccountLimits = Action('DescribeAccountLimits')
DescribeInstanceHealth = Action('DescribeInstanceHealth')
DescribeListenerCertificates = Action('DescribeListenerCertificates')
DescribeListeners = Action('DescribeListeners')
DescribeLoadBalancerAttributes = Action('DescribeLoadBalancerAttributes')
DescribeLoadBalancerPolicies = Action('DescribeLoadBalancerPolicies')
DescribeLoadBalancerPolicyTypes = \
    Action('DescribeLoadBalancerPolicyTypes')
DescribeLoadBalancers = Action('DescribeLoadBalancers')
DescribeRules = Action('DescribeRules')
DescribeSSLPolicies = Action('DescribeSSLPolicies')
DescribeTags = Action('DescribeTags')
DescribeTargetGroupAttributes = Action('DescribeTargetGroupAttributes')
DescribeTargetGroups = Action('DescribeTargetGroups')
DescribeTargetHealth = Action('DescribeTargetHealth')
DetachLoadBalancerFromSubnets = Action('DetachLoadBalancerFromSubnets')
DisableAvailabilityZonesForLoadBalancer = \
    Action('DisableAvailabilityZonesForLoadBalancer')
EnableAvailabilityZonesForLoadBalancer = \
    Action('EnableAvailabilityZonesForLoadBalancer')
ModifyListener = Action('ModifyListener')
ModifyLoadBalancerAttributes = Action('ModifyLoadBalancerAttributes')
ModifyRule = Action('ModifyRule')
ModifyTargetGroup = Action('ModifyTargetGroup')
ModifyTargetGroupAttributes = Action('ModifyTargetGroupAttributes')
RegisterInstancesWithLoadBalancer = \
    Action('RegisterInstancesWithLoadBalancer')
RegisterTargets = Action('RegisterTargets')
RemoveListenerCertificates = Action('RemoveListenerCertificates')
RemoveTags = Action('RemoveTags')
SetIpAddressType = Action('SetIpAddressType')
SetLoadBalancerListenerSSLCertificate = \
    Action('SetLoadBalancerListenerSSLCertificate')
SetLoadBalancerPoliciesForBackendServer = \
    Action('SetLoadBalancerPoliciesForBackendServer')
SetLoadBalancerPoliciesOfListener = \
    Action('SetLoadBalancerPoliciesOfListener')
SetRulePriorities = Action('SetRulePriorities')
SetSecurityGroups = Action('SetSecurityGroups')
SetSubnets = Action('SetSubnets')
SetWebAcl = Action('SetWebAcl')
