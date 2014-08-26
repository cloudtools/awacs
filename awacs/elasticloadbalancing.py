# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Elastic Load Balancing'
prefix = 'elasticloadbalancing'

AddTags = Action(prefix, 'AddTags')
ApplySecurityGroupsToLoadBalancer = \
    Action(prefix, 'ApplySecurityGroupsToLoadBalancer')
AttachLoadBalancerToSubnets = \
    Action(prefix, 'AttachLoadBalancerToSubnets')
ConfigureHealthCheck = Action(prefix, 'ConfigureHealthCheck')
CreateAppCookieStickinessPolicy = \
    Action(prefix, 'CreateAppCookieStickinessPolicy')
CreateLBCookieStickinessPolicy = \
    Action(prefix, 'CreateLBCookieStickinessPolicy')
CreateLoadBalancer = Action(prefix, 'CreateLoadBalancer')
CreateLoadBalancerListeners = \
    Action(prefix, 'CreateLoadBalancerListeners')
CreateLoadBalancerPolicy = Action(prefix, 'CreateLoadBalancerPolicy')
DeleteLoadBalancer = Action(prefix, 'DeleteLoadBalancer')
DeleteLoadBalancerListeners = \
    Action(prefix, 'DeleteLoadBalancerListeners')
DeleteLoadBalancerPolicy = Action(prefix, 'DeleteLoadBalancerPolicy')
DeregisterInstancesFromLoadBalancer = \
    Action(prefix, 'DeregisterInstancesFromLoadBalancer')
DescribeInstanceHealth = Action(prefix, 'DescribeInstanceHealth')
DescribeLoadBalancerAttributes = \
    Action(prefix, 'DescribeLoadBalancerAttributes')
DescribeLoadBalancerPolicyTypes = \
    Action(prefix, 'DescribeLoadBalancerPolicyTypes')
DescribeLoadBalancerPolicies = \
    Action(prefix, 'DescribeLoadBalancerPolicies')
DescribeLoadBalancers = Action(prefix, 'DescribeLoadBalancers')
DescribeTags = Action(prefix, 'DescribeTags')
DetachLoadBalancerFromSubnets = \
    Action(prefix, 'DetachLoadBalancerFromSubnets')
DisableAvailabilityZonesForLoadBalancer = \
    Action(prefix, 'DisableAvailabilityZonesForLoadBalancer')
EnableAvailabilityZonesForLoadBalancer = \
    Action(prefix, 'EnableAvailabilityZonesForLoadBalancer')
ModifyLoadBalancerAttributes = \
    Action(prefix, 'ModifyLoadBalancerAttributes')
RemoveTags = Action(prefix, 'RemoveTags')
RegisterInstancesWithLoadBalancer = \
    Action(prefix, 'RegisterInstancesWithLoadBalancer')
SetLoadBalancerListenerSSLCertificate = \
    Action(prefix, 'SetLoadBalancerListenerSSLCertificate')
SetLoadBalancerPoliciesForBackendServer = \
    Action(prefix, 'SetLoadBalancerPoliciesForBackendServer')
SetLoadBalancerPoliciesOfListener = \
    Action(prefix, 'SetLoadBalancerPoliciesOfListener')
