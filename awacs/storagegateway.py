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
AddUploadBuffer = Action('AddUploadBuffer')
AddWorkingStorage = Action('AddWorkingStorage')
CancelArchival = Action('CancelArchival')
CancelRetrieval = Action('CancelRetrieval')
CreateCachediSCSIVolume = Action('CreateCachediSCSIVolume')
CreateSnapshot = Action('CreateSnapshot')
CreateSnapshotFromVolumeRecoveryPoint = \
    Action('CreateSnapshotFromVolumeRecoveryPoint')
CreateStorediSCSIVolume = Action('CreateStorediSCSIVolume')
CreateTapes = Action('CreateTapes')
CreateTapeWithBarcode = Action('CreateTapeWithBarcode')
DeleteBandwidthRateLimit = Action('DeleteBandwidthRateLimit')
DeleteChapCredentials = Action('DeleteChapCredentials')
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
DescribeSnapshotSchedule = Action('DescribeSnapshotSchedule')
DescribeStorediSCSIVolumes = Action('DescribeStorediSCSIVolumes')
DescribeTapeArchives = Action('DescribeTapeArchives')
DescribeTapeRecoveryPoints = Action('DescribeTapeRecoveryPoints')
DescribeTapes = Action('DescribeTapes')
DescribeUploadBuffer = Action('DescribeUploadBuffer')
DescribeVTLDevices = Action('DescribeVTLDevices')
DescribeWorkingStorage = Action('DescribeWorkingStorage')
DisableGateway = Action('DisableGateway')
ListGateways = Action('ListGateways')
ListLocalDisks = Action('ListLocalDisks')
ListTagsForResource = Action('ListTagsForResource')
ListTapes = Action('ListTapes')
ListVolumeRecoveryPoints = Action('ListVolumeRecoveryPoints')
ListVolumes = Action('ListVolumes')
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
UpdateSnapshotSchedule = Action('UpdateSnapshotSchedule')
