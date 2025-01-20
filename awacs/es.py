# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon OpenSearch Service"
prefix = "es"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
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
AddDataSource = Action("AddDataSource")
AddDirectQueryDataSource = Action("AddDirectQueryDataSource")
AddTags = Action("AddTags")
AssociatePackage = Action("AssociatePackage")
AssociatePackages = Action("AssociatePackages")
AuthorizeVpcEndpointAccess = Action("AuthorizeVpcEndpointAccess")
CancelDomainConfigChange = Action("CancelDomainConfigChange")
CancelElasticsearchServiceSoftwareUpdate = Action(
    "CancelElasticsearchServiceSoftwareUpdate"
)
CancelServiceSoftwareUpdate = Action("CancelServiceSoftwareUpdate")
CreateApplication = Action("CreateApplication")
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
CreateVpcEndpoint = Action("CreateVpcEndpoint")
DeleteApplication = Action("DeleteApplication")
DeleteDataPrepperPipeline = Action("DeleteDataPrepperPipeline")
DeleteDataSource = Action("DeleteDataSource")
DeleteDirectQueryDataSource = Action("DeleteDirectQueryDataSource")
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
DeleteVpcEndpoint = Action("DeleteVpcEndpoint")
DescribeDataPrepperPipeline = Action("DescribeDataPrepperPipeline")
DescribeDomain = Action("DescribeDomain")
DescribeDomainAutoTunes = Action("DescribeDomainAutoTunes")
DescribeDomainChangeProgress = Action("DescribeDomainChangeProgress")
DescribeDomainConfig = Action("DescribeDomainConfig")
DescribeDomainHealth = Action("DescribeDomainHealth")
DescribeDomainNodes = Action("DescribeDomainNodes")
DescribeDomains = Action("DescribeDomains")
DescribeDryRunProgress = Action("DescribeDryRunProgress")
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
DescribeVpcEndpoints = Action("DescribeVpcEndpoints")
DissociatePackage = Action("DissociatePackage")
DissociatePackages = Action("DissociatePackages")
ESCrossClusterGet = Action("ESCrossClusterGet")
ESHttpDelete = Action("ESHttpDelete")
ESHttpGet = Action("ESHttpGet")
ESHttpHead = Action("ESHttpHead")
ESHttpPatch = Action("ESHttpPatch")
ESHttpPost = Action("ESHttpPost")
ESHttpPut = Action("ESHttpPut")
GetApplication = Action("GetApplication")
GetCompatibleElasticsearchVersions = Action("GetCompatibleElasticsearchVersions")
GetCompatibleVersions = Action("GetCompatibleVersions")
GetDataSource = Action("GetDataSource")
GetDirectQueryDataSource = Action("GetDirectQueryDataSource")
GetDomainMaintenanceStatus = Action("GetDomainMaintenanceStatus")
GetPackageVersionHistory = Action("GetPackageVersionHistory")
GetUpgradeHistory = Action("GetUpgradeHistory")
GetUpgradeStatus = Action("GetUpgradeStatus")
IngestDataPrepperPipeline = Action("IngestDataPrepperPipeline")
ListApplications = Action("ListApplications")
ListDataPrepperPipelines = Action("ListDataPrepperPipelines")
ListDataSources = Action("ListDataSources")
ListDirectQueryDataSources = Action("ListDirectQueryDataSources")
ListDomainMaintenances = Action("ListDomainMaintenances")
ListDomainNames = Action("ListDomainNames")
ListDomainsForPackage = Action("ListDomainsForPackage")
ListElasticsearchInstanceTypeDetails = Action("ListElasticsearchInstanceTypeDetails")
ListElasticsearchInstanceTypes = Action("ListElasticsearchInstanceTypes")
ListElasticsearchVersions = Action("ListElasticsearchVersions")
ListInstanceTypeDetails = Action("ListInstanceTypeDetails")
ListInstanceTypes = Action("ListInstanceTypes")
ListPackagesForDomain = Action("ListPackagesForDomain")
ListScheduledActions = Action("ListScheduledActions")
ListTags = Action("ListTags")
ListVersions = Action("ListVersions")
ListVpcEndpointAccess = Action("ListVpcEndpointAccess")
ListVpcEndpoints = Action("ListVpcEndpoints")
ListVpcEndpointsForDomain = Action("ListVpcEndpointsForDomain")
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
RevokeVpcEndpointAccess = Action("RevokeVpcEndpointAccess")
StartDomainMaintenance = Action("StartDomainMaintenance")
StartElasticsearchServiceSoftwareUpdate = Action(
    "StartElasticsearchServiceSoftwareUpdate"
)
StartServiceSoftwareUpdate = Action("StartServiceSoftwareUpdate")
UpdateApplication = Action("UpdateApplication")
UpdateDataPrepperPipeline = Action("UpdateDataPrepperPipeline")
UpdateDataSource = Action("UpdateDataSource")
UpdateDirectQueryDataSource = Action("UpdateDirectQueryDataSource")
UpdateDomainConfig = Action("UpdateDomainConfig")
UpdateElasticsearchDomainConfig = Action("UpdateElasticsearchDomainConfig")
UpdatePackage = Action("UpdatePackage")
UpdatePackageScope = Action("UpdatePackageScope")
UpdateScheduledAction = Action("UpdateScheduledAction")
UpdateVpcEndpoint = Action("UpdateVpcEndpoint")
UpgradeDomain = Action("UpgradeDomain")
UpgradeElasticsearchDomain = Action("UpgradeElasticsearchDomain")
