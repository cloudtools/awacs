# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Storage Gateway'
prefix = 'storagegateway'

ActivateGateway = Action(prefix, 'ActivateGateway')
AddCache = Action(prefix, 'AddCache')
AddUploadBuffer = Action(prefix, 'AddUploadBuffer')
AddWorkingStorage = Action(prefix, 'AddWorkingStorage')
CancelArchival = Action(prefix, 'CancelArchival')
CancelRetrieval = Action(prefix, 'CancelRetrieval')
CreateCachediSCSIVolume = Action(prefix, 'CreateCachediSCSIVolume')
CreateSnapshot = Action(prefix, 'CreateSnapshot')
CreateSnapshotFromVolumeRecoveryPoint = \
    Action(prefix, 'CreateSnapshotFromVolumeRecoveryPoint')
CreateStorediSCSIVolume = Action(prefix, 'CreateStorediSCSIVolume')
CreateTapes = Action(prefix, 'CreateTapes')
DeleteBandwidthRateLimit = Action(prefix, 'DeleteBandwidthRateLimit')
DeleteChapCredentials = Action(prefix, 'DeleteChapCredentials')
DeleteGateway = Action(prefix, 'DeleteGateway')
DeleteSnapshotSchedule = Action(prefix, 'DeleteSnapshotSchedule')
DeleteTape = Action(prefix, 'DeleteTape')
DeleteTapeArchive = Action(prefix, 'DeleteTapeArchive')
DeleteVolume = Action(prefix, 'DeleteVolume')
DescribeBandwidthRateLimit = \
    Action(prefix, 'DescribeBandwidthRateLimit')
DescribeCache = Action(prefix, 'DescribeCache')
DescribeCachediSCSIVolumes = \
    Action(prefix, 'DescribeCachediSCSIVolumes')
DescribeChapCredentials = Action(prefix, 'DescribeChapCredentials')
DescribeGatewayInformation = \
    Action(prefix, 'DescribeGatewayInformation')
DescribeMaintenanceStartTime = \
    Action(prefix, 'DescribeMaintenanceStartTime')
DescribeSnapshotSchedule = Action(prefix, 'DescribeSnapshotSchedule')
DescribeStorediSCSIVolumes = \
    Action(prefix, 'DescribeStorediSCSIVolumes')
DescribeTapeArchives = Action(prefix, 'DescribeTapeArchives')
DescribeTapeRecoveryPoints = \
    Action(prefix, 'DescribeTapeRecoveryPoints')
DescribeTapes = Action(prefix, 'DescribeTapes')
DescribeUploadBuffer = Action(prefix, 'DescribeUploadBuffer')
DescribeVTLDevices = Action(prefix, 'DescribeVTLDevices')
DescribeWorkingStorage = Action(prefix, 'DescribeWorkingStorage')
DisableGateway = Action(prefix, 'DisableGateway')
ListGateways = Action(prefix, 'ListGateways')
ListLocalDisks = Action(prefix, 'ListLocalDisks')
ListVolumeRecoveryPoints = Action(prefix, 'ListVolumeRecoveryPoints')
ListVolumes = Action(prefix, 'ListVolumes')
RetrieveTapeArchive = Action(prefix, 'RetrieveTapeArchive')
RetrieveTapeRecoveryPoint = Action(prefix, 'RetrieveTapeRecoveryPoint')
ShutdownGateway = Action(prefix, 'ShutdownGateway')
StartGateway = Action(prefix, 'StartGateway')
UpdateBandwidthRateLimit = Action(prefix, 'UpdateBandwidthRateLimit')
UpdateChapCredentials = Action(prefix, 'UpdateChapCredentials')
UpdateGatewayInformation = Action(prefix, 'UpdateGatewayInformation')
UpdateGatewaySoftwareNow = Action(prefix, 'UpdateGatewaySoftwareNow')
UpdateMaintenanceStartTime = \
    Action(prefix, 'UpdateMaintenanceStartTime')
UpdateSnapshotSchedule = Action(prefix, 'UpdateSnapshotSchedule')
