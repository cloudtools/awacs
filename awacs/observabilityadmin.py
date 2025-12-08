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


CreateCentralizationRuleForOrganization = Action(
    "CreateCentralizationRuleForOrganization"
)
CreateS3TableIntegration = Action("CreateS3TableIntegration")
CreateTelemetryPipeline = Action("CreateTelemetryPipeline")
CreateTelemetryRule = Action("CreateTelemetryRule")
CreateTelemetryRuleForOrganization = Action("CreateTelemetryRuleForOrganization")
DeleteCentralizationRuleForOrganization = Action(
    "DeleteCentralizationRuleForOrganization"
)
DeleteS3TableIntegration = Action("DeleteS3TableIntegration")
DeleteTelemetryPipeline = Action("DeleteTelemetryPipeline")
DeleteTelemetryRule = Action("DeleteTelemetryRule")
DeleteTelemetryRuleForOrganization = Action("DeleteTelemetryRuleForOrganization")
GetCentralizationRuleForOrganization = Action("GetCentralizationRuleForOrganization")
GetS3TableIntegration = Action("GetS3TableIntegration")
GetTelemetryEnrichmentStatus = Action("GetTelemetryEnrichmentStatus")
GetTelemetryEvaluationStatus = Action("GetTelemetryEvaluationStatus")
GetTelemetryEvaluationStatusForOrganization = Action(
    "GetTelemetryEvaluationStatusForOrganization"
)
GetTelemetryPipeline = Action("GetTelemetryPipeline")
GetTelemetryRule = Action("GetTelemetryRule")
GetTelemetryRuleForOrganization = Action("GetTelemetryRuleForOrganization")
ListCentralizationRulesForOrganization = Action(
    "ListCentralizationRulesForOrganization"
)
ListResourceTelemetry = Action("ListResourceTelemetry")
ListResourceTelemetryForOrganization = Action("ListResourceTelemetryForOrganization")
ListS3TableIntegrations = Action("ListS3TableIntegrations")
ListTagsForResource = Action("ListTagsForResource")
ListTelemetryPipelines = Action("ListTelemetryPipelines")
ListTelemetryRules = Action("ListTelemetryRules")
ListTelemetryRulesForOrganization = Action("ListTelemetryRulesForOrganization")
StartTelemetryEnrichment = Action("StartTelemetryEnrichment")
StartTelemetryEvaluation = Action("StartTelemetryEvaluation")
StartTelemetryEvaluationForOrganization = Action(
    "StartTelemetryEvaluationForOrganization"
)
StopTelemetryEnrichment = Action("StopTelemetryEnrichment")
StopTelemetryEvaluation = Action("StopTelemetryEvaluation")
StopTelemetryEvaluationForOrganization = Action(
    "StopTelemetryEvaluationForOrganization"
)
TagResource = Action("TagResource")
TestTelemetryPipeline = Action("TestTelemetryPipeline")
UntagResource = Action("UntagResource")
UpdateCentralizationRuleForOrganization = Action(
    "UpdateCentralizationRuleForOrganization"
)
UpdateTelemetryPipeline = Action("UpdateTelemetryPipeline")
UpdateTelemetryRule = Action("UpdateTelemetryRule")
UpdateTelemetryRuleForOrganization = Action("UpdateTelemetryRuleForOrganization")
ValidateTelemetryPipelineConfiguration = Action(
    "ValidateTelemetryPipelineConfiguration"
)
