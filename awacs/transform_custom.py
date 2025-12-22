# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Transform custom"
prefix = "transform-custom"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CompleteTransformationPackageUpload = Action("CompleteTransformationPackageUpload")
ConverseStream = Action("ConverseStream")
CreateCampaign = Action("CreateCampaign")
CreateTransformationPackageUrl = Action("CreateTransformationPackageUrl")
DeleteCampaign = Action("DeleteCampaign")
DeleteKnowledgeItem = Action("DeleteKnowledgeItem")
DeleteTransformationPackage = Action("DeleteTransformationPackage")
ExecuteTransformation = Action("ExecuteTransformation")
GetCampaign = Action("GetCampaign")
GetKnowledgeItem = Action("GetKnowledgeItem")
GetTransformationPackageUrl = Action("GetTransformationPackageUrl")
ListCampaignRepositories = Action("ListCampaignRepositories")
ListCampaigns = Action("ListCampaigns")
ListKnowledgeItems = Action("ListKnowledgeItems")
ListTagsForResource = Action("ListTagsForResource")
ListTransformationPackageMetadata = Action("ListTransformationPackageMetadata")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCampaign = Action("UpdateCampaign")
UpdateCampaignRepositoryStatus = Action("UpdateCampaignRepositoryStatus")
UpdateKnowledgeItemConfiguration = Action("UpdateKnowledgeItemConfiguration")
UpdateKnowledgeItemStatus = Action("UpdateKnowledgeItemStatus")
