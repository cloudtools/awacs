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


DeleteRecommendationPreferences = Action("DeleteRecommendationPreferences")
DescribeRecommendationExportJobs = Action("DescribeRecommendationExportJobs")
ExportAutoScalingGroupRecommendations = Action("ExportAutoScalingGroupRecommendations")
ExportEBSVolumeRecommendations = Action("ExportEBSVolumeRecommendations")
ExportEC2InstanceRecommendations = Action("ExportEC2InstanceRecommendations")
ExportLambdaFunctionRecommendations = Action("ExportLambdaFunctionRecommendations")
GetAutoScalingGroupRecommendations = Action("GetAutoScalingGroupRecommendations")
GetEBSVolumeRecommendations = Action("GetEBSVolumeRecommendations")
GetEC2InstanceRecommendations = Action("GetEC2InstanceRecommendations")
GetEC2RecommendationProjectedMetrics = Action("GetEC2RecommendationProjectedMetrics")
GetEffectiveRecommendationPreferences = Action("GetEffectiveRecommendationPreferences")
GetEnrollmentStatus = Action("GetEnrollmentStatus")
GetEnrollmentStatusesForOrganization = Action("GetEnrollmentStatusesForOrganization")
GetLambdaFunctionRecommendations = Action("GetLambdaFunctionRecommendations")
GetRecommendationPreferences = Action("GetRecommendationPreferences")
GetRecommendationSummaries = Action("GetRecommendationSummaries")
PutRecommendationPreferences = Action("PutRecommendationPreferences")
UpdateEnrollmentStatus = Action("UpdateEnrollmentStatus")
