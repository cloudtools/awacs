# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Invoicing Service"
prefix = "invoicing"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetInvoiceProfile = Action("BatchGetInvoiceProfile")
CreateInvoiceUnit = Action("CreateInvoiceUnit")
DeleteInvoiceUnit = Action("DeleteInvoiceUnit")
GetInvoiceEmailDeliveryPreferences = Action("GetInvoiceEmailDeliveryPreferences")
GetInvoicePDF = Action("GetInvoicePDF")
GetInvoiceUnit = Action("GetInvoiceUnit")
ListInvoiceSummaries = Action("ListInvoiceSummaries")
ListInvoiceUnits = Action("ListInvoiceUnits")
ListTagsForResource = Action("ListTagsForResource")
PutInvoiceEmailDeliveryPreferences = Action("PutInvoiceEmailDeliveryPreferences")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateInvoiceUnit = Action("UpdateInvoiceUnit")
