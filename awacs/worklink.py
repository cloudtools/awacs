# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkLink"
prefix = "worklink"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateDomain = Action("AssociateDomain")
AssociateWebsiteAuthorizationProvider = Action("AssociateWebsiteAuthorizationProvider")
AssociateWebsiteCertificateAuthority = Action("AssociateWebsiteCertificateAuthority")
CreateFleet = Action("CreateFleet")
DeleteFleet = Action("DeleteFleet")
DescribeAuditStreamConfiguration = Action("DescribeAuditStreamConfiguration")
DescribeCompanyNetworkConfiguration = Action("DescribeCompanyNetworkConfiguration")
DescribeDevice = Action("DescribeDevice")
DescribeDevicePolicyConfiguration = Action("DescribeDevicePolicyConfiguration")
DescribeDomain = Action("DescribeDomain")
DescribeFleetMetadata = Action("DescribeFleetMetadata")
DescribeIdentityProviderConfiguration = Action("DescribeIdentityProviderConfiguration")
DescribeWebsiteCertificateAuthority = Action("DescribeWebsiteCertificateAuthority")
DisassociateDomain = Action("DisassociateDomain")
DisassociateWebsiteAuthorizationProvider = Action(
    "DisassociateWebsiteAuthorizationProvider"
)
DisassociateWebsiteCertificateAuthority = Action(
    "DisassociateWebsiteCertificateAuthority"
)
ListDevices = Action("ListDevices")
ListDomains = Action("ListDomains")
ListFleets = Action("ListFleets")
ListTagsForResource = Action("ListTagsForResource")
ListWebsiteAuthorizationProviders = Action("ListWebsiteAuthorizationProviders")
ListWebsiteCertificateAuthorities = Action("ListWebsiteCertificateAuthorities")
RestoreDomainAccess = Action("RestoreDomainAccess")
RevokeDomainAccess = Action("RevokeDomainAccess")
SearchEntity = Action("SearchEntity")
SignOutUser = Action("SignOutUser")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAuditStreamConfiguration = Action("UpdateAuditStreamConfiguration")
UpdateCompanyNetworkConfiguration = Action("UpdateCompanyNetworkConfiguration")
UpdateDevicePolicyConfiguration = Action("UpdateDevicePolicyConfiguration")
UpdateDomainMetadata = Action("UpdateDomainMetadata")
UpdateFleetMetadata = Action("UpdateFleetMetadata")
UpdateIdentityProviderConfiguration = Action("UpdateIdentityProviderConfiguration")
