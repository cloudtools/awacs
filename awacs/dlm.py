# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Data Lifecycle Manager"
prefix = "dlm"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateLifecyclePolicy = Action("CreateLifecyclePolicy")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
GetLifecyclePolicies = Action("GetLifecyclePolicies")
GetLifecyclePolicy = Action("GetLifecyclePolicy")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLifecyclePolicy = Action("UpdateLifecyclePolicy")
