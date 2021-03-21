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


AssociateFileSystemAliases = Action("AssociateFileSystemAliases")
CancelDataRepositoryTask = Action("CancelDataRepositoryTask")
CreateBackup = Action("CreateBackup")
CreateDataRepositoryTask = Action("CreateDataRepositoryTask")
CreateFileSystem = Action("CreateFileSystem")
CreateFileSystemFromBackup = Action("CreateFileSystemFromBackup")
DeleteBackup = Action("DeleteBackup")
DeleteFileSystem = Action("DeleteFileSystem")
DescribeBackups = Action("DescribeBackups")
DescribeDataRepositoryTasks = Action("DescribeDataRepositoryTasks")
DescribeFileSystemAliases = Action("DescribeFileSystemAliases")
DescribeFileSystems = Action("DescribeFileSystems")
DisassociateFileSystemAliases = Action("DisassociateFileSystemAliases")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFileSystem = Action("UpdateFileSystem")
