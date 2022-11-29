# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Storage Gateway"
prefix = "storagegateway"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateGateway = Action("ActivateGateway")
AddCache = Action("AddCache")
AddTagsToResource = Action("AddTagsToResource")
AddUploadBuffer = Action("AddUploadBuffer")
AddWorkingStorage = Action("AddWorkingStorage")
AssignTapePool = Action("AssignTapePool")
AssociateFileSystem = Action("AssociateFileSystem")
AttachVolume = Action("AttachVolume")
BypassGovernanceRetention = Action("BypassGovernanceRetention")
CancelArchival = Action("CancelArchival")
CancelRetrieval = Action("CancelRetrieval")
CreateCachediSCSIVolume = Action("CreateCachediSCSIVolume")
CreateNFSFileShare = Action("CreateNFSFileShare")
CreateSMBFileShare = Action("CreateSMBFileShare")
CreateSnapshot = Action("CreateSnapshot")
CreateSnapshotFromVolumeRecoveryPoint = Action("CreateSnapshotFromVolumeRecoveryPoint")
CreateStorediSCSIVolume = Action("CreateStorediSCSIVolume")
CreateTapePool = Action("CreateTapePool")
CreateTapeWithBarcode = Action("CreateTapeWithBarcode")
CreateTapes = Action("CreateTapes")
DeleteAutomaticTapeCreationPolicy = Action("DeleteAutomaticTapeCreationPolicy")
DeleteBandwidthRateLimit = Action("DeleteBandwidthRateLimit")
DeleteChapCredentials = Action("DeleteChapCredentials")
DeleteFileShare = Action("DeleteFileShare")
DeleteGateway = Action("DeleteGateway")
DeleteSnapshotSchedule = Action("DeleteSnapshotSchedule")
DeleteTape = Action("DeleteTape")
DeleteTapeArchive = Action("DeleteTapeArchive")
DeleteTapePool = Action("DeleteTapePool")
DeleteVolume = Action("DeleteVolume")
DescribeAvailabilityMonitorTest = Action("DescribeAvailabilityMonitorTest")
DescribeBandwidthRateLimit = Action("DescribeBandwidthRateLimit")
DescribeBandwidthRateLimitSchedule = Action("DescribeBandwidthRateLimitSchedule")
DescribeCache = Action("DescribeCache")
DescribeCachediSCSIVolumes = Action("DescribeCachediSCSIVolumes")
DescribeChapCredentials = Action("DescribeChapCredentials")
DescribeFileSystemAssociations = Action("DescribeFileSystemAssociations")
DescribeGatewayInformation = Action("DescribeGatewayInformation")
DescribeMaintenanceStartTime = Action("DescribeMaintenanceStartTime")
DescribeNFSFileShares = Action("DescribeNFSFileShares")
DescribeSMBFileShares = Action("DescribeSMBFileShares")
DescribeSMBSettings = Action("DescribeSMBSettings")
DescribeSnapshotSchedule = Action("DescribeSnapshotSchedule")
DescribeStorediSCSIVolumes = Action("DescribeStorediSCSIVolumes")
DescribeTapeArchives = Action("DescribeTapeArchives")
DescribeTapeRecoveryPoints = Action("DescribeTapeRecoveryPoints")
DescribeTapes = Action("DescribeTapes")
DescribeUploadBuffer = Action("DescribeUploadBuffer")
DescribeVTLDevices = Action("DescribeVTLDevices")
DescribeWorkingStorage = Action("DescribeWorkingStorage")
DetachVolume = Action("DetachVolume")
DisableGateway = Action("DisableGateway")
DisassociateFileSystem = Action("DisassociateFileSystem")
JoinDomain = Action("JoinDomain")
ListAutomaticTapeCreationPolicies = Action("ListAutomaticTapeCreationPolicies")
ListFileShares = Action("ListFileShares")
ListFileSystemAssociations = Action("ListFileSystemAssociations")
ListGateways = Action("ListGateways")
ListLocalDisks = Action("ListLocalDisks")
ListTagsForResource = Action("ListTagsForResource")
ListTapePools = Action("ListTapePools")
ListTapes = Action("ListTapes")
ListVolumeInitiators = Action("ListVolumeInitiators")
ListVolumeRecoveryPoints = Action("ListVolumeRecoveryPoints")
ListVolumes = Action("ListVolumes")
NotifyWhenUploaded = Action("NotifyWhenUploaded")
RefreshCache = Action("RefreshCache")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
ResetCache = Action("ResetCache")
RetrieveTapeArchive = Action("RetrieveTapeArchive")
RetrieveTapeRecoveryPoint = Action("RetrieveTapeRecoveryPoint")
SetLocalConsolePassword = Action("SetLocalConsolePassword")
SetSMBGuestPassword = Action("SetSMBGuestPassword")
ShutdownGateway = Action("ShutdownGateway")
StartAvailabilityMonitorTest = Action("StartAvailabilityMonitorTest")
StartGateway = Action("StartGateway")
UpdateAutomaticTapeCreationPolicy = Action("UpdateAutomaticTapeCreationPolicy")
UpdateBandwidthRateLimit = Action("UpdateBandwidthRateLimit")
UpdateBandwidthRateLimitSchedule = Action("UpdateBandwidthRateLimitSchedule")
UpdateChapCredentials = Action("UpdateChapCredentials")
UpdateFileSystemAssociation = Action("UpdateFileSystemAssociation")
UpdateGatewayInformation = Action("UpdateGatewayInformation")
UpdateGatewaySoftwareNow = Action("UpdateGatewaySoftwareNow")
UpdateMaintenanceStartTime = Action("UpdateMaintenanceStartTime")
UpdateNFSFileShare = Action("UpdateNFSFileShare")
UpdateSMBFileShare = Action("UpdateSMBFileShare")
UpdateSMBFileShareVisibility = Action("UpdateSMBFileShareVisibility")
UpdateSMBLocalGroups = Action("UpdateSMBLocalGroups")
UpdateSMBSecurityStrategy = Action("UpdateSMBSecurityStrategy")
UpdateSnapshotSchedule = Action("UpdateSnapshotSchedule")
UpdateVTLDeviceType = Action("UpdateVTLDeviceType")
