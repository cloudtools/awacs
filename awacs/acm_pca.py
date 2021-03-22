# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Certificate Manager Private Certificate Authority"
prefix = "acm-pca"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCertificateAuthority = Action("CreateCertificateAuthority")
CreateCertificateAuthorityAuditReport = Action("CreateCertificateAuthorityAuditReport")
CreatePermission = Action("CreatePermission")
DeleteCertificateAuthority = Action("DeleteCertificateAuthority")
DeletePermission = Action("DeletePermission")
DeletePolicy = Action("DeletePolicy")
DescribeCertificateAuthority = Action("DescribeCertificateAuthority")
DescribeCertificateAuthorityAuditReport = Action(
    "DescribeCertificateAuthorityAuditReport"
)
GetCertificate = Action("GetCertificate")
GetCertificateAuthorityCertificate = Action("GetCertificateAuthorityCertificate")
GetCertificateAuthorityCsr = Action("GetCertificateAuthorityCsr")
GetPolicy = Action("GetPolicy")
ImportCertificateAuthorityCertificate = Action("ImportCertificateAuthorityCertificate")
IssueCertificate = Action("IssueCertificate")
ListCertificateAuthorities = Action("ListCertificateAuthorities")
ListPermissions = Action("ListPermissions")
ListTags = Action("ListTags")
PutPolicy = Action("PutPolicy")
RestoreCertificateAuthority = Action("RestoreCertificateAuthority")
RevokeCertificate = Action("RevokeCertificate")
TagCertificateAuthority = Action("TagCertificateAuthority")
UntagCertificateAuthority = Action("UntagCertificateAuthority")
UpdateCertificateAuthority = Action("UpdateCertificateAuthority")
