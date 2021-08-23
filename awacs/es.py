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


AcceptInboundConnection = Action("AcceptInboundConnection")
AcceptInboundCrossClusterSearchConnection = Action(
    "AcceptInboundCrossClusterSearchConnection"
)
AddTags = Action("AddTags")
AssociatePackage = Action("AssociatePackage")
CancelElasticsearchServiceSoftwareUpdate = Action(
    "CancelElasticsearchServiceSoftwareUpdate"
)
CreateDataPrepperPipeline = Action("CreateDataPrepperPipeline")
CreateDomain = Action("CreateDomain")
CreateElasticsearchDomain = Action("CreateElasticsearchDomain")
CreateElasticsearchServiceRole = Action("CreateElasticsearchServiceRole")
CreateOutboundConnection = Action("CreateOutboundConnection")
CreateOutboundCrossClusterSearchConnection = Action(
    "CreateOutboundCrossClusterSearchConnection"
)
CreatePackage = Action("CreatePackage")
CreateServiceRole = Action("CreateServiceRole")
DeleteDataPrepperPipeline = Action("DeleteDataPrepperPipeline")
DeleteDomain = Action("DeleteDomain")
DeleteElasticsearchDomain = Action("DeleteElasticsearchDomain")
DeleteElasticsearchServiceRole = Action("DeleteElasticsearchServiceRole")
DeleteInboundConnection = Action("DeleteInboundConnection")
DeleteInboundCrossClusterSearchConnection = Action(
    "DeleteInboundCrossClusterSearchConnection"
)
DeleteOutboundConnection = Action("DeleteOutboundConnection")
DeleteOutboundCrossClusterSearchConnection = Action(
    "DeleteOutboundCrossClusterSearchConnection"
)
DeletePackage = Action("DeletePackage")
DescribeDataPrepperPipeline = Action("DescribeDataPrepperPipeline")
DescribeDomain = Action("DescribeDomain")
DescribeDomainConfig = Action("DescribeDomainConfig")
DescribeDomains = Action("DescribeDomains")
DescribeElasticsearchDomain = Action("DescribeElasticsearchDomain")
DescribeElasticsearchDomainConfig = Action("DescribeElasticsearchDomainConfig")
DescribeElasticsearchDomains = Action("DescribeElasticsearchDomains")
DescribeElasticsearchInstanceTypeLimits = Action(
    "DescribeElasticsearchInstanceTypeLimits"
)
DescribeInboundConnections = Action("DescribeInboundConnections")
DescribeInboundCrossClusterSearchConnections = Action(
    "DescribeInboundCrossClusterSearchConnections"
)
DescribeInstanceTypeLimits = Action("DescribeInstanceTypeLimits")
DescribeOutboundConnections = Action("DescribeOutboundConnections")
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
DescribeReservedInstanceOfferings = Action("DescribeReservedInstanceOfferings")
DescribeReservedInstances = Action("DescribeReservedInstances")
DissociatePackage = Action("DissociatePackage")
ESCrossClusterGet = Action("ESCrossClusterGet")
ESHttpDelete = Action("ESHttpDelete")
ESHttpGet = Action("ESHttpGet")
ESHttpHead = Action("ESHttpHead")
ESHttpPatch = Action("ESHttpPatch")
ESHttpPost = Action("ESHttpPost")
ESHttpPut = Action("ESHttpPut")
GetCompatibleElasticsearchVersions = Action("GetCompatibleElasticsearchVersions")
GetCompatibleVersions = Action("GetCompatibleVersions")
GetPackageVersionHistory = Action("GetPackageVersionHistory")
GetUpgradeHistory = Action("GetUpgradeHistory")
GetUpgradeStatus = Action("GetUpgradeStatus")
IngestDataPrepperPipeline = Action("IngestDataPrepperPipeline")
ListDataPrepperPipelines = Action("ListDataPrepperPipelines")
ListDomainNames = Action("ListDomainNames")
ListDomainsForPackage = Action("ListDomainsForPackage")
ListElasticsearchInstanceTypeDetails = Action("ListElasticsearchInstanceTypeDetails")
ListElasticsearchInstanceTypes = Action("ListElasticsearchInstanceTypes")
ListElasticsearchVersions = Action("ListElasticsearchVersions")
ListInstanceTypeDetails = Action("ListInstanceTypeDetails")
ListInstanceTypes = Action("ListInstanceTypes")
ListPackagesForDomain = Action("ListPackagesForDomain")
ListTags = Action("ListTags")
ListVersions = Action("ListVersions")
PurchaseReservedElasticsearchInstance = Action("PurchaseReservedElasticsearchInstance")
PurchaseReservedElasticsearchInstanceOffering = Action(
    "PurchaseReservedElasticsearchInstanceOffering"
)
PurchaseReservedInstanceOffering = Action("PurchaseReservedInstanceOffering")
RejectInboundConnection = Action("RejectInboundConnection")
RejectInboundCrossClusterSearchConnection = Action(
    "RejectInboundCrossClusterSearchConnection"
)
RemoveTags = Action("RemoveTags")
StartElasticsearchServiceSoftwareUpdate = Action(
    "StartElasticsearchServiceSoftwareUpdate"
)
UpdateDataPrepperPipeline = Action("UpdateDataPrepperPipeline")
UpdateDomainConfig = Action("UpdateDomainConfig")
UpdateElasticsearchDomainConfig = Action("UpdateElasticsearchDomainConfig")
UpdatePackage = Action("UpdatePackage")
UpgradeElasticsearchDomain = Action("UpgradeElasticsearchDomain")
