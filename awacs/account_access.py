# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Account access manager"
prefix = "account-access"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApplication = Action("CreateApplication")
CreateEntitlement = Action("CreateEntitlement")
DeleteApplication = Action("DeleteApplication")
DeleteEntitlement = Action("DeleteEntitlement")
GetApplication = Action("GetApplication")
GetEntitlement = Action("GetEntitlement")
ListApplications = Action("ListApplications")
ListEntitlements = Action("ListEntitlements")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
