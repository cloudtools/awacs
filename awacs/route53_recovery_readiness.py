# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Recovery Readiness"
prefix = "route53-recovery-readiness"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCell = Action("CreateCell")
CreateCrossAccountAuthorization = Action("CreateCrossAccountAuthorization")
CreateReadinessCheck = Action("CreateReadinessCheck")
CreateRecoveryGroup = Action("CreateRecoveryGroup")
CreateResourceSet = Action("CreateResourceSet")
DeleteCell = Action("DeleteCell")
DeleteCrossAccountAuthorization = Action("DeleteCrossAccountAuthorization")
DeleteReadinessCheck = Action("DeleteReadinessCheck")
DeleteRecoveryGroup = Action("DeleteRecoveryGroup")
DeleteResourceSet = Action("DeleteResourceSet")
GetArchitectureRecommendations = Action("GetArchitectureRecommendations")
GetCell = Action("GetCell")
GetCellReadinessSummary = Action("GetCellReadinessSummary")
GetReadinessCheck = Action("GetReadinessCheck")
GetReadinessCheckResourceStatus = Action("GetReadinessCheckResourceStatus")
GetReadinessCheckStatus = Action("GetReadinessCheckStatus")
GetRecoveryGroup = Action("GetRecoveryGroup")
GetRecoveryGroupReadinessSummary = Action("GetRecoveryGroupReadinessSummary")
GetResourceSet = Action("GetResourceSet")
ListCells = Action("ListCells")
ListCrossAccountAuthorizations = Action("ListCrossAccountAuthorizations")
ListReadinessChecks = Action("ListReadinessChecks")
ListRecoveryGroups = Action("ListRecoveryGroups")
ListResourceSets = Action("ListResourceSets")
ListRules = Action("ListRules")
ListTagsForResources = Action("ListTagsForResources")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCell = Action("UpdateCell")
UpdateReadinessCheck = Action("UpdateReadinessCheck")
UpdateRecoveryGroup = Action("UpdateRecoveryGroup")
UpdateResourceSet = Action("UpdateResourceSet")
