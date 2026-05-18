# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS RTB Fabric"
prefix = "rtbfabric"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptLink = Action("AcceptLink")
AssociateCertificate = Action("AssociateCertificate")
CreateInboundExternalLink = Action("CreateInboundExternalLink")
CreateLink = Action("CreateLink")
CreateLinkRoutingRule = Action("CreateLinkRoutingRule")
CreateOutboundExternalLink = Action("CreateOutboundExternalLink")
CreateRequesterGateway = Action("CreateRequesterGateway")
CreateResponderGateway = Action("CreateResponderGateway")
DeleteInboundExternalLink = Action("DeleteInboundExternalLink")
DeleteLink = Action("DeleteLink")
DeleteLinkRoutingRule = Action("DeleteLinkRoutingRule")
DeleteOutboundExternalLink = Action("DeleteOutboundExternalLink")
DeleteRequesterGateway = Action("DeleteRequesterGateway")
DeleteResponderGateway = Action("DeleteResponderGateway")
DisassociateCertificate = Action("DisassociateCertificate")
GetCertificateAssociation = Action("GetCertificateAssociation")
GetInboundExternalLink = Action("GetInboundExternalLink")
GetLink = Action("GetLink")
GetLinkRoutingRule = Action("GetLinkRoutingRule")
GetOutboundExternalLink = Action("GetOutboundExternalLink")
GetRequesterGateway = Action("GetRequesterGateway")
GetResponderGateway = Action("GetResponderGateway")
ListCertificateAssociations = Action("ListCertificateAssociations")
ListLinkRoutingRules = Action("ListLinkRoutingRules")
ListLinks = Action("ListLinks")
ListRequesterGateways = Action("ListRequesterGateways")
ListResponderGateways = Action("ListResponderGateways")
ListTagsForResource = Action("ListTagsForResource")
RejectLink = Action("RejectLink")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLink = Action("UpdateLink")
UpdateLinkModuleFlow = Action("UpdateLinkModuleFlow")
UpdateLinkRoutingRule = Action("UpdateLinkRoutingRule")
UpdateRequesterGateway = Action("UpdateRequesterGateway")
UpdateResponderGateway = Action("UpdateResponderGateway")
