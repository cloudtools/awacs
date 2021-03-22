# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Budget Service"
prefix = "budgets"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBudgetAction = Action("CreateBudgetAction")
DeleteBudgetAction = Action("DeleteBudgetAction")
DescribeBudgetAction = Action("DescribeBudgetAction")
DescribeBudgetActionHistories = Action("DescribeBudgetActionHistories")
DescribeBudgetActionsForAccount = Action("DescribeBudgetActionsForAccount")
DescribeBudgetActionsForBudget = Action("DescribeBudgetActionsForBudget")
ExecuteBudgetAction = Action("ExecuteBudgetAction")
ModifyBudget = Action("ModifyBudget")
UpdateBudgetAction = Action("UpdateBudgetAction")
ViewBudget = Action("ViewBudget")
