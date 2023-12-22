# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FSx"
prefix = "fsx"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFileGateway = Action("AssociateFileGateway")
AssociateFileSystemAliases = Action("AssociateFileSystemAliases")
BypassSnaplockEnterpriseRetention = Action("BypassSnaplockEnterpriseRetention")
CancelDataRepositoryTask = Action("CancelDataRepositoryTask")
CopyBackup = Action("CopyBackup")
CopySnapshotAndUpdateVolume = Action("CopySnapshotAndUpdateVolume")
CreateBackup = Action("CreateBackup")
CreateDataRepositoryAssociation = Action("CreateDataRepositoryAssociation")
CreateDataRepositoryTask = Action("CreateDataRepositoryTask")
CreateFileCache = Action("CreateFileCache")
CreateFileSystem = Action("CreateFileSystem")
CreateFileSystemFromBackup = Action("CreateFileSystemFromBackup")
CreateSnapshot = Action("CreateSnapshot")
CreateStorageVirtualMachine = Action("CreateStorageVirtualMachine")
CreateVolume = Action("CreateVolume")
CreateVolumeFromBackup = Action("CreateVolumeFromBackup")
DeleteBackup = Action("DeleteBackup")
DeleteDataRepositoryAssociation = Action("DeleteDataRepositoryAssociation")
DeleteFileCache = Action("DeleteFileCache")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteStorageVirtualMachine = Action("DeleteStorageVirtualMachine")
DeleteVolume = Action("DeleteVolume")
DescribeAssociatedFileGateways = Action("DescribeAssociatedFileGateways")
DescribeBackups = Action("DescribeBackups")
DescribeDataRepositoryAssociations = Action("DescribeDataRepositoryAssociations")
DescribeDataRepositoryTasks = Action("DescribeDataRepositoryTasks")
DescribeFileCaches = Action("DescribeFileCaches")
DescribeFileSystemAliases = Action("DescribeFileSystemAliases")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeSharedVpcConfiguration = Action("DescribeSharedVpcConfiguration")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeStorageVirtualMachines = Action("DescribeStorageVirtualMachines")
DescribeVolumes = Action("DescribeVolumes")
DisassociateFileGateway = Action("DisassociateFileGateway")
DisassociateFileSystemAliases = Action("DisassociateFileSystemAliases")
GetResourcePolicy = Action("GetResourcePolicy")
ListTagsForResource = Action("ListTagsForResource")
ManageBackupPrincipalAssociations = Action("ManageBackupPrincipalAssociations")
PutResourcePolicy = Action("PutResourcePolicy")
ReleaseFileSystemNfsV3Locks = Action("ReleaseFileSystemNfsV3Locks")
RestoreVolumeFromSnapshot = Action("RestoreVolumeFromSnapshot")
StartMisconfiguredStateRecovery = Action("StartMisconfiguredStateRecovery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataRepositoryAssociation = Action("UpdateDataRepositoryAssociation")
UpdateFileCache = Action("UpdateFileCache")
UpdateFileSystem = Action("UpdateFileSystem")
UpdateSharedVpcConfiguration = Action("UpdateSharedVpcConfiguration")
UpdateSnapshot = Action("UpdateSnapshot")
UpdateStorageVirtualMachine = Action("UpdateStorageVirtualMachine")
UpdateVolume = Action("UpdateVolume")
