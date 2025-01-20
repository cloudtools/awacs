# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic Container Registry"
prefix = "ecr"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCheckLayerAvailability = Action("BatchCheckLayerAvailability")
BatchDeleteImage = Action("BatchDeleteImage")
BatchGetImage = Action("BatchGetImage")
BatchGetRepositoryScanningConfiguration = Action(
    "BatchGetRepositoryScanningConfiguration"
)
BatchImportUpstreamImage = Action("BatchImportUpstreamImage")
CompleteLayerUpload = Action("CompleteLayerUpload")
CreatePullThroughCacheRule = Action("CreatePullThroughCacheRule")
CreateRepository = Action("CreateRepository")
CreateRepositoryCreationTemplate = Action("CreateRepositoryCreationTemplate")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
DeletePullThroughCacheRule = Action("DeletePullThroughCacheRule")
DeleteRegistryPolicy = Action("DeleteRegistryPolicy")
DeleteRepository = Action("DeleteRepository")
DeleteRepositoryCreationTemplate = Action("DeleteRepositoryCreationTemplate")
DeleteRepositoryPolicy = Action("DeleteRepositoryPolicy")
DescribeImageReplicationStatus = Action("DescribeImageReplicationStatus")
DescribeImageScanFindings = Action("DescribeImageScanFindings")
DescribeImages = Action("DescribeImages")
DescribePullThroughCacheRules = Action("DescribePullThroughCacheRules")
DescribeRegistry = Action("DescribeRegistry")
DescribeRepositories = Action("DescribeRepositories")
DescribeRepositoryCreationTemplate = Action("DescribeRepositoryCreationTemplate")
DescribeRepositoryCreationTemplates = Action("DescribeRepositoryCreationTemplates")
GetAccountSetting = Action("GetAccountSetting")
GetAuthorizationToken = Action("GetAuthorizationToken")
GetDownloadUrlForLayer = Action("GetDownloadUrlForLayer")
GetLifecyclePolicy = Action("GetLifecyclePolicy")
GetLifecyclePolicyPreview = Action("GetLifecyclePolicyPreview")
GetRegistryPolicy = Action("GetRegistryPolicy")
GetRegistryScanningConfiguration = Action("GetRegistryScanningConfiguration")
GetRepositoryPolicy = Action("GetRepositoryPolicy")
InitiateLayerUpload = Action("InitiateLayerUpload")
ListImages = Action("ListImages")
ListTagsForResource = Action("ListTagsForResource")
PutAccountSetting = Action("PutAccountSetting")
PutImage = Action("PutImage")
PutImageScanningConfiguration = Action("PutImageScanningConfiguration")
PutImageTagMutability = Action("PutImageTagMutability")
PutLifecyclePolicy = Action("PutLifecyclePolicy")
PutRegistryPolicy = Action("PutRegistryPolicy")
PutRegistryScanningConfiguration = Action("PutRegistryScanningConfiguration")
PutReplicationConfiguration = Action("PutReplicationConfiguration")
ReplicateImage = Action("ReplicateImage")
SetRepositoryPolicy = Action("SetRepositoryPolicy")
StartImageScan = Action("StartImageScan")
StartLifecyclePolicyPreview = Action("StartLifecyclePolicyPreview")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePullThroughCacheRule = Action("UpdatePullThroughCacheRule")
UpdateRepositoryCreationTemplate = Action("UpdateRepositoryCreationTemplate")
UploadLayerPart = Action("UploadLayerPart")
ValidatePullThroughCacheRule = Action("ValidatePullThroughCacheRule")
