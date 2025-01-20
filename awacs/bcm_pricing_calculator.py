# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Billing And Cost Management Pricing Calculator"
prefix = "bcm-pricing-calculator"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBillEstimate = Action("CreateBillEstimate")
CreateBillScenario = Action("CreateBillScenario")
CreateBillScenarioCommitmentModification = Action(
    "CreateBillScenarioCommitmentModification"
)
CreateBillScenarioUsageModification = Action("CreateBillScenarioUsageModification")
CreateWorkloadEstimate = Action("CreateWorkloadEstimate")
CreateWorkloadEstimateUsage = Action("CreateWorkloadEstimateUsage")
DeleteBillEstimate = Action("DeleteBillEstimate")
DeleteBillScenario = Action("DeleteBillScenario")
DeleteBillScenarioCommitmentModification = Action(
    "DeleteBillScenarioCommitmentModification"
)
DeleteBillScenarioUsageModification = Action("DeleteBillScenarioUsageModification")
DeleteWorkloadEstimate = Action("DeleteWorkloadEstimate")
DeleteWorkloadEstimateUsage = Action("DeleteWorkloadEstimateUsage")
GetBillEstimate = Action("GetBillEstimate")
GetBillScenario = Action("GetBillScenario")
GetPreferences = Action("GetPreferences")
GetWorkloadEstimate = Action("GetWorkloadEstimate")
ListBillEstimateCommitments = Action("ListBillEstimateCommitments")
ListBillEstimateInputCommitmentModifications = Action(
    "ListBillEstimateInputCommitmentModifications"
)
ListBillEstimateInputUsageModifications = Action(
    "ListBillEstimateInputUsageModifications"
)
ListBillEstimateLineItems = Action("ListBillEstimateLineItems")
ListBillEstimates = Action("ListBillEstimates")
ListBillScenarioCommitmentModifications = Action(
    "ListBillScenarioCommitmentModifications"
)
ListBillScenarioUsageModifications = Action("ListBillScenarioUsageModifications")
ListBillScenarios = Action("ListBillScenarios")
ListTagsForResource = Action("ListTagsForResource")
ListWorkloadEstimateUsage = Action("ListWorkloadEstimateUsage")
ListWorkloadEstimates = Action("ListWorkloadEstimates")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBillEstimate = Action("UpdateBillEstimate")
UpdateBillScenario = Action("UpdateBillScenario")
UpdateBillScenarioCommitmentModification = Action(
    "UpdateBillScenarioCommitmentModification"
)
UpdateBillScenarioUsageModification = Action("UpdateBillScenarioUsageModification")
UpdatePreferences = Action("UpdatePreferences")
UpdateWorkloadEstimate = Action("UpdateWorkloadEstimate")
UpdateWorkloadEstimateUsage = Action("UpdateWorkloadEstimateUsage")
