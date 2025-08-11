# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Observability Admin Service"
prefix = "observabilityadmin"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateTelemetryRule = Action("CreateTelemetryRule")
CreateTelemetryRuleForOrganization = Action("CreateTelemetryRuleForOrganization")
DeleteTelemetryRule = Action("DeleteTelemetryRule")
DeleteTelemetryRuleForOrganization = Action("DeleteTelemetryRuleForOrganization")
GetTelemetryEvaluationStatus = Action("GetTelemetryEvaluationStatus")
GetTelemetryEvaluationStatusForOrganization = Action(
    "GetTelemetryEvaluationStatusForOrganization"
)
GetTelemetryRule = Action("GetTelemetryRule")
GetTelemetryRuleForOrganization = Action("GetTelemetryRuleForOrganization")
ListResourceTelemetry = Action("ListResourceTelemetry")
ListResourceTelemetryForOrganization = Action("ListResourceTelemetryForOrganization")
ListTagsForResource = Action("ListTagsForResource")
ListTelemetryRules = Action("ListTelemetryRules")
ListTelemetryRulesForOrganization = Action("ListTelemetryRulesForOrganization")
StartTelemetryEvaluation = Action("StartTelemetryEvaluation")
StartTelemetryEvaluationForOrganization = Action(
    "StartTelemetryEvaluationForOrganization"
)
StopTelemetryEvaluation = Action("StopTelemetryEvaluation")
StopTelemetryEvaluationForOrganization = Action(
    "StopTelemetryEvaluationForOrganization"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTelemetryRule = Action("UpdateTelemetryRule")
UpdateTelemetryRuleForOrganization = Action("UpdateTelemetryRuleForOrganization")
