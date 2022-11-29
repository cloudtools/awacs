# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaPackage VOD"
prefix = "mediapackage-vod"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConfigureLogs = Action("ConfigureLogs")
CreateAsset = Action("CreateAsset")
CreatePackagingConfiguration = Action("CreatePackagingConfiguration")
CreatePackagingGroup = Action("CreatePackagingGroup")
DeleteAsset = Action("DeleteAsset")
DeletePackagingConfiguration = Action("DeletePackagingConfiguration")
DeletePackagingGroup = Action("DeletePackagingGroup")
DescribeAsset = Action("DescribeAsset")
DescribePackagingConfiguration = Action("DescribePackagingConfiguration")
DescribePackagingGroup = Action("DescribePackagingGroup")
ListAssets = Action("ListAssets")
ListPackagingConfigurations = Action("ListPackagingConfigurations")
ListPackagingGroups = Action("ListPackagingGroups")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePackagingGroup = Action("UpdatePackagingGroup")
