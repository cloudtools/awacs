# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Certificate Manager"
prefix = "acm"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToCertificate = Action("AddTagsToCertificate")
DeleteCertificate = Action("DeleteCertificate")
DescribeCertificate = Action("DescribeCertificate")
ExportCertificate = Action("ExportCertificate")
GetAccountConfiguration = Action("GetAccountConfiguration")
GetCertificate = Action("GetCertificate")
ImportCertificate = Action("ImportCertificate")
ListCertificates = Action("ListCertificates")
ListTagsForCertificate = Action("ListTagsForCertificate")
PutAccountConfiguration = Action("PutAccountConfiguration")
RemoveTagsFromCertificate = Action("RemoveTagsFromCertificate")
RenewCertificate = Action("RenewCertificate")
RequestCertificate = Action("RequestCertificate")
ResendValidationEmail = Action("ResendValidationEmail")
UpdateCertificateOptions = Action("UpdateCertificateOptions")
