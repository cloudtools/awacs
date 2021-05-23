# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elasticsearch Service"
prefix = "es"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptInboundCrossClusterSearchConnection = Action(
    "AcceptInboundCrossClusterSearchConnection"
)
AddTags = Action("AddTags")
AssociatePackage = Action("AssociatePackage")
CancelElasticsearchServiceSoftwareUpdate = Action(
    "CancelElasticsearchServiceSoftwareUpdate"
)
CreateElasticsearchDomain = Action("CreateElasticsearchDomain")
CreateElasticsearchServiceRole = Action("CreateElasticsearchServiceRole")
CreateOutboundCrossClusterSearchConnection = Action(
    "CreateOutboundCrossClusterSearchConnection"
)
CreatePackage = Action("CreatePackage")
DeleteElasticsearchDomain = Action("DeleteElasticsearchDomain")
DeleteElasticsearchServiceRole = Action("DeleteElasticsearchServiceRole")
DeleteInboundCrossClusterSearchConnection = Action(
    "DeleteInboundCrossClusterSearchConnection"
)
DeleteOutboundCrossClusterSearchConnection = Action(
    "DeleteOutboundCrossClusterSearchConnection"
)
DeletePackage = Action("DeletePackage")
DescribeElasticsearchDomain = Action("DescribeElasticsearchDomain")
DescribeElasticsearchDomainConfig = Action("DescribeElasticsearchDomainConfig")
DescribeElasticsearchDomains = Action("DescribeElasticsearchDomains")
DescribeElasticsearchInstanceTypeLimits = Action(
    "DescribeElasticsearchInstanceTypeLimits"
)
DescribeInboundCrossClusterSearchConnections = Action(
    "DescribeInboundCrossClusterSearchConnections"
)
DescribeOutboundCrossClusterSearchConnections = Action(
    "DescribeOutboundCrossClusterSearchConnections"
)
DescribePackages = Action("DescribePackages")
DescribeReservedElasticsearchInstanceOfferings = Action(
    "DescribeReservedElasticsearchInstanceOfferings"
)
DescribeReservedElasticsearchInstances = Action(
    "DescribeReservedElasticsearchInstances"
)
DissociatePackage = Action("DissociatePackage")
ESCrossClusterGet = Action("ESCrossClusterGet")
ESHttpDelete = Action("ESHttpDelete")
ESHttpGet = Action("ESHttpGet")
ESHttpHead = Action("ESHttpHead")
ESHttpPatch = Action("ESHttpPatch")
ESHttpPost = Action("ESHttpPost")
ESHttpPut = Action("ESHttpPut")
GetCompatibleElasticsearchVersions = Action("GetCompatibleElasticsearchVersions")
GetPackageVersionHistory = Action("GetPackageVersionHistory")
GetUpgradeHistory = Action("GetUpgradeHistory")
GetUpgradeStatus = Action("GetUpgradeStatus")
ListDomainNames = Action("ListDomainNames")
ListDomainsForPackage = Action("ListDomainsForPackage")
ListElasticsearchInstanceTypeDetails = Action("ListElasticsearchInstanceTypeDetails")
ListElasticsearchInstanceTypes = Action("ListElasticsearchInstanceTypes")
ListElasticsearchVersions = Action("ListElasticsearchVersions")
ListPackagesForDomain = Action("ListPackagesForDomain")
ListTags = Action("ListTags")
PurchaseReservedElasticsearchInstance = Action("PurchaseReservedElasticsearchInstance")
PurchaseReservedElasticsearchInstanceOffering = Action(
    "PurchaseReservedElasticsearchInstanceOffering"
)
RejectInboundCrossClusterSearchConnection = Action(
    "RejectInboundCrossClusterSearchConnection"
)
RemoveTags = Action("RemoveTags")
StartElasticsearchServiceSoftwareUpdate = Action(
    "StartElasticsearchServiceSoftwareUpdate"
)
UpdateElasticsearchDomainConfig = Action("UpdateElasticsearchDomainConfig")
UpdatePackage = Action("UpdatePackage")
UpgradeElasticsearchDomain = Action("UpgradeElasticsearchDomain")
