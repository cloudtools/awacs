# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Vectors"
prefix = "s3vectors"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateIndex = Action("CreateIndex")
CreateVectorBucket = Action("CreateVectorBucket")
DeleteIndex = Action("DeleteIndex")
DeleteVectorBucket = Action("DeleteVectorBucket")
DeleteVectorBucketPolicy = Action("DeleteVectorBucketPolicy")
DeleteVectors = Action("DeleteVectors")
GetIndex = Action("GetIndex")
GetVectorBucket = Action("GetVectorBucket")
GetVectorBucketPolicy = Action("GetVectorBucketPolicy")
GetVectors = Action("GetVectors")
ListIndexes = Action("ListIndexes")
ListVectorBuckets = Action("ListVectorBuckets")
ListVectors = Action("ListVectors")
PutVectorBucketPolicy = Action("PutVectorBucketPolicy")
PutVectors = Action("PutVectors")
QueryVectors = Action("QueryVectors")
