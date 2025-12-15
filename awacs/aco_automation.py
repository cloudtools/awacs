# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Compute Optimizer Automation"
prefix = "aco-automation"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAccounts = Action("AssociateAccounts")
CreateAutomationRule = Action("CreateAutomationRule")
DeleteAutomationRule = Action("DeleteAutomationRule")
DisassociateAccounts = Action("DisassociateAccounts")
GetAutomationEvent = Action("GetAutomationEvent")
GetAutomationRule = Action("GetAutomationRule")
GetEnrollmentConfiguration = Action("GetEnrollmentConfiguration")
ListAccounts = Action("ListAccounts")
ListAutomationEventSteps = Action("ListAutomationEventSteps")
ListAutomationEventSummaries = Action("ListAutomationEventSummaries")
ListAutomationEvents = Action("ListAutomationEvents")
ListAutomationRulePreview = Action("ListAutomationRulePreview")
ListAutomationRulePreviewSummaries = Action("ListAutomationRulePreviewSummaries")
ListAutomationRules = Action("ListAutomationRules")
ListRecommendedActionSummaries = Action("ListRecommendedActionSummaries")
ListRecommendedActions = Action("ListRecommendedActions")
ListTagsForResource = Action("ListTagsForResource")
RollbackAutomationEvent = Action("RollbackAutomationEvent")
StartAutomationEvent = Action("StartAutomationEvent")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAutomationRule = Action("UpdateAutomationRule")
UpdateEnrollmentConfiguration = Action("UpdateEnrollmentConfiguration")
