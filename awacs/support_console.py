# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support Console"
prefix = "support-console"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CheckSubscription = Action("CheckSubscription")
CreateCaseDraft = Action("CreateCaseDraft")
CreateContact = Action("CreateContact")
DeleteCaseDraft = Action("DeleteCaseDraft")
DescribeDynamicHelp = Action("DescribeDynamicHelp")
GetAccountGovCloudEnabled = Action("GetAccountGovCloudEnabled")
GetAccountState = Action("GetAccountState")
GetBanner = Action("GetBanner")
GetCaseDraft = Action("GetCaseDraft")
GetQuestionnaire = Action("GetQuestionnaire")
SaveFeedback = Action("SaveFeedback")
