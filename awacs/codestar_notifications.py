# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodeStar Notifications"
prefix = "codestar-notifications"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateNotificationRule = Action("CreateNotificationRule")
DeleteNotificationRule = Action("DeleteNotificationRule")
DeleteTarget = Action("DeleteTarget")
DescribeNotificationRule = Action("DescribeNotificationRule")
ListEventTypes = Action("ListEventTypes")
ListNotificationRules = Action("ListNotificationRules")
ListTagsForResource = Action("ListTagsForResource")
ListTargets = Action("ListTargets")
Subscribe = Action("Subscribe")
TagResource = Action("TagResource")
Unsubscribe = Action("Unsubscribe")
UntagResource = Action("UntagResource")
UpdateNotificationRule = Action("UpdateNotificationRule")
