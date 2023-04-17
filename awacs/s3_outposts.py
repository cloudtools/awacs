# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 on Outposts"
prefix = "s3-outposts"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortMultipartUpload = Action("AbortMultipartUpload")
CreateAccessPoint = Action("CreateAccessPoint")
CreateBucket = Action("CreateBucket")
CreateEndpoint = Action("CreateEndpoint")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteAccessPointPolicy = Action("DeleteAccessPointPolicy")
DeleteBucket = Action("DeleteBucket")
DeleteBucketPolicy = Action("DeleteBucketPolicy")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteObject = Action("DeleteObject")
DeleteObjectTagging = Action("DeleteObjectTagging")
DeleteObjectVersion = Action("DeleteObjectVersion")
DeleteObjectVersionTagging = Action("DeleteObjectVersionTagging")
GetAccessPoint = Action("GetAccessPoint")
GetAccessPointPolicy = Action("GetAccessPointPolicy")
GetBucket = Action("GetBucket")
GetBucketPolicy = Action("GetBucketPolicy")
GetBucketTagging = Action("GetBucketTagging")
GetBucketVersioning = Action("GetBucketVersioning")
GetLifecycleConfiguration = Action("GetLifecycleConfiguration")
GetObject = Action("GetObject")
GetObjectTagging = Action("GetObjectTagging")
GetObjectVersion = Action("GetObjectVersion")
GetObjectVersionForReplication = Action("GetObjectVersionForReplication")
GetObjectVersionTagging = Action("GetObjectVersionTagging")
GetReplicationConfiguration = Action("GetReplicationConfiguration")
ListAccessPoints = Action("ListAccessPoints")
ListBucket = Action("ListBucket")
ListBucketMultipartUploads = Action("ListBucketMultipartUploads")
ListBucketVersions = Action("ListBucketVersions")
ListEndpoints = Action("ListEndpoints")
ListMultipartUploadParts = Action("ListMultipartUploadParts")
ListOutpostsWithS3 = Action("ListOutpostsWithS3")
ListRegionalBuckets = Action("ListRegionalBuckets")
ListSharedEndpoints = Action("ListSharedEndpoints")
PutAccessPointPolicy = Action("PutAccessPointPolicy")
PutBucketPolicy = Action("PutBucketPolicy")
PutBucketTagging = Action("PutBucketTagging")
PutBucketVersioning = Action("PutBucketVersioning")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
PutObject = Action("PutObject")
PutObjectAcl = Action("PutObjectAcl")
PutObjectTagging = Action("PutObjectTagging")
PutObjectVersionTagging = Action("PutObjectVersionTagging")
PutReplicationConfiguration = Action("PutReplicationConfiguration")
ReplicateDelete = Action("ReplicateDelete")
ReplicateObject = Action("ReplicateObject")
ReplicateTags = Action("ReplicateTags")
