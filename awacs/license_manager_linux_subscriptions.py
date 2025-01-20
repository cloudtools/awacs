# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS License Manager Linux Subscriptions Manager"
prefix = "license-manager-linux-subscriptions"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeregisterSubscriptionProvider = Action("DeregisterSubscriptionProvider")
GetRegisteredSubscriptionProvider = Action("GetRegisteredSubscriptionProvider")
GetServiceSettings = Action("GetServiceSettings")
ListLinuxSubscriptionInstances = Action("ListLinuxSubscriptionInstances")
ListLinuxSubscriptions = Action("ListLinuxSubscriptions")
ListRegisteredSubscriptionProviders = Action("ListRegisteredSubscriptionProviders")
ListTagsForResource = Action("ListTagsForResource")
RegisterSubscriptionProvider = Action("RegisterSubscriptionProvider")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateServiceSettings = Action("UpdateServiceSettings")
