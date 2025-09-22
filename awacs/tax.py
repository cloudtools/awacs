# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Tax Settings"
prefix = "tax"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchDeleteTaxRegistration = Action("BatchDeleteTaxRegistration")
BatchPutTaxRegistration = Action("BatchPutTaxRegistration")
CancelDocument = Action("CancelDocument")
CreateDocument = Action("CreateDocument")
DeleteSupplementalTaxRegistration = Action("DeleteSupplementalTaxRegistration")
DeleteTaxRegistration = Action("DeleteTaxRegistration")
GetDocument = Action("GetDocument")
GetDocumentUploadUrl = Action("GetDocumentUploadUrl")
GetExemptions = Action("GetExemptions")
GetTaxInfoReportingDocument = Action("GetTaxInfoReportingDocument")
GetTaxInheritance = Action("GetTaxInheritance")
GetTaxInterview = Action("GetTaxInterview")
GetTaxRegistration = Action("GetTaxRegistration")
GetTaxRegistrationDocument = Action("GetTaxRegistrationDocument")
ListDocuments = Action("ListDocuments")
ListSupplementalTaxRegistrations = Action("ListSupplementalTaxRegistrations")
ListTaxRegistrations = Action("ListTaxRegistrations")
ListWithholdingEligibleInvoices = Action("ListWithholdingEligibleInvoices")
PutSupplementalTaxRegistration = Action("PutSupplementalTaxRegistration")
PutTaxInheritance = Action("PutTaxInheritance")
PutTaxInterview = Action("PutTaxInterview")
PutTaxRegistration = Action("PutTaxRegistration")
UpdateExemptions = Action("UpdateExemptions")
