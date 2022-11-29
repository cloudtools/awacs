# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CodeGuru Reviewer"
prefix = "codeguru-reviewer"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateRepository = Action("AssociateRepository")
CreateCodeReview = Action("CreateCodeReview")
CreateConnectionToken = Action("CreateConnectionToken")
DescribeCodeReview = Action("DescribeCodeReview")
DescribeRecommendationFeedback = Action("DescribeRecommendationFeedback")
DescribeRepositoryAssociation = Action("DescribeRepositoryAssociation")
DisassociateRepository = Action("DisassociateRepository")
GetMetricsData = Action("GetMetricsData")
ListCodeReviews = Action("ListCodeReviews")
ListRecommendationFeedback = Action("ListRecommendationFeedback")
ListRecommendations = Action("ListRecommendations")
ListRepositoryAssociations = Action("ListRepositoryAssociations")
ListTagsForResource = Action("ListTagsForResource")
ListThirdPartyRepositories = Action("ListThirdPartyRepositories")
PutRecommendationFeedback = Action("PutRecommendationFeedback")
TagResource = Action("TagResource")
UnTagResource = Action("UnTagResource")
