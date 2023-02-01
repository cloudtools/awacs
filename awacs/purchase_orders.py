# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Purchase Orders Console"
prefix = "purchase-orders"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddPurchaseOrder = Action("AddPurchaseOrder")
DeletePurchaseOrder = Action("DeletePurchaseOrder")
GetPurchaseOrder = Action("GetPurchaseOrder")
ListPurchaseOrderInvoices = Action("ListPurchaseOrderInvoices")
ListPurchaseOrders = Action("ListPurchaseOrders")
ModifyPurchaseOrders = Action("ModifyPurchaseOrders")
UpdatePurchaseOrder = Action("UpdatePurchaseOrder")
UpdatePurchaseOrderStatus = Action("UpdatePurchaseOrderStatus")
ViewPurchaseOrders = Action("ViewPurchaseOrders")
