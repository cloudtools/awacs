# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Artifact"
prefix = "artifact"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAgreement = Action("AcceptAgreement")
AcceptNdaForAgreement = Action("AcceptNdaForAgreement")
DownloadAgreement = Action("DownloadAgreement")
Get = Action("Get")
GetAccountSettings = Action("GetAccountSettings")
GetAgreement = Action("GetAgreement")
GetCustomerAgreement = Action("GetCustomerAgreement")
GetNdaForAgreement = Action("GetNdaForAgreement")
GetReport = Action("GetReport")
GetReportMetadata = Action("GetReportMetadata")
GetTermForReport = Action("GetTermForReport")
ListAgreements = Action("ListAgreements")
ListCustomerAgreements = Action("ListCustomerAgreements")
ListReports = Action("ListReports")
PutAccountSettings = Action("PutAccountSettings")
TerminateAgreement = Action("TerminateAgreement")
