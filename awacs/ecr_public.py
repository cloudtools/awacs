# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic Container Registry Public"
prefix = "ecr-public"


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
CompleteLayerUpload = Action("CompleteLayerUpload")
CreateRepository = Action("CreateRepository")
DeleteRepository = Action("DeleteRepository")
DeleteRepositoryPolicy = Action("DeleteRepositoryPolicy")
DescribeImageTags = Action("DescribeImageTags")
DescribeImages = Action("DescribeImages")
DescribeRegistries = Action("DescribeRegistries")
DescribeRepositories = Action("DescribeRepositories")
GetAuthorizationToken = Action("GetAuthorizationToken")
GetRegistryCatalogData = Action("GetRegistryCatalogData")
GetRepositoryCatalogData = Action("GetRepositoryCatalogData")
GetRepositoryPolicy = Action("GetRepositoryPolicy")
InitiateLayerUpload = Action("InitiateLayerUpload")
ListTagsForResource = Action("ListTagsForResource")
PutImage = Action("PutImage")
PutRegistryCatalogData = Action("PutRegistryCatalogData")
PutRepositoryCatalogData = Action("PutRepositoryCatalogData")
SetRepositoryPolicy = Action("SetRepositoryPolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UploadLayerPart = Action("UploadLayerPart")
