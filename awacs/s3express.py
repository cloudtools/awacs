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


CreateAccessPoint = Action("CreateAccessPoint")
CreateBucket = Action("CreateBucket")
CreateSession = Action("CreateSession")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteAccessPointPolicy = Action("DeleteAccessPointPolicy")
DeleteAccessPointScope = Action("DeleteAccessPointScope")
DeleteBucket = Action("DeleteBucket")
DeleteBucketPolicy = Action("DeleteBucketPolicy")
GetAccessPoint = Action("GetAccessPoint")
GetAccessPointPolicy = Action("GetAccessPointPolicy")
GetAccessPointScope = Action("GetAccessPointScope")
GetBucketPolicy = Action("GetBucketPolicy")
GetEncryptionConfiguration = Action("GetEncryptionConfiguration")
GetLifecycleConfiguration = Action("GetLifecycleConfiguration")
ListAccessPointsForDirectoryBuckets = Action("ListAccessPointsForDirectoryBuckets")
ListAllMyDirectoryBuckets = Action("ListAllMyDirectoryBuckets")
PutAccessPointPolicy = Action("PutAccessPointPolicy")
PutAccessPointScope = Action("PutAccessPointScope")
PutBucketPolicy = Action("PutBucketPolicy")
PutEncryptionConfiguration = Action("PutEncryptionConfiguration")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
