# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic File System"
prefix = "elasticfilesystem"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


Backup = Action("Backup")
ClientMount = Action("ClientMount")
ClientRootAccess = Action("ClientRootAccess")
ClientWrite = Action("ClientWrite")
CreateAccessPoint = Action("CreateAccessPoint")
CreateFileSystem = Action("CreateFileSystem")
CreateMountTarget = Action("CreateMountTarget")
CreateReplicationConfiguration = Action("CreateReplicationConfiguration")
CreateTags = Action("CreateTags")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteFileSystemPolicy = Action("DeleteFileSystemPolicy")
DeleteMountTarget = Action("DeleteMountTarget")
DeleteReplicationConfiguration = Action("DeleteReplicationConfiguration")
DeleteTags = Action("DeleteTags")
DescribeAccessPoints = Action("DescribeAccessPoints")
DescribeAccountPreferences = Action("DescribeAccountPreferences")
DescribeBackupPolicy = Action("DescribeBackupPolicy")
DescribeFileSystemPolicy = Action("DescribeFileSystemPolicy")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeLifecycleConfiguration = Action("DescribeLifecycleConfiguration")
DescribeMountTargetSecurityGroups = Action("DescribeMountTargetSecurityGroups")
DescribeMountTargets = Action("DescribeMountTargets")
DescribeReplicationConfigurations = Action("DescribeReplicationConfigurations")
DescribeTags = Action("DescribeTags")
ListTagsForResource = Action("ListTagsForResource")
ModifyMountTargetSecurityGroups = Action("ModifyMountTargetSecurityGroups")
PutAccountPreferences = Action("PutAccountPreferences")
PutBackupPolicy = Action("PutBackupPolicy")
PutFileSystemPolicy = Action("PutFileSystemPolicy")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
ReplicationRead = Action("ReplicationRead")
ReplicationWrite = Action("ReplicationWrite")
Restore = Action("Restore")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFileSystem = Action("UpdateFileSystem")
UpdateFileSystemProtection = Action("UpdateFileSystemProtection")
