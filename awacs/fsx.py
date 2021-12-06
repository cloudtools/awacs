# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon FSx"
prefix = "fsx"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFileGateway = Action("AssociateFileGateway")
AssociateFileSystemAliases = Action("AssociateFileSystemAliases")
CancelDataRepositoryTask = Action("CancelDataRepositoryTask")
CopyBackup = Action("CopyBackup")
CreateBackup = Action("CreateBackup")
CreateDataRepositoryAssociation = Action("CreateDataRepositoryAssociation")
CreateDataRepositoryTask = Action("CreateDataRepositoryTask")
CreateFileSystem = Action("CreateFileSystem")
CreateFileSystemFromBackup = Action("CreateFileSystemFromBackup")
CreateSnapshot = Action("CreateSnapshot")
CreateStorageVirtualMachine = Action("CreateStorageVirtualMachine")
CreateVolume = Action("CreateVolume")
CreateVolumeFromBackup = Action("CreateVolumeFromBackup")
DeleteBackup = Action("DeleteBackup")
DeleteDataRepositoryAssociation = Action("DeleteDataRepositoryAssociation")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteStorageVirtualMachine = Action("DeleteStorageVirtualMachine")
DeleteVolume = Action("DeleteVolume")
DescribeAssociatedFileGateways = Action("DescribeAssociatedFileGateways")
DescribeBackups = Action("DescribeBackups")
DescribeDataRepositoryAssociations = Action("DescribeDataRepositoryAssociations")
DescribeDataRepositoryTasks = Action("DescribeDataRepositoryTasks")
DescribeFileSystemAliases = Action("DescribeFileSystemAliases")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeStorageVirtualMachines = Action("DescribeStorageVirtualMachines")
DescribeVolumes = Action("DescribeVolumes")
DisassociateFileGateway = Action("DisassociateFileGateway")
DisassociateFileSystemAliases = Action("DisassociateFileSystemAliases")
ListTagsForResource = Action("ListTagsForResource")
ManageBackupPrincipalAssociations = Action("ManageBackupPrincipalAssociations")
RestoreVolumeFromSnapshot = Action("RestoreVolumeFromSnapshot")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataRepositoryAssociation = Action("UpdateDataRepositoryAssociation")
UpdateFileSystem = Action("UpdateFileSystem")
UpdateSnapshot = Action("UpdateSnapshot")
UpdateStorageVirtualMachine = Action("UpdateStorageVirtualMachine")
UpdateVolume = Action("UpdateVolume")
