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


BatchCreateFindings = Action("BatchCreateFindings")
BatchUpdateFindings = Action("BatchUpdateFindings")
CompleteTransformationPackageUpload = Action("CompleteTransformationPackageUpload")
ConverseStream = Action("ConverseStream")
CreateAnalysis = Action("CreateAnalysis")
CreateCampaign = Action("CreateCampaign")
CreateRemediation = Action("CreateRemediation")
CreateRepository = Action("CreateRepository")
CreateSource = Action("CreateSource")
CreateTransformationPackageUrl = Action("CreateTransformationPackageUrl")
DeleteAnalysis = Action("DeleteAnalysis")
DeleteCampaign = Action("DeleteCampaign")
DeleteFinding = Action("DeleteFinding")
DeleteKnowledgeItem = Action("DeleteKnowledgeItem")
DeleteRemediation = Action("DeleteRemediation")
DeleteRepository = Action("DeleteRepository")
DeleteSource = Action("DeleteSource")
DeleteTransformationPackage = Action("DeleteTransformationPackage")
ExecuteTransformation = Action("ExecuteTransformation")
GetAnalysis = Action("GetAnalysis")
GetCampaign = Action("GetCampaign")
GetFinding = Action("GetFinding")
GetFindingGroups = Action("GetFindingGroups")
GetKnowledgeItem = Action("GetKnowledgeItem")
GetRemediation = Action("GetRemediation")
GetRepository = Action("GetRepository")
GetSource = Action("GetSource")
GetTransformationPackageUrl = Action("GetTransformationPackageUrl")
ListAnalyses = Action("ListAnalyses")
ListCampaignRepositories = Action("ListCampaignRepositories")
ListCampaigns = Action("ListCampaigns")
ListFindings = Action("ListFindings")
ListKnowledgeItems = Action("ListKnowledgeItems")
ListRemediations = Action("ListRemediations")
ListRepositories = Action("ListRepositories")
ListSources = Action("ListSources")
ListTagsForResource = Action("ListTagsForResource")
ListTransformationPackageMetadata = Action("ListTransformationPackageMetadata")
ListTransformationPackageShares = Action("ListTransformationPackageShares")
ShareTransformationPackage = Action("ShareTransformationPackage")
TagResource = Action("TagResource")
UnshareTransformationPackage = Action("UnshareTransformationPackage")
UntagResource = Action("UntagResource")
UpdateAnalysis = Action("UpdateAnalysis")
UpdateCampaign = Action("UpdateCampaign")
UpdateCampaignRepositoryStatus = Action("UpdateCampaignRepositoryStatus")
UpdateKnowledgeItemConfiguration = Action("UpdateKnowledgeItemConfiguration")
UpdateKnowledgeItemStatus = Action("UpdateKnowledgeItemStatus")
UpdateRemediation = Action("UpdateRemediation")
UpdateRepository = Action("UpdateRepository")
UpdateSource = Action("UpdateSource")
