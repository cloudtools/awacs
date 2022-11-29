# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Object Lambda"
prefix = "s3-object-lambda"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortMultipartUpload = Action("AbortMultipartUpload")
DeleteObject = Action("DeleteObject")
DeleteObjectTagging = Action("DeleteObjectTagging")
DeleteObjectVersion = Action("DeleteObjectVersion")
DeleteObjectVersionTagging = Action("DeleteObjectVersionTagging")
GetObject = Action("GetObject")
GetObjectAcl = Action("GetObjectAcl")
GetObjectLegalHold = Action("GetObjectLegalHold")
GetObjectRetention = Action("GetObjectRetention")
GetObjectTagging = Action("GetObjectTagging")
GetObjectVersion = Action("GetObjectVersion")
GetObjectVersionAcl = Action("GetObjectVersionAcl")
GetObjectVersionTagging = Action("GetObjectVersionTagging")
ListBucket = Action("ListBucket")
ListBucketMultipartUploads = Action("ListBucketMultipartUploads")
ListBucketVersions = Action("ListBucketVersions")
ListMultipartUploadParts = Action("ListMultipartUploadParts")
PutObject = Action("PutObject")
PutObjectAcl = Action("PutObjectAcl")
PutObjectLegalHold = Action("PutObjectLegalHold")
PutObjectRetention = Action("PutObjectRetention")
PutObjectTagging = Action("PutObjectTagging")
PutObjectVersionAcl = Action("PutObjectVersionAcl")
PutObjectVersionTagging = Action("PutObjectVersionTagging")
RestoreObject = Action("RestoreObject")
WriteGetObjectResponse = Action("WriteGetObjectResponse")
