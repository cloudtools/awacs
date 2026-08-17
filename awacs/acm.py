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
CreateAcmeDomainValidation = Action("CreateAcmeDomainValidation")
CreateAcmeEndpoint = Action("CreateAcmeEndpoint")
CreateAcmeExternalAccountBinding = Action("CreateAcmeExternalAccountBinding")
DeleteAcmeDomainValidation = Action("DeleteAcmeDomainValidation")
DeleteAcmeEndpoint = Action("DeleteAcmeEndpoint")
DeleteAcmeExternalAccountBinding = Action("DeleteAcmeExternalAccountBinding")
DeleteCertificate = Action("DeleteCertificate")
DescribeAcmeAccount = Action("DescribeAcmeAccount")
DescribeAcmeDomainValidation = Action("DescribeAcmeDomainValidation")
DescribeAcmeEndpoint = Action("DescribeAcmeEndpoint")
DescribeAcmeExternalAccountBinding = Action("DescribeAcmeExternalAccountBinding")
DescribeCertificate = Action("DescribeCertificate")
ExportCertificate = Action("ExportCertificate")
GetAccountConfiguration = Action("GetAccountConfiguration")
GetAcmeExternalAccountBindingCredentials = Action(
    "GetAcmeExternalAccountBindingCredentials"
)
GetCertificate = Action("GetCertificate")
ImportCertificate = Action("ImportCertificate")
ListAcmeAccounts = Action("ListAcmeAccounts")
ListAcmeDomainValidations = Action("ListAcmeDomainValidations")
ListAcmeEndpoints = Action("ListAcmeEndpoints")
ListAcmeExternalAccountBindings = Action("ListAcmeExternalAccountBindings")
ListCertificateDomainValidations = Action("ListCertificateDomainValidations")
ListCertificates = Action("ListCertificates")
ListTagsForCertificate = Action("ListTagsForCertificate")
ListTagsForResource = Action("ListTagsForResource")
PutAccountConfiguration = Action("PutAccountConfiguration")
RemoveTagsFromCertificate = Action("RemoveTagsFromCertificate")
RenewCertificate = Action("RenewCertificate")
RequestCertificate = Action("RequestCertificate")
ResendValidationEmail = Action("ResendValidationEmail")
RevokeAcmeAccount = Action("RevokeAcmeAccount")
RevokeAcmeExternalAccountBinding = Action("RevokeAcmeExternalAccountBinding")
RevokeCertificate = Action("RevokeCertificate")
SearchCertificates = Action("SearchCertificates")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAcmeDomainValidation = Action("UpdateAcmeDomainValidation")
UpdateAcmeEndpoint = Action("UpdateAcmeEndpoint")
UpdateCertificate = Action("UpdateCertificate")
UpdateCertificateOptions = Action("UpdateCertificateOptions")
