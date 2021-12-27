# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Outposts"
prefix = "outposts"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelOrder = Action("CancelOrder")
CreateOrder = Action("CreateOrder")
CreateOutpost = Action("CreateOutpost")
CreateSite = Action("CreateSite")
DeleteOutpost = Action("DeleteOutpost")
DeleteSite = Action("DeleteSite")
GetCatalogItem = Action("GetCatalogItem")
GetOutpost = Action("GetOutpost")
GetOutpostInstanceTypes = Action("GetOutpostInstanceTypes")
GetSite = Action("GetSite")
GetSiteAddress = Action("GetSiteAddress")
ListCatalogItems = Action("ListCatalogItems")
ListOrders = Action("ListOrders")
ListOutposts = Action("ListOutposts")
ListSites = Action("ListSites")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateOutpost = Action("UpdateOutpost")
UpdateSite = Action("UpdateSite")
UpdateSiteAddress = Action("UpdateSiteAddress")
UpdateSiteRackPhysicalProperties = Action("UpdateSiteRackPhysicalProperties")
