# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental Appliances and Software"
prefix = "elemental-appliances-software"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CompleteUpload = Action("CompleteUpload")
CreateOrderV1 = Action("CreateOrderV1")
CreateQuote = Action("CreateQuote")
GetAvsCorrectAddress = Action("GetAvsCorrectAddress")
GetBillingAddresses = Action("GetBillingAddresses")
GetDeliveryAddressesV2 = Action("GetDeliveryAddressesV2")
GetOrder = Action("GetOrder")
GetOrdersV2 = Action("GetOrdersV2")
GetQuote = Action("GetQuote")
GetTaxes = Action("GetTaxes")
ListQuotes = Action("ListQuotes")
ListTagsForResource = Action("ListTagsForResource")
StartUpload = Action("StartUpload")
SubmitOrderV1 = Action("SubmitOrderV1")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateQuote = Action("UpdateQuote")
