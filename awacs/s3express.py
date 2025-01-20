# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Express"
prefix = "s3express"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBucket = Action("CreateBucket")
CreateSession = Action("CreateSession")
DeleteBucket = Action("DeleteBucket")
DeleteBucketPolicy = Action("DeleteBucketPolicy")
GetBucketPolicy = Action("GetBucketPolicy")
GetEncryptionConfiguration = Action("GetEncryptionConfiguration")
GetLifecycleConfiguration = Action("GetLifecycleConfiguration")
ListAllMyDirectoryBuckets = Action("ListAllMyDirectoryBuckets")
PutBucketPolicy = Action("PutBucketPolicy")
PutEncryptionConfiguration = Action("PutEncryptionConfiguration")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
