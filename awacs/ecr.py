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
CompleteLayerUpload = Action("CompleteLayerUpload")
CreateRepository = Action("CreateRepository")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
DeleteRegistryPolicy = Action("DeleteRegistryPolicy")
DeleteRepository = Action("DeleteRepository")
DeleteRepositoryPolicy = Action("DeleteRepositoryPolicy")
DescribeImageScanFindings = Action("DescribeImageScanFindings")
DescribeImages = Action("DescribeImages")
DescribeRegistry = Action("DescribeRegistry")
DescribeRepositories = Action("DescribeRepositories")
GetAuthorizationToken = Action("GetAuthorizationToken")
GetDownloadUrlForLayer = Action("GetDownloadUrlForLayer")
GetLifecyclePolicy = Action("GetLifecyclePolicy")
GetLifecyclePolicyPreview = Action("GetLifecyclePolicyPreview")
GetRegistryPolicy = Action("GetRegistryPolicy")
GetRepositoryPolicy = Action("GetRepositoryPolicy")
InitiateLayerUpload = Action("InitiateLayerUpload")
ListImages = Action("ListImages")
ListTagsForResource = Action("ListTagsForResource")
PutImage = Action("PutImage")
PutImageScanningConfiguration = Action("PutImageScanningConfiguration")
PutImageTagMutability = Action("PutImageTagMutability")
PutLifecyclePolicy = Action("PutLifecyclePolicy")
PutRegistryPolicy = Action("PutRegistryPolicy")
PutReplicationConfiguration = Action("PutReplicationConfiguration")
ReplicateImage = Action("ReplicateImage")
SetRepositoryPolicy = Action("SetRepositoryPolicy")
StartImageScan = Action("StartImageScan")
StartLifecyclePolicyPreview = Action("StartLifecyclePolicyPreview")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UploadLayerPart = Action("UploadLayerPart")
