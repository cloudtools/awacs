# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support Plans"
prefix = "supportplans"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptSupportAgreement = Action("AcceptSupportAgreement")
CancelSupportAgreement = Action("CancelSupportAgreement")
CreateSupportAgreement = Action("CreateSupportAgreement")
CreateSupportPlanSchedule = Action("CreateSupportPlanSchedule")
GetSupportAgreement = Action("GetSupportAgreement")
GetSupportPlan = Action("GetSupportPlan")
GetSupportPlanUpdateStatus = Action("GetSupportPlanUpdateStatus")
ListSupportAgreementRevisions = Action("ListSupportAgreementRevisions")
ListSupportAgreements = Action("ListSupportAgreements")
ListSupportPlanModifiers = Action("ListSupportPlanModifiers")
RejectSupportAgreement = Action("RejectSupportAgreement")
StartSupportPlanUpdate = Action("StartSupportPlanUpdate")
UpdateSupportAgreement = Action("UpdateSupportAgreement")
