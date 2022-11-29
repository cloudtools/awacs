# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Glacier"
prefix = "glacier"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortMultipartUpload = Action("AbortMultipartUpload")
AbortVaultLock = Action("AbortVaultLock")
AddTagsToVault = Action("AddTagsToVault")
CompleteMultipartUpload = Action("CompleteMultipartUpload")
CompleteVaultLock = Action("CompleteVaultLock")
CreateVault = Action("CreateVault")
DeleteArchive = Action("DeleteArchive")
DeleteVault = Action("DeleteVault")
DeleteVaultAccessPolicy = Action("DeleteVaultAccessPolicy")
DeleteVaultNotifications = Action("DeleteVaultNotifications")
DescribeJob = Action("DescribeJob")
DescribeVault = Action("DescribeVault")
GetDataRetrievalPolicy = Action("GetDataRetrievalPolicy")
GetJobOutput = Action("GetJobOutput")
GetVaultAccessPolicy = Action("GetVaultAccessPolicy")
GetVaultLock = Action("GetVaultLock")
GetVaultNotifications = Action("GetVaultNotifications")
InitiateJob = Action("InitiateJob")
InitiateMultipartUpload = Action("InitiateMultipartUpload")
InitiateVaultLock = Action("InitiateVaultLock")
ListJobs = Action("ListJobs")
ListMultipartUploads = Action("ListMultipartUploads")
ListParts = Action("ListParts")
ListProvisionedCapacity = Action("ListProvisionedCapacity")
ListTagsForVault = Action("ListTagsForVault")
ListVaults = Action("ListVaults")
PurchaseProvisionedCapacity = Action("PurchaseProvisionedCapacity")
RemoveTagsFromVault = Action("RemoveTagsFromVault")
SetDataRetrievalPolicy = Action("SetDataRetrievalPolicy")
SetVaultAccessPolicy = Action("SetVaultAccessPolicy")
SetVaultNotifications = Action("SetVaultNotifications")
UploadArchive = Action("UploadArchive")
UploadMultipartPart = Action("UploadMultipartPart")
