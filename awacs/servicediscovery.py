# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Cloud Map'
prefix = 'servicediscovery'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateHttpNamespace = Action('CreateHttpNamespace')
CreatePrivateDnsNamespace = Action('CreatePrivateDnsNamespace')
CreatePublicDnsNamespace = Action('CreatePublicDnsNamespace')
CreateService = Action('CreateService')
DeleteNamespace = Action('DeleteNamespace')
DeleteService = Action('DeleteService')
DeregisterInstance = Action('DeregisterInstance')
DiscoverInstances = Action('DiscoverInstances')
GetInstance = Action('GetInstance')
GetInstancesHealthStatus = Action('GetInstancesHealthStatus')
GetNamespace = Action('GetNamespace')
GetOperation = Action('GetOperation')
GetService = Action('GetService')
ListInstances = Action('ListInstances')
ListNamespaces = Action('ListNamespaces')
ListOperations = Action('ListOperations')
ListServices = Action('ListServices')
ListTagsForResource = Action('ListTagsForResource')
RegisterInstance = Action('RegisterInstance')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateInstanceCustomHealthStatus = \
    Action('UpdateInstanceCustomHealthStatus')
UpdateInstanceHeartbeatStatus = Action('UpdateInstanceHeartbeatStatus')
UpdateService = Action('UpdateService')
