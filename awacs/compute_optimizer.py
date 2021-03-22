# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Compute Optimizer"
prefix = "compute-optimizer"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DescribeRecommendationExportJobs = Action("DescribeRecommendationExportJobs")
ExportAutoScalingGroupRecommendations = Action("ExportAutoScalingGroupRecommendations")
ExportEC2InstanceRecommendations = Action("ExportEC2InstanceRecommendations")
GetAutoScalingGroupRecommendations = Action("GetAutoScalingGroupRecommendations")
GetEBSVolumeRecommendations = Action("GetEBSVolumeRecommendations")
GetEC2InstanceRecommendations = Action("GetEC2InstanceRecommendations")
GetEC2RecommendationProjectedMetrics = Action("GetEC2RecommendationProjectedMetrics")
GetEnrollmentStatus = Action("GetEnrollmentStatus")
GetLambdaFunctionRecommendations = Action("GetLambdaFunctionRecommendations")
GetRecommendationSummaries = Action("GetRecommendationSummaries")
UpdateEnrollmentStatus = Action("UpdateEnrollmentStatus")
