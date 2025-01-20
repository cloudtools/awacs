# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Account Management"
prefix = "account"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptPrimaryEmailUpdate = Action("AcceptPrimaryEmailUpdate")
CloseAccount = Action("CloseAccount")
DeleteAlternateContact = Action("DeleteAlternateContact")
DisableRegion = Action("DisableRegion")
EnableRegion = Action("EnableRegion")
GetAccountInformation = Action("GetAccountInformation")
GetAlternateContact = Action("GetAlternateContact")
GetChallengeQuestions = Action("GetChallengeQuestions")
GetContactInformation = Action("GetContactInformation")
GetPrimaryEmail = Action("GetPrimaryEmail")
GetRegionOptStatus = Action("GetRegionOptStatus")
ListRegions = Action("ListRegions")
PutAlternateContact = Action("PutAlternateContact")
PutChallengeQuestions = Action("PutChallengeQuestions")
PutContactInformation = Action("PutContactInformation")
StartPrimaryEmailUpdate = Action("StartPrimaryEmailUpdate")
