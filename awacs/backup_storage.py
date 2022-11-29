# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Backup storage"
prefix = "backup-storage"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CommitBackupJob = Action("CommitBackupJob")
DeleteObjects = Action("DeleteObjects")
DescribeBackupJob = Action("DescribeBackupJob")
GetBaseBackup = Action("GetBaseBackup")
GetChunk = Action("GetChunk")
GetIncrementalBaseBackup = Action("GetIncrementalBaseBackup")
GetObjectMetadata = Action("GetObjectMetadata")
ListChunks = Action("ListChunks")
ListObjects = Action("ListObjects")
MountCapsule = Action("MountCapsule")
NotifyObjectComplete = Action("NotifyObjectComplete")
PutChunk = Action("PutChunk")
PutObject = Action("PutObject")
StartObject = Action("StartObject")
UpdateObjectComplete = Action("UpdateObjectComplete")
