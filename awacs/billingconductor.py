# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Billing Conductor"
prefix = "billingconductor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAccounts = Action("AssociateAccounts")
AssociatePricingRules = Action("AssociatePricingRules")
BatchAssociateResourcesToCustomLineItem = Action(
    "BatchAssociateResourcesToCustomLineItem"
)
BatchDisassociateResourcesFromCustomLineItem = Action(
    "BatchDisassociateResourcesFromCustomLineItem"
)
CreateBillingGroup = Action("CreateBillingGroup")
CreateCustomLineItem = Action("CreateCustomLineItem")
CreatePricingPlan = Action("CreatePricingPlan")
CreatePricingRule = Action("CreatePricingRule")
DeleteBillingGroup = Action("DeleteBillingGroup")
DeleteCustomLineItem = Action("DeleteCustomLineItem")
DeletePricingPlan = Action("DeletePricingPlan")
DeletePricingRule = Action("DeletePricingRule")
DisassociateAccounts = Action("DisassociateAccounts")
DisassociatePricingRules = Action("DisassociatePricingRules")
GetBillingGroupCostReport = Action("GetBillingGroupCostReport")
ListAccountAssociations = Action("ListAccountAssociations")
ListBillingGroupCostReports = Action("ListBillingGroupCostReports")
ListBillingGroups = Action("ListBillingGroups")
ListCustomLineItemVersions = Action("ListCustomLineItemVersions")
ListCustomLineItems = Action("ListCustomLineItems")
ListPricingPlans = Action("ListPricingPlans")
ListPricingPlansAssociatedWithPricingRule = Action(
    "ListPricingPlansAssociatedWithPricingRule"
)
ListPricingRules = Action("ListPricingRules")
ListPricingRulesAssociatedToPricingPlan = Action(
    "ListPricingRulesAssociatedToPricingPlan"
)
ListResourcesAssociatedToCustomLineItem = Action(
    "ListResourcesAssociatedToCustomLineItem"
)
ListTagsForResource = Action("ListTagsForResource")
ListTagsResource = Action("ListTagsResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBillingGroup = Action("UpdateBillingGroup")
UpdateCustomLineItem = Action("UpdateCustomLineItem")
UpdatePricingPlan = Action("UpdatePricingPlan")
UpdatePricingRule = Action("UpdatePricingRule")
