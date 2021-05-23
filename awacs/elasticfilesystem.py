# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic File System"
prefix = "elasticfilesystem"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CreateTags = Action("CreateTags")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteFileSystemPolicy = Action("DeleteFileSystemPolicy")
DeleteMountTarget = Action("DeleteMountTarget")
DeleteTags = Action("DeleteTags")
DescribeAccessPoints = Action("DescribeAccessPoints")
DescribeAccountPreferences = Action("DescribeAccountPreferences")
DescribeBackupPolicy = Action("DescribeBackupPolicy")
DescribeFileSystemPolicy = Action("DescribeFileSystemPolicy")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeLifecycleConfiguration = Action("DescribeLifecycleConfiguration")
DescribeMountTargetSecurityGroups = Action("DescribeMountTargetSecurityGroups")
DescribeMountTargets = Action("DescribeMountTargets")
DescribeTags = Action("DescribeTags")
ListTagsForResource = Action("ListTagsForResource")
ModifyMountTargetSecurityGroups = Action("ModifyMountTargetSecurityGroups")
PutAccountPreferences = Action("PutAccountPreferences")
PutBackupPolicy = Action("PutBackupPolicy")
PutFileSystemPolicy = Action("PutFileSystemPolicy")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
Restore = Action("Restore")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFileSystem = Action("UpdateFileSystem")
