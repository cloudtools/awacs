# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, BaseARN

service_name = 'Elastic Load Balancing'
prefix = 'elasticloadbalancing'


class ARN(BaseARN):
    def __init__(self, resource="*", region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class ELBAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


AddTags = ELBAction('AddTags')
ApplySecurityGroupsToLoadBalancer = \
    ELBAction('ApplySecurityGroupsToLoadBalancer')
AttachLoadBalancerToSubnets = \
    ELBAction('AttachLoadBalancerToSubnets')
ConfigureHealthCheck = ELBAction('ConfigureHealthCheck')
CreateAppCookieStickinessPolicy = \
    ELBAction('CreateAppCookieStickinessPolicy')
CreateLBCookieStickinessPolicy = \
    ELBAction('CreateLBCookieStickinessPolicy')
CreateLoadBalancer = ELBAction('CreateLoadBalancer')
CreateLoadBalancerListeners = \
    ELBAction('CreateLoadBalancerListeners')
CreateLoadBalancerPolicy = ELBAction('CreateLoadBalancerPolicy')
DeleteLoadBalancer = ELBAction('DeleteLoadBalancer')
DeleteLoadBalancerListeners = \
    ELBAction('DeleteLoadBalancerListeners')
DeleteLoadBalancerPolicy = ELBAction('DeleteLoadBalancerPolicy')
DeregisterInstancesFromLoadBalancer = \
    ELBAction('DeregisterInstancesFromLoadBalancer')
DescribeInstanceHealth = ELBAction('DescribeInstanceHealth')
DescribeLoadBalancerAttributes = \
    ELBAction('DescribeLoadBalancerAttributes')
DescribeLoadBalancerPolicyTypes = \
    ELBAction('DescribeLoadBalancerPolicyTypes')
DescribeLoadBalancerPolicies = \
    ELBAction('DescribeLoadBalancerPolicies')
DescribeLoadBalancers = ELBAction('DescribeLoadBalancers')
DescribeTags = ELBAction('DescribeTags')
DetachLoadBalancerFromSubnets = \
    ELBAction('DetachLoadBalancerFromSubnets')
DisableAvailabilityZonesForLoadBalancer = \
    ELBAction('DisableAvailabilityZonesForLoadBalancer')
EnableAvailabilityZonesForLoadBalancer = \
    ELBAction('EnableAvailabilityZonesForLoadBalancer')
ModifyLoadBalancerAttributes = \
    ELBAction('ModifyLoadBalancerAttributes')
RemoveTags = ELBAction('RemoveTags')
RegisterInstancesWithLoadBalancer = \
    ELBAction('RegisterInstancesWithLoadBalancer')
SetLoadBalancerListenerSSLCertificate = \
    ELBAction('SetLoadBalancerListenerSSLCertificate')
SetLoadBalancerPoliciesForBackendServer = \
    ELBAction('SetLoadBalancerPoliciesForBackendServer')
SetLoadBalancerPoliciesOfListener = \
    ELBAction('SetLoadBalancerPoliciesOfListener')
