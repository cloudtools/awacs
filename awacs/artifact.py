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
CreateComplianceInquiry = Action("CreateComplianceInquiry")
DownloadAgreement = Action("DownloadAgreement")
ExportComplianceInquiry = Action("ExportComplianceInquiry")
Get = Action("Get")
GetAccountSettings = Action("GetAccountSettings")
GetAgreement = Action("GetAgreement")
GetComplianceInquiryMetadata = Action("GetComplianceInquiryMetadata")
GetCustomerAgreement = Action("GetCustomerAgreement")
GetNdaForAgreement = Action("GetNdaForAgreement")
GetReport = Action("GetReport")
GetReportMetadata = Action("GetReportMetadata")
GetTermForReport = Action("GetTermForReport")
ListAgreements = Action("ListAgreements")
ListComplianceInquiries = Action("ListComplianceInquiries")
ListComplianceInquiryQueries = Action("ListComplianceInquiryQueries")
ListCustomerAgreements = Action("ListCustomerAgreements")
ListReportVersions = Action("ListReportVersions")
ListReports = Action("ListReports")
ListTagsForResource = Action("ListTagsForResource")
PutAccountSettings = Action("PutAccountSettings")
PutComplianceInquiryFeedback = Action("PutComplianceInquiryFeedback")
TagResource = Action("TagResource")
TerminateAgreement = Action("TerminateAgreement")
UntagResource = Action("UntagResource")
