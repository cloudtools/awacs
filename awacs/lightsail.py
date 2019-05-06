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
AttachDisk = Action('AttachDisk')
AttachInstancesToLoadBalancer = Action('AttachInstancesToLoadBalancer')
AttachLoadBalancerTlsCertificate = \
    Action('AttachLoadBalancerTlsCertificate')
AttachStaticIp = Action('AttachStaticIp')
CloseInstancePublicPorts = Action('CloseInstancePublicPorts')
CopySnapshot = Action('CopySnapshot')
CreateCloudFormationStack = Action('CreateCloudFormationStack')
CreateDisk = Action('CreateDisk')
CreateDiskFromSnapshot = Action('CreateDiskFromSnapshot')
CreateDiskSnapshot = Action('CreateDiskSnapshot')
CreateDomain = Action('CreateDomain')
CreateDomainEntry = Action('CreateDomainEntry')
CreateInstanceSnapshot = Action('CreateInstanceSnapshot')
CreateInstances = Action('CreateInstances')
CreateInstancesFromSnapshot = Action('CreateInstancesFromSnapshot')
CreateKeyPair = Action('CreateKeyPair')
CreateLoadBalancer = Action('CreateLoadBalancer')
CreateLoadBalancerTlsCertificate = \
    Action('CreateLoadBalancerTlsCertificate')
CreateRelationalDatabase = Action('CreateRelationalDatabase')
CreateRelationalDatabaseFromSnapshot = \
    Action('CreateRelationalDatabaseFromSnapshot')
CreateRelationalDatabaseSnapshot = \
    Action('CreateRelationalDatabaseSnapshot')
DeleteDisk = Action('DeleteDisk')
DeleteDiskSnapshot = Action('DeleteDiskSnapshot')
DeleteDomain = Action('DeleteDomain')
DeleteDomainEntry = Action('DeleteDomainEntry')
DeleteInstance = Action('DeleteInstance')
DeleteInstanceSnapshot = Action('DeleteInstanceSnapshot')
DeleteKeyPair = Action('DeleteKeyPair')
DeleteKnownHostKeys = Action('DeleteKnownHostKeys')
DeleteLoadBalancer = Action('DeleteLoadBalancer')
DeleteLoadBalancerTlsCertificate = \
    Action('DeleteLoadBalancerTlsCertificate')
DeleteRelationalDatabase = Action('DeleteRelationalDatabase')
DeleteRelationalDatabaseSnapshot = \
    Action('DeleteRelationalDatabaseSnapshot')
DetachDisk = Action('DetachDisk')
DetachInstancesFromLoadBalancer = \
    Action('DetachInstancesFromLoadBalancer')
DetachStaticIp = Action('DetachStaticIp')
DownloadDefaultKeyPair = Action('DownloadDefaultKeyPair')
ExportSnapshot = Action('ExportSnapshot')
GetActiveNames = Action('GetActiveNames')
GetBlueprints = Action('GetBlueprints')
GetBundles = Action('GetBundles')
GetCloudFormationStackRecords = Action('GetCloudFormationStackRecords')
GetDisk = Action('GetDisk')
GetDiskSnapshot = Action('GetDiskSnapshot')
GetDiskSnapshots = Action('GetDiskSnapshots')
GetDisks = Action('GetDisks')
GetDomain = Action('GetDomain')
GetDomains = Action('GetDomains')
GetExportSnapshotRecords = Action('GetExportSnapshotRecords')
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
GetLoadBalancer = Action('GetLoadBalancer')
GetLoadBalancerMetricData = Action('GetLoadBalancerMetricData')
GetLoadBalancerTlsCertificates = Action('GetLoadBalancerTlsCertificates')
GetLoadBalancers = Action('GetLoadBalancers')
GetOperation = Action('GetOperation')
GetOperations = Action('GetOperations')
GetOperationsForResource = Action('GetOperationsForResource')
GetRegions = Action('GetRegions')
GetRelationalDatabase = Action('GetRelationalDatabase')
GetRelationalDatabaseBlueprints = \
    Action('GetRelationalDatabaseBlueprints')
GetRelationalDatabaseBundles = Action('GetRelationalDatabaseBundles')
GetRelationalDatabaseEvents = Action('GetRelationalDatabaseEvents')
GetRelationalDatabaseLogEvents = Action('GetRelationalDatabaseLogEvents')
GetRelationalDatabaseLogStreams = \
    Action('GetRelationalDatabaseLogStreams')
GetRelationalDatabaseMasterUserPassword = \
    Action('GetRelationalDatabaseMasterUserPassword')
GetRelationalDatabaseMetricData = \
    Action('GetRelationalDatabaseMetricData')
GetRelationalDatabaseParameters = \
    Action('GetRelationalDatabaseParameters')
GetRelationalDatabaseSnapshot = Action('GetRelationalDatabaseSnapshot')
GetRelationalDatabaseSnapshots = Action('GetRelationalDatabaseSnapshots')
GetRelationalDatabases = Action('GetRelationalDatabases')
GetStaticIp = Action('GetStaticIp')
GetStaticIps = Action('GetStaticIps')
ImportKeyPair = Action('ImportKeyPair')
IsVpcPeered = Action('IsVpcPeered')
OpenInstancePublicPorts = Action('OpenInstancePublicPorts')
PeerVpc = Action('PeerVpc')
PutInstancePublicPorts = Action('PutInstancePublicPorts')
RebootInstance = Action('RebootInstance')
RebootRelationalDatabase = Action('RebootRelationalDatabase')
ReleaseStaticIp = Action('ReleaseStaticIp')
StartInstance = Action('StartInstance')
StartRelationalDatabase = Action('StartRelationalDatabase')
StopInstance = Action('StopInstance')
StopRelationalDatabase = Action('StopRelationalDatabase')
TagResource = Action('TagResource')
UnpeerVpc = Action('UnpeerVpc')
UntagResource = Action('UntagResource')
UpdateDomainEntry = Action('UpdateDomainEntry')
UpdateLoadBalancerAttribute = Action('UpdateLoadBalancerAttribute')
UpdateRelationalDatabase = Action('UpdateRelationalDatabase')
UpdateRelationalDatabaseParameters = \
    Action('UpdateRelationalDatabaseParameters')
