# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Payments"
prefix = "payments"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptFinancingApplicationTerms = Action("AcceptFinancingApplicationTerms")
CreateFinancingApplication = Action("CreateFinancingApplication")
CreatePaymentInstrument = Action("CreatePaymentInstrument")
DeletePaymentInstrument = Action("DeletePaymentInstrument")
GetFinancingApplication = Action("GetFinancingApplication")
GetFinancingLine = Action("GetFinancingLine")
GetFinancingLineWithdrawal = Action("GetFinancingLineWithdrawal")
GetFinancingOption = Action("GetFinancingOption")
GetPaymentInstrument = Action("GetPaymentInstrument")
GetPaymentStatus = Action("GetPaymentStatus")
ListFinancingApplications = Action("ListFinancingApplications")
ListFinancingLineWithdrawals = Action("ListFinancingLineWithdrawals")
ListFinancingLines = Action("ListFinancingLines")
ListPaymentInstruments = Action("ListPaymentInstruments")
ListPaymentPreferences = Action("ListPaymentPreferences")
ListPaymentProgramOptions = Action("ListPaymentProgramOptions")
ListPaymentProgramStatus = Action("ListPaymentProgramStatus")
ListTagsForResource = Action("ListTagsForResource")
MakePayment = Action("MakePayment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFinancingApplication = Action("UpdateFinancingApplication")
UpdatePaymentInstrument = Action("UpdatePaymentInstrument")
UpdatePaymentPreferences = Action("UpdatePaymentPreferences")
