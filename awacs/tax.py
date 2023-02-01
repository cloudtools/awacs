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


BatchPutTaxRegistration = Action("BatchPutTaxRegistration")
DeleteTaxRegistration = Action("DeleteTaxRegistration")
GetExemptions = Action("GetExemptions")
GetTaxInheritance = Action("GetTaxInheritance")
GetTaxInterview = Action("GetTaxInterview")
GetTaxRegistration = Action("GetTaxRegistration")
GetTaxRegistrationDocument = Action("GetTaxRegistrationDocument")
ListTaxRegistrations = Action("ListTaxRegistrations")
PutTaxInheritance = Action("PutTaxInheritance")
PutTaxInterview = Action("PutTaxInterview")
PutTaxRegistration = Action("PutTaxRegistration")
UpdateExemptions = Action("UpdateExemptions")
