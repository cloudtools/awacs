# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Marketplace Management Portal"
prefix = "aws-marketplace-management"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetAdditionalSellerNotificationRecipients = Action(
    "GetAdditionalSellerNotificationRecipients"
)
GetBankAccountVerificationDetails = Action("GetBankAccountVerificationDetails")
GetSecondaryUserVerificationDetails = Action("GetSecondaryUserVerificationDetails")
GetSellerVerificationDetails = Action("GetSellerVerificationDetails")
PutAdditionalSellerNotificationRecipients = Action(
    "PutAdditionalSellerNotificationRecipients"
)
PutBankAccountVerificationDetails = Action("PutBankAccountVerificationDetails")
PutSecondaryUserVerificationDetails = Action("PutSecondaryUserVerificationDetails")
PutSellerVerificationDetails = Action("PutSellerVerificationDetails")
uploadFiles = Action("uploadFiles")
viewMarketing = Action("viewMarketing")
viewReports = Action("viewReports")
viewSettings = Action("viewSettings")
viewSupport = Action("viewSupport")
