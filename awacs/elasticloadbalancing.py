# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Elastic Load Balancing'
prefix = 'elasticloadbalancing'

ConfigureHealthCheck = Action(prefix, 'ConfigureHealthCheck')
CreateAppCookieStickinessPolicy = \
    Action(prefix, 'CreateAppCookieStickinessPolicy')
CreateLBCookieStickinessPolicy = \
    Action(prefix, 'CreateLBCookieStickinessPolicy')
CreateLoadBalancer = Action(prefix, 'CreateLoadBalancer')
CreateLoadBalancerListeners = \
    Action(prefix, 'CreateLoadBalancerListeners')
DeleteLoadBalancer = Action(prefix, 'DeleteLoadBalancer')
DeleteLoadBalancerListeners = \
    Action(prefix, 'DeleteLoadBalancerListeners')
DeleteLoadBalancerPolicy = Action(prefix, 'DeleteLoadBalancerPolicy')
DeregisterInstancesFromLoadBalancer = \
    Action(prefix, 'DeregisterInstancesFromLoadBalancer')
DescribeInstanceHealth = Action(prefix, 'DescribeInstanceHealth')
DescribeLoadBalancers = Action(prefix, 'DescribeLoadBalancers')
DisableAvailabilityZonesForLoadBalancer = \
    Action(prefix, 'DisableAvailabilityZonesForLoadBalancer')
EnableAvailabilityZonesForLoadBalancer = \
    Action(prefix, 'EnableAvailabilityZonesForLoadBalancer')
RegisterInstancesWithLoadBalancer = \
    Action(prefix, 'RegisterInstancesWithLoadBalancer')
SetLoadBalancerListenerSSLCertificate = \
    Action(prefix, 'SetLoadBalancerListenerSSLCertificate')
SetLoadBalancerPoliciesOfListener = \
    Action(prefix, 'SetLoadBalancerPoliciesOfListener')
