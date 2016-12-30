# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Lightsail'
prefix = 'lightsail'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AllocateStaticIp = Action('AllocateStaticIp')
AttachStaticIp = Action('AttachStaticIp')
CloseInstancePublicPorts = Action('CloseInstancePublicPorts')
CreateDomain = Action('CreateDomain')
CreateDomainEntry = Action('CreateDomainEntry')
CreateInstanceSnapshot = Action('CreateInstanceSnapshot')
CreateInstances = Action('CreateInstances')
CreateInstancesFromSnapshot = Action('CreateInstancesFromSnapshot')
CreateKeyPair = Action('CreateKeyPair')
DeleteDomain = Action('DeleteDomain')
DeleteDomainEntry = Action('DeleteDomainEntry')
DeleteInstance = Action('DeleteInstance')
DeleteInstanceSnapshot = Action('DeleteInstanceSnapshot')
DeleteKeyPair = Action('DeleteKeyPair')
DetachStaticIp = Action('DetachStaticIp')
DownloadDefaultKeyPair = Action('DownloadDefaultKeyPair')
GetActiveNames = Action('GetActiveNames')
GetBlueprints = Action('GetBlueprints')
GetBundles = Action('GetBundles')
GetDomain = Action('GetDomain')
GetDomains = Action('GetDomains')
GetInstance = Action('GetInstance')
GetInstanceAccessDetails = Action('GetInstanceAccessDetails')
GetInstanceMetricData = Action('GetInstanceMetricData')
GetInstancePortStates = Action('GetInstancePortStates')
GetInstanceSnapshot = Action('GetInstanceSnapshot')
GetInstanceSnapshots = Action('GetInstanceSnapshots')
GetInstanceState = Action('GetInstanceState')
GetInstances = Action('GetInstances')
GetKeyPair = Action('GetKeyPair')
GetKeyPairs = Action('GetKeyPairs')
GetOperation = Action('GetOperation')
GetOperations = Action('GetOperations')
GetOperationsForResource = Action('GetOperationsForResource')
GetRegions = Action('GetRegions')
GetStaticIp = Action('GetStaticIp')
GetStaticIps = Action('GetStaticIps')
ImportKeyPair = Action('ImportKeyPair')
IsVpcPeered = Action('IsVpcPeered')
OpenInstancePublicPorts = Action('OpenInstancePublicPorts')
PeerVpc = Action('PeerVpc')
RebootInstance = Action('RebootInstance')
ReleaseStaticIp = Action('ReleaseStaticIp')
StartInstance = Action('StartInstance')
StopInstance = Action('StopInstance')
UnpeerVpc = Action('UnpeerVpc')
UpdateDomainEntry = Action('UpdateDomainEntry')
