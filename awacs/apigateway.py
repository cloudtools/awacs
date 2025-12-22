# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon API Gateway Management"
prefix = "apigateway"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddCertificateToDomain = Action("AddCertificateToDomain")
CreateAccessAssociation = Action("CreateAccessAssociation")
CreatePortal = Action("CreatePortal")
CreatePortalProduct = Action("CreatePortalProduct")
CreateProductPage = Action("CreateProductPage")
CreateProductRestEndpointPage = Action("CreateProductRestEndpointPage")
CreateRoutingRule = Action("CreateRoutingRule")
DELETE = Action("DELETE")
DeletePortal = Action("DeletePortal")
DeletePortalProduct = Action("DeletePortalProduct")
DeletePortalProductSharingPolicy = Action("DeletePortalProductSharingPolicy")
DeleteProductPage = Action("DeleteProductPage")
DeleteProductRestEndpointPage = Action("DeleteProductRestEndpointPage")
DeleteRoutingRule = Action("DeleteRoutingRule")
DisablePortal = Action("DisablePortal")
GET = Action("GET")
GetPortal = Action("GetPortal")
GetPortalProduct = Action("GetPortalProduct")
GetPortalProductSharingPolicy = Action("GetPortalProductSharingPolicy")
GetProductPage = Action("GetProductPage")
GetProductRestEndpointPage = Action("GetProductRestEndpointPage")
GetRoutingRule = Action("GetRoutingRule")
HEAD = Action("HEAD")
ListPortalProducts = Action("ListPortalProducts")
ListPortals = Action("ListPortals")
ListProductPages = Action("ListProductPages")
ListProductRestEndpointPages = Action("ListProductRestEndpointPages")
ListRoutingRule = Action("ListRoutingRule")
ListRoutingRules = Action("ListRoutingRules")
OPTIONS = Action("OPTIONS")
PATCH = Action("PATCH")
POST = Action("POST")
PUT = Action("PUT")
PreviewPortal = Action("PreviewPortal")
PublishPortal = Action("PublishPortal")
PutPortalProductSharingPolicy = Action("PutPortalProductSharingPolicy")
RejectAccessAssociation = Action("RejectAccessAssociation")
RemoveCertificateFromDomain = Action("RemoveCertificateFromDomain")
SetWebACL = Action("SetWebACL")
UpdateDomainNameManagementPolicy = Action("UpdateDomainNameManagementPolicy")
UpdateDomainNamePolicy = Action("UpdateDomainNamePolicy")
UpdatePortal = Action("UpdatePortal")
UpdatePortalProduct = Action("UpdatePortalProduct")
UpdateProductPage = Action("UpdateProductPage")
UpdateProductRestEndpointPage = Action("UpdateProductRestEndpointPage")
UpdateRestApiPolicy = Action("UpdateRestApiPolicy")
UpdateRoutingRule = Action("UpdateRoutingRule")
