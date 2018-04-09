# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Storage Gateway'
prefix = 'storagegateway'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ActivateGateway = Action('ActivateGateway')
AddCache = Action('AddCache')
AddTagsToResource = Action('AddTagsToResource')
AddUploadBuffer = Action('AddUploadBuffer')
AddWorkingStorage = Action('AddWorkingStorage')
CancelArchival = Action('CancelArchival')
CancelRetrieval = Action('CancelRetrieval')
CreateCachediSCSIVolume = Action('CreateCachediSCSIVolume')
CreateNFSFileShare = Action('CreateNFSFileShare')
CreateSnapshot = Action('CreateSnapshot')
CreateSnapshotFromVolumeRecoveryPoint = \
    Action('CreateSnapshotFromVolumeRecoveryPoint')
CreateStorediSCSIVolume = Action('CreateStorediSCSIVolume')
CreateTapeWithBarcode = Action('CreateTapeWithBarcode')
CreateTapes = Action('CreateTapes')
DeleteBandwidthRateLimit = Action('DeleteBandwidthRateLimit')
DeleteChapCredentials = Action('DeleteChapCredentials')
DeleteFileShare = Action('DeleteFileShare')
DeleteGateway = Action('DeleteGateway')
DeleteSnapshotSchedule = Action('DeleteSnapshotSchedule')
DeleteTape = Action('DeleteTape')
DeleteTapeArchive = Action('DeleteTapeArchive')
DeleteVolume = Action('DeleteVolume')
DescribeBandwidthRateLimit = Action('DescribeBandwidthRateLimit')
DescribeCache = Action('DescribeCache')
DescribeCachediSCSIVolumes = Action('DescribeCachediSCSIVolumes')
DescribeChapCredentials = Action('DescribeChapCredentials')
DescribeGatewayInformation = Action('DescribeGatewayInformation')
DescribeMaintenanceStartTime = Action('DescribeMaintenanceStartTime')
DescribeNFSFileShares = Action('DescribeNFSFileShares')
DescribeSnapshotSchedule = Action('DescribeSnapshotSchedule')
DescribeStorediSCSIVolumes = Action('DescribeStorediSCSIVolumes')
DescribeTapeArchives = Action('DescribeTapeArchives')
DescribeTapeRecoveryPoints = Action('DescribeTapeRecoveryPoints')
DescribeTapes = Action('DescribeTapes')
DescribeUploadBuffer = Action('DescribeUploadBuffer')
DescribeVTLDevices = Action('DescribeVTLDevices')
DescribeWorkingStorage = Action('DescribeWorkingStorage')
DisableGateway = Action('DisableGateway')
ListFileShares = Action('ListFileShares')
ListGateways = Action('ListGateways')
ListLocalDisks = Action('ListLocalDisks')
ListTagsForResource = Action('ListTagsForResource')
ListTapes = Action('ListTapes')
ListVolumeInitiators = Action('ListVolumeInitiators')
ListVolumeRecoveryPoints = Action('ListVolumeRecoveryPoints')
ListVolumes = Action('ListVolumes')
RefreshCache = Action('RefreshCache')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
ResetCache = Action('ResetCache')
RetrieveTapeArchive = Action('RetrieveTapeArchive')
RetrieveTapeRecoveryPoint = Action('RetrieveTapeRecoveryPoint')
SetLocalConsolePassword = Action('SetLocalConsolePassword')
ShutdownGateway = Action('ShutdownGateway')
StartGateway = Action('StartGateway')
UpdateBandwidthRateLimit = Action('UpdateBandwidthRateLimit')
UpdateChapCredentials = Action('UpdateChapCredentials')
UpdateGatewayInformation = Action('UpdateGatewayInformation')
UpdateGatewaySoftwareNow = Action('UpdateGatewaySoftwareNow')
UpdateMaintenanceStartTime = Action('UpdateMaintenanceStartTime')
UpdateNFSFileShare = Action('UpdateNFSFileShare')
UpdateSnapshotSchedule = Action('UpdateSnapshotSchedule')
UpdateVTLDeviceType = Action('UpdateVTLDeviceType')
