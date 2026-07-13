# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support Authorization"
prefix = "supportauthz"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSupportPermit = Action("CreateSupportPermit")
DeleteSupportPermit = Action("DeleteSupportPermit")
GetAction = Action("GetAction")
GetSupportPermit = Action("GetSupportPermit")
ListActions = Action("ListActions")
ListSupportPermitRequests = Action("ListSupportPermitRequests")
ListSupportPermits = Action("ListSupportPermits")
ListTagsForResource = Action("ListTagsForResource")
RegisterKey = Action("RegisterKey")
RejectSupportPermitRequest = Action("RejectSupportPermitRequest")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
