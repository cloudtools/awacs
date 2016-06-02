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


AddTags = Action('AddTags')
ApplySecurityGroupsToLoadBalancer = \
    Action('ApplySecurityGroupsToLoadBalancer')
AttachLoadBalancerToSubnets = Action('AttachLoadBalancerToSubnets')
ConfigureHealthCheck = Action('ConfigureHealthCheck')
CreateAppCookieStickinessPolicy = \
    Action('CreateAppCookieStickinessPolicy')
CreateLBCookieStickinessPolicy = Action('CreateLBCookieStickinessPolicy')
CreateLoadBalancer = Action('CreateLoadBalancer')
CreateLoadBalancerListeners = Action('CreateLoadBalancerListeners')
CreateLoadBalancerPolicy = Action('CreateLoadBalancerPolicy')
DeleteLoadBalancer = Action('DeleteLoadBalancer')
DeleteLoadBalancerListeners = Action('DeleteLoadBalancerListeners')
DeleteLoadBalancerPolicy = Action('DeleteLoadBalancerPolicy')
DeregisterInstancesFromLoadBalancer = \
    Action('DeregisterInstancesFromLoadBalancer')
DescribeInstanceHealth = Action('DescribeInstanceHealth')
DescribeLoadBalancerAttributes = Action('DescribeLoadBalancerAttributes')
DescribeLoadBalancerPolicyTypes = \
    Action('DescribeLoadBalancerPolicyTypes')
DescribeLoadBalancerPolicies = Action('DescribeLoadBalancerPolicies')
DescribeLoadBalancers = Action('DescribeLoadBalancers')
DescribeTags = Action('DescribeTags')
DetachLoadBalancerFromSubnets = Action('DetachLoadBalancerFromSubnets')
DisableAvailabilityZonesForLoadBalancer = \
    Action('DisableAvailabilityZonesForLoadBalancer')
EnableAvailabilityZonesForLoadBalancer = \
    Action('EnableAvailabilityZonesForLoadBalancer')
ModifyLoadBalancerAttributes = Action('ModifyLoadBalancerAttributes')
RemoveTags = Action('RemoveTags')
RegisterInstancesWithLoadBalancer = \
    Action('RegisterInstancesWithLoadBalancer')
SetLoadBalancerListenerSSLCertificate = \
    Action('SetLoadBalancerListenerSSLCertificate')
SetLoadBalancerPoliciesForBackendServer = \
    Action('SetLoadBalancerPoliciesForBackendServer')
SetLoadBalancerPoliciesOfListener = \
    Action('SetLoadBalancerPoliciesOfListener')
