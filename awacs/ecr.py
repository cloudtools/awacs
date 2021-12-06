# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic Container Registry"
prefix = "ecr"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
CompleteLayerUpload = Action("CompleteLayerUpload")
CreatePullThroughCacheRule = Action("CreatePullThroughCacheRule")
CreateRepository = Action("CreateRepository")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
DeletePullThroughCacheRule = Action("DeletePullThroughCacheRule")
DeleteRegistryPolicy = Action("DeleteRegistryPolicy")
DeleteRepository = Action("DeleteRepository")
DeleteRepositoryPolicy = Action("DeleteRepositoryPolicy")
DescribeImageReplicationStatus = Action("DescribeImageReplicationStatus")
DescribeImageScanFindings = Action("DescribeImageScanFindings")
DescribeImages = Action("DescribeImages")
DescribePullThroughCacheRules = Action("DescribePullThroughCacheRules")
DescribeRegistry = Action("DescribeRegistry")
DescribeRepositories = Action("DescribeRepositories")
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
UploadLayerPart = Action("UploadLayerPart")
