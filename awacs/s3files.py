# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Files"
prefix = "s3files"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ClientMount = Action("ClientMount")
ClientRootAccess = Action("ClientRootAccess")
ClientWrite = Action("ClientWrite")
CreateAccessPoint = Action("CreateAccessPoint")
CreateFileSystem = Action("CreateFileSystem")
CreateMountTarget = Action("CreateMountTarget")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteFileSystemPolicy = Action("DeleteFileSystemPolicy")
DeleteMountTarget = Action("DeleteMountTarget")
GetAccessPoint = Action("GetAccessPoint")
GetFileSystem = Action("GetFileSystem")
GetFileSystemPolicy = Action("GetFileSystemPolicy")
GetMountTarget = Action("GetMountTarget")
GetSynchronizationConfiguration = Action("GetSynchronizationConfiguration")
ListAccessPoints = Action("ListAccessPoints")
ListFileSystems = Action("ListFileSystems")
ListMountTargets = Action("ListMountTargets")
ListTagsForResource = Action("ListTagsForResource")
PutFileSystemPolicy = Action("PutFileSystemPolicy")
PutSynchronizationConfiguration = Action("PutSynchronizationConfiguration")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateMountTarget = Action("UpdateMountTarget")
