# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EC2"
prefix = "ec2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAddressTransfer = Action("AcceptAddressTransfer")
AcceptCapacityReservationBillingOwnership = Action(
    "AcceptCapacityReservationBillingOwnership"
)
AcceptReservedInstancesExchangeQuote = Action("AcceptReservedInstancesExchangeQuote")
AcceptTransitGatewayMulticastDomainAssociations = Action(
    "AcceptTransitGatewayMulticastDomainAssociations"
)
AcceptTransitGatewayPeeringAttachment = Action("AcceptTransitGatewayPeeringAttachment")
AcceptTransitGatewayVpcAttachment = Action("AcceptTransitGatewayVpcAttachment")
AcceptVpcEndpointConnections = Action("AcceptVpcEndpointConnections")
AcceptVpcPeeringConnection = Action("AcceptVpcPeeringConnection")
AdvertiseByoipCidr = Action("AdvertiseByoipCidr")
AllocateAddress = Action("AllocateAddress")
AllocateHosts = Action("AllocateHosts")
AllocateIpamPoolCidr = Action("AllocateIpamPoolCidr")
ApplySecurityGroupsToClientVpnTargetNetwork = Action(
    "ApplySecurityGroupsToClientVpnTargetNetwork"
)
AssignIpv6Addresses = Action("AssignIpv6Addresses")
AssignPrivateIpAddresses = Action("AssignPrivateIpAddresses")
AssignPrivateNatGatewayAddress = Action("AssignPrivateNatGatewayAddress")
AssociateAddress = Action("AssociateAddress")
AssociateCapacityReservationBillingOwner = Action(
    "AssociateCapacityReservationBillingOwner"
)
AssociateClientVpnTargetNetwork = Action("AssociateClientVpnTargetNetwork")
AssociateDhcpOptions = Action("AssociateDhcpOptions")
AssociateEnclaveCertificateIamRole = Action("AssociateEnclaveCertificateIamRole")
AssociateIamInstanceProfile = Action("AssociateIamInstanceProfile")
AssociateInstanceEventWindow = Action("AssociateInstanceEventWindow")
AssociateIpamByoasn = Action("AssociateIpamByoasn")
AssociateIpamResourceDiscovery = Action("AssociateIpamResourceDiscovery")
AssociateNatGatewayAddress = Action("AssociateNatGatewayAddress")
AssociateRouteTable = Action("AssociateRouteTable")
AssociateSecurityGroupVpc = Action("AssociateSecurityGroupVpc")
AssociateSubnetCidrBlock = Action("AssociateSubnetCidrBlock")
AssociateTransitGatewayMulticastDomain = Action(
    "AssociateTransitGatewayMulticastDomain"
)
AssociateTransitGatewayPolicyTable = Action("AssociateTransitGatewayPolicyTable")
AssociateTransitGatewayRouteTable = Action("AssociateTransitGatewayRouteTable")
AssociateTrunkInterface = Action("AssociateTrunkInterface")
AssociateVerifiedAccessInstanceWebAcl = Action("AssociateVerifiedAccessInstanceWebAcl")
AssociateVpcCidrBlock = Action("AssociateVpcCidrBlock")
AttachClassicLinkVpc = Action("AttachClassicLinkVpc")
AttachInternetGateway = Action("AttachInternetGateway")
AttachNetworkInterface = Action("AttachNetworkInterface")
AttachVerifiedAccessTrustProvider = Action("AttachVerifiedAccessTrustProvider")
AttachVolume = Action("AttachVolume")
AttachVpnGateway = Action("AttachVpnGateway")
AuthorizeClientVpnIngress = Action("AuthorizeClientVpnIngress")
AuthorizeSecurityGroupEgress = Action("AuthorizeSecurityGroupEgress")
AuthorizeSecurityGroupIngress = Action("AuthorizeSecurityGroupIngress")
BundleInstance = Action("BundleInstance")
CancelBundleTask = Action("CancelBundleTask")
CancelCapacityReservation = Action("CancelCapacityReservation")
CancelCapacityReservationFleets = Action("CancelCapacityReservationFleets")
CancelConversionTask = Action("CancelConversionTask")
CancelDeclarativePoliciesReport = Action("CancelDeclarativePoliciesReport")
CancelExportTask = Action("CancelExportTask")
CancelImageLaunchPermission = Action("CancelImageLaunchPermission")
CancelImportTask = Action("CancelImportTask")
CancelReservedInstancesListing = Action("CancelReservedInstancesListing")
CancelSpotFleetRequests = Action("CancelSpotFleetRequests")
CancelSpotInstanceRequests = Action("CancelSpotInstanceRequests")
ConfirmProductInstance = Action("ConfirmProductInstance")
CopyFpgaImage = Action("CopyFpgaImage")
CopyImage = Action("CopyImage")
CopySnapshot = Action("CopySnapshot")
CreateCapacityReservation = Action("CreateCapacityReservation")
CreateCapacityReservationBySplitting = Action("CreateCapacityReservationBySplitting")
CreateCapacityReservationFleet = Action("CreateCapacityReservationFleet")
CreateCarrierGateway = Action("CreateCarrierGateway")
CreateClientVpnEndpoint = Action("CreateClientVpnEndpoint")
CreateClientVpnRoute = Action("CreateClientVpnRoute")
CreateCoipCidr = Action("CreateCoipCidr")
CreateCoipPool = Action("CreateCoipPool")
CreateCoipPoolPermission = Action("CreateCoipPoolPermission")
CreateCustomerGateway = Action("CreateCustomerGateway")
CreateDefaultSubnet = Action("CreateDefaultSubnet")
CreateDefaultVpc = Action("CreateDefaultVpc")
CreateDhcpOptions = Action("CreateDhcpOptions")
CreateEgressOnlyInternetGateway = Action("CreateEgressOnlyInternetGateway")
CreateFleet = Action("CreateFleet")
CreateFlowLogs = Action("CreateFlowLogs")
CreateFpgaImage = Action("CreateFpgaImage")
CreateImage = Action("CreateImage")
CreateInstanceConnectEndpoint = Action("CreateInstanceConnectEndpoint")
CreateInstanceEventWindow = Action("CreateInstanceEventWindow")
CreateInstanceExportTask = Action("CreateInstanceExportTask")
CreateInternetGateway = Action("CreateInternetGateway")
CreateIpam = Action("CreateIpam")
CreateIpamExternalResourceVerificationToken = Action(
    "CreateIpamExternalResourceVerificationToken"
)
CreateIpamPool = Action("CreateIpamPool")
CreateIpamResourceDiscovery = Action("CreateIpamResourceDiscovery")
CreateIpamScope = Action("CreateIpamScope")
CreateKeyPair = Action("CreateKeyPair")
CreateLaunchTemplate = Action("CreateLaunchTemplate")
CreateLaunchTemplateVersion = Action("CreateLaunchTemplateVersion")
CreateLocalGatewayRoute = Action("CreateLocalGatewayRoute")
CreateLocalGatewayRouteTable = Action("CreateLocalGatewayRouteTable")
CreateLocalGatewayRouteTablePermission = Action(
    "CreateLocalGatewayRouteTablePermission"
)
CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation = Action(
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation"
)
CreateLocalGatewayRouteTableVpcAssociation = Action(
    "CreateLocalGatewayRouteTableVpcAssociation"
)
CreateManagedPrefixList = Action("CreateManagedPrefixList")
CreateNatGateway = Action("CreateNatGateway")
CreateNetworkAcl = Action("CreateNetworkAcl")
CreateNetworkAclEntry = Action("CreateNetworkAclEntry")
CreateNetworkInsightsAccessScope = Action("CreateNetworkInsightsAccessScope")
CreateNetworkInsightsPath = Action("CreateNetworkInsightsPath")
CreateNetworkInterface = Action("CreateNetworkInterface")
CreateNetworkInterfacePermission = Action("CreateNetworkInterfacePermission")
CreatePlacementGroup = Action("CreatePlacementGroup")
CreatePublicIpv4Pool = Action("CreatePublicIpv4Pool")
CreateReplaceRootVolumeTask = Action("CreateReplaceRootVolumeTask")
CreateReservedInstancesListing = Action("CreateReservedInstancesListing")
CreateRestoreImageTask = Action("CreateRestoreImageTask")
CreateRoute = Action("CreateRoute")
CreateRouteTable = Action("CreateRouteTable")
CreateSecurityGroup = Action("CreateSecurityGroup")
CreateSnapshot = Action("CreateSnapshot")
CreateSnapshots = Action("CreateSnapshots")
CreateSpotDatafeedSubscription = Action("CreateSpotDatafeedSubscription")
CreateStoreImageTask = Action("CreateStoreImageTask")
CreateSubnet = Action("CreateSubnet")
CreateSubnetCidrReservation = Action("CreateSubnetCidrReservation")
CreateTags = Action("CreateTags")
CreateTrafficMirrorFilter = Action("CreateTrafficMirrorFilter")
CreateTrafficMirrorFilterRule = Action("CreateTrafficMirrorFilterRule")
CreateTrafficMirrorSession = Action("CreateTrafficMirrorSession")
CreateTrafficMirrorTarget = Action("CreateTrafficMirrorTarget")
CreateTransitGateway = Action("CreateTransitGateway")
CreateTransitGatewayConnect = Action("CreateTransitGatewayConnect")
CreateTransitGatewayConnectPeer = Action("CreateTransitGatewayConnectPeer")
CreateTransitGatewayMulticastDomain = Action("CreateTransitGatewayMulticastDomain")
CreateTransitGatewayPeeringAttachment = Action("CreateTransitGatewayPeeringAttachment")
CreateTransitGatewayPolicyTable = Action("CreateTransitGatewayPolicyTable")
CreateTransitGatewayPrefixListReference = Action(
    "CreateTransitGatewayPrefixListReference"
)
CreateTransitGatewayRoute = Action("CreateTransitGatewayRoute")
CreateTransitGatewayRouteTable = Action("CreateTransitGatewayRouteTable")
CreateTransitGatewayRouteTableAnnouncement = Action(
    "CreateTransitGatewayRouteTableAnnouncement"
)
CreateTransitGatewayVpcAttachment = Action("CreateTransitGatewayVpcAttachment")
CreateVerifiedAccessEndpoint = Action("CreateVerifiedAccessEndpoint")
CreateVerifiedAccessGroup = Action("CreateVerifiedAccessGroup")
CreateVerifiedAccessInstance = Action("CreateVerifiedAccessInstance")
CreateVerifiedAccessTrustProvider = Action("CreateVerifiedAccessTrustProvider")
CreateVolume = Action("CreateVolume")
CreateVpc = Action("CreateVpc")
CreateVpcBlockPublicAccessExclusion = Action("CreateVpcBlockPublicAccessExclusion")
CreateVpcEndpoint = Action("CreateVpcEndpoint")
CreateVpcEndpointConnectionNotification = Action(
    "CreateVpcEndpointConnectionNotification"
)
CreateVpcEndpointServiceConfiguration = Action("CreateVpcEndpointServiceConfiguration")
CreateVpcPeeringConnection = Action("CreateVpcPeeringConnection")
CreateVpnConnection = Action("CreateVpnConnection")
CreateVpnConnectionRoute = Action("CreateVpnConnectionRoute")
CreateVpnGateway = Action("CreateVpnGateway")
DeleteCarrierGateway = Action("DeleteCarrierGateway")
DeleteClientVpnEndpoint = Action("DeleteClientVpnEndpoint")
DeleteClientVpnRoute = Action("DeleteClientVpnRoute")
DeleteCoipCidr = Action("DeleteCoipCidr")
DeleteCoipPool = Action("DeleteCoipPool")
DeleteCoipPoolPermission = Action("DeleteCoipPoolPermission")
DeleteCustomerGateway = Action("DeleteCustomerGateway")
DeleteDhcpOptions = Action("DeleteDhcpOptions")
DeleteEgressOnlyInternetGateway = Action("DeleteEgressOnlyInternetGateway")
DeleteFleets = Action("DeleteFleets")
DeleteFlowLogs = Action("DeleteFlowLogs")
DeleteFpgaImage = Action("DeleteFpgaImage")
DeleteInstanceConnectEndpoint = Action("DeleteInstanceConnectEndpoint")
DeleteInstanceEventWindow = Action("DeleteInstanceEventWindow")
DeleteInternetGateway = Action("DeleteInternetGateway")
DeleteIpam = Action("DeleteIpam")
DeleteIpamExternalResourceVerificationToken = Action(
    "DeleteIpamExternalResourceVerificationToken"
)
DeleteIpamPool = Action("DeleteIpamPool")
DeleteIpamResourceDiscovery = Action("DeleteIpamResourceDiscovery")
DeleteIpamScope = Action("DeleteIpamScope")
DeleteKeyPair = Action("DeleteKeyPair")
DeleteLaunchTemplate = Action("DeleteLaunchTemplate")
DeleteLaunchTemplateVersions = Action("DeleteLaunchTemplateVersions")
DeleteLocalGatewayRoute = Action("DeleteLocalGatewayRoute")
DeleteLocalGatewayRouteTable = Action("DeleteLocalGatewayRouteTable")
DeleteLocalGatewayRouteTablePermission = Action(
    "DeleteLocalGatewayRouteTablePermission"
)
DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation = Action(
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation"
)
DeleteLocalGatewayRouteTableVpcAssociation = Action(
    "DeleteLocalGatewayRouteTableVpcAssociation"
)
DeleteManagedPrefixList = Action("DeleteManagedPrefixList")
DeleteNatGateway = Action("DeleteNatGateway")
DeleteNetworkAcl = Action("DeleteNetworkAcl")
DeleteNetworkAclEntry = Action("DeleteNetworkAclEntry")
DeleteNetworkInsightsAccessScope = Action("DeleteNetworkInsightsAccessScope")
DeleteNetworkInsightsAccessScopeAnalysis = Action(
    "DeleteNetworkInsightsAccessScopeAnalysis"
)
DeleteNetworkInsightsAnalysis = Action("DeleteNetworkInsightsAnalysis")
DeleteNetworkInsightsPath = Action("DeleteNetworkInsightsPath")
DeleteNetworkInterface = Action("DeleteNetworkInterface")
DeleteNetworkInterfacePermission = Action("DeleteNetworkInterfacePermission")
DeletePlacementGroup = Action("DeletePlacementGroup")
DeletePublicIpv4Pool = Action("DeletePublicIpv4Pool")
DeleteQueuedReservedInstances = Action("DeleteQueuedReservedInstances")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRoute = Action("DeleteRoute")
DeleteRouteTable = Action("DeleteRouteTable")
DeleteSecurityGroup = Action("DeleteSecurityGroup")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteSpotDatafeedSubscription = Action("DeleteSpotDatafeedSubscription")
DeleteSubnet = Action("DeleteSubnet")
DeleteSubnetCidrReservation = Action("DeleteSubnetCidrReservation")
DeleteTags = Action("DeleteTags")
DeleteTrafficMirrorFilter = Action("DeleteTrafficMirrorFilter")
DeleteTrafficMirrorFilterRule = Action("DeleteTrafficMirrorFilterRule")
DeleteTrafficMirrorSession = Action("DeleteTrafficMirrorSession")
DeleteTrafficMirrorTarget = Action("DeleteTrafficMirrorTarget")
DeleteTransitGateway = Action("DeleteTransitGateway")
DeleteTransitGatewayConnect = Action("DeleteTransitGatewayConnect")
DeleteTransitGatewayConnectPeer = Action("DeleteTransitGatewayConnectPeer")
DeleteTransitGatewayMulticastDomain = Action("DeleteTransitGatewayMulticastDomain")
DeleteTransitGatewayPeeringAttachment = Action("DeleteTransitGatewayPeeringAttachment")
DeleteTransitGatewayPolicyTable = Action("DeleteTransitGatewayPolicyTable")
DeleteTransitGatewayPrefixListReference = Action(
    "DeleteTransitGatewayPrefixListReference"
)
DeleteTransitGatewayRoute = Action("DeleteTransitGatewayRoute")
DeleteTransitGatewayRouteTable = Action("DeleteTransitGatewayRouteTable")
DeleteTransitGatewayRouteTableAnnouncement = Action(
    "DeleteTransitGatewayRouteTableAnnouncement"
)
DeleteTransitGatewayVpcAttachment = Action("DeleteTransitGatewayVpcAttachment")
DeleteVerifiedAccessEndpoint = Action("DeleteVerifiedAccessEndpoint")
DeleteVerifiedAccessGroup = Action("DeleteVerifiedAccessGroup")
DeleteVerifiedAccessInstance = Action("DeleteVerifiedAccessInstance")
DeleteVerifiedAccessTrustProvider = Action("DeleteVerifiedAccessTrustProvider")
DeleteVolume = Action("DeleteVolume")
DeleteVpc = Action("DeleteVpc")
DeleteVpcBlockPublicAccessExclusion = Action("DeleteVpcBlockPublicAccessExclusion")
DeleteVpcEndpointConnectionNotifications = Action(
    "DeleteVpcEndpointConnectionNotifications"
)
DeleteVpcEndpointServiceConfigurations = Action(
    "DeleteVpcEndpointServiceConfigurations"
)
DeleteVpcEndpoints = Action("DeleteVpcEndpoints")
DeleteVpcPeeringConnection = Action("DeleteVpcPeeringConnection")
DeleteVpnConnection = Action("DeleteVpnConnection")
DeleteVpnConnectionRoute = Action("DeleteVpnConnectionRoute")
DeleteVpnGateway = Action("DeleteVpnGateway")
DeprovisionByoipCidr = Action("DeprovisionByoipCidr")
DeprovisionIpamByoasn = Action("DeprovisionIpamByoasn")
DeprovisionIpamPoolCidr = Action("DeprovisionIpamPoolCidr")
DeprovisionPublicIpv4PoolCidr = Action("DeprovisionPublicIpv4PoolCidr")
DeregisterImage = Action("DeregisterImage")
DeregisterInstanceEventNotificationAttributes = Action(
    "DeregisterInstanceEventNotificationAttributes"
)
DeregisterTransitGatewayMulticastGroupMembers = Action(
    "DeregisterTransitGatewayMulticastGroupMembers"
)
DeregisterTransitGatewayMulticastGroupSources = Action(
    "DeregisterTransitGatewayMulticastGroupSources"
)
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeAddressTransfers = Action("DescribeAddressTransfers")
DescribeAddresses = Action("DescribeAddresses")
DescribeAddressesAttribute = Action("DescribeAddressesAttribute")
DescribeAggregateIdFormat = Action("DescribeAggregateIdFormat")
DescribeAvailabilityZones = Action("DescribeAvailabilityZones")
DescribeAwsNetworkPerformanceMetricSubscriptions = Action(
    "DescribeAwsNetworkPerformanceMetricSubscriptions"
)
DescribeBundleTasks = Action("DescribeBundleTasks")
DescribeByoipCidrs = Action("DescribeByoipCidrs")
DescribeCapacityBlockExtensionHistory = Action("DescribeCapacityBlockExtensionHistory")
DescribeCapacityBlockExtensionOfferings = Action(
    "DescribeCapacityBlockExtensionOfferings"
)
DescribeCapacityBlockOfferings = Action("DescribeCapacityBlockOfferings")
DescribeCapacityReservationBillingRequests = Action(
    "DescribeCapacityReservationBillingRequests"
)
DescribeCapacityReservationFleets = Action("DescribeCapacityReservationFleets")
DescribeCapacityReservations = Action("DescribeCapacityReservations")
DescribeCarrierGateways = Action("DescribeCarrierGateways")
DescribeClassicLinkInstances = Action("DescribeClassicLinkInstances")
DescribeClientVpnAuthorizationRules = Action("DescribeClientVpnAuthorizationRules")
DescribeClientVpnConnections = Action("DescribeClientVpnConnections")
DescribeClientVpnEndpoints = Action("DescribeClientVpnEndpoints")
DescribeClientVpnRoutes = Action("DescribeClientVpnRoutes")
DescribeClientVpnTargetNetworks = Action("DescribeClientVpnTargetNetworks")
DescribeCoipPools = Action("DescribeCoipPools")
DescribeConversionTasks = Action("DescribeConversionTasks")
DescribeCustomerGateways = Action("DescribeCustomerGateways")
DescribeDeclarativePoliciesReports = Action("DescribeDeclarativePoliciesReports")
DescribeDhcpOptions = Action("DescribeDhcpOptions")
DescribeEgressOnlyInternetGateways = Action("DescribeEgressOnlyInternetGateways")
DescribeElasticGpus = Action("DescribeElasticGpus")
DescribeExportImageTasks = Action("DescribeExportImageTasks")
DescribeExportTasks = Action("DescribeExportTasks")
DescribeFastLaunchImages = Action("DescribeFastLaunchImages")
DescribeFastSnapshotRestores = Action("DescribeFastSnapshotRestores")
DescribeFleetHistory = Action("DescribeFleetHistory")
DescribeFleetInstances = Action("DescribeFleetInstances")
DescribeFleets = Action("DescribeFleets")
DescribeFlowLogs = Action("DescribeFlowLogs")
DescribeFpgaImageAttribute = Action("DescribeFpgaImageAttribute")
DescribeFpgaImages = Action("DescribeFpgaImages")
DescribeHostReservationOfferings = Action("DescribeHostReservationOfferings")
DescribeHostReservations = Action("DescribeHostReservations")
DescribeHosts = Action("DescribeHosts")
DescribeIamInstanceProfileAssociations = Action(
    "DescribeIamInstanceProfileAssociations"
)
DescribeIdFormat = Action("DescribeIdFormat")
DescribeIdentityIdFormat = Action("DescribeIdentityIdFormat")
DescribeImageAttribute = Action("DescribeImageAttribute")
DescribeImages = Action("DescribeImages")
DescribeImportImageTasks = Action("DescribeImportImageTasks")
DescribeImportSnapshotTasks = Action("DescribeImportSnapshotTasks")
DescribeInstanceAttribute = Action("DescribeInstanceAttribute")
DescribeInstanceConnectEndpoints = Action("DescribeInstanceConnectEndpoints")
DescribeInstanceCreditSpecifications = Action("DescribeInstanceCreditSpecifications")
DescribeInstanceEventNotificationAttributes = Action(
    "DescribeInstanceEventNotificationAttributes"
)
DescribeInstanceEventWindows = Action("DescribeInstanceEventWindows")
DescribeInstanceImageMetadata = Action("DescribeInstanceImageMetadata")
DescribeInstanceStatus = Action("DescribeInstanceStatus")
DescribeInstanceTopology = Action("DescribeInstanceTopology")
DescribeInstanceTypeOfferings = Action("DescribeInstanceTypeOfferings")
DescribeInstanceTypes = Action("DescribeInstanceTypes")
DescribeInstances = Action("DescribeInstances")
DescribeInternetGateways = Action("DescribeInternetGateways")
DescribeIpamByoasn = Action("DescribeIpamByoasn")
DescribeIpamExternalResourceVerificationTokens = Action(
    "DescribeIpamExternalResourceVerificationTokens"
)
DescribeIpamPools = Action("DescribeIpamPools")
DescribeIpamResourceDiscoveries = Action("DescribeIpamResourceDiscoveries")
DescribeIpamResourceDiscoveryAssociations = Action(
    "DescribeIpamResourceDiscoveryAssociations"
)
DescribeIpamScopes = Action("DescribeIpamScopes")
DescribeIpams = Action("DescribeIpams")
DescribeIpv6Pools = Action("DescribeIpv6Pools")
DescribeKeyPairs = Action("DescribeKeyPairs")
DescribeLaunchTemplateVersions = Action("DescribeLaunchTemplateVersions")
DescribeLaunchTemplates = Action("DescribeLaunchTemplates")
DescribeLocalGatewayRouteTablePermissions = Action(
    "DescribeLocalGatewayRouteTablePermissions"
)
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations = Action(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations"
)
DescribeLocalGatewayRouteTableVpcAssociations = Action(
    "DescribeLocalGatewayRouteTableVpcAssociations"
)
DescribeLocalGatewayRouteTables = Action("DescribeLocalGatewayRouteTables")
DescribeLocalGatewayVirtualInterfaceGroups = Action(
    "DescribeLocalGatewayVirtualInterfaceGroups"
)
DescribeLocalGatewayVirtualInterfaces = Action("DescribeLocalGatewayVirtualInterfaces")
DescribeLocalGateways = Action("DescribeLocalGateways")
DescribeLockedSnapshots = Action("DescribeLockedSnapshots")
DescribeMacHosts = Action("DescribeMacHosts")
DescribeManagedPrefixLists = Action("DescribeManagedPrefixLists")
DescribeMovingAddresses = Action("DescribeMovingAddresses")
DescribeNatGateways = Action("DescribeNatGateways")
DescribeNetworkAcls = Action("DescribeNetworkAcls")
DescribeNetworkInsightsAccessScopeAnalyses = Action(
    "DescribeNetworkInsightsAccessScopeAnalyses"
)
DescribeNetworkInsightsAccessScopes = Action("DescribeNetworkInsightsAccessScopes")
DescribeNetworkInsightsAnalyses = Action("DescribeNetworkInsightsAnalyses")
DescribeNetworkInsightsPaths = Action("DescribeNetworkInsightsPaths")
DescribeNetworkInterfaceAttribute = Action("DescribeNetworkInterfaceAttribute")
DescribeNetworkInterfacePermissions = Action("DescribeNetworkInterfacePermissions")
DescribeNetworkInterfaces = Action("DescribeNetworkInterfaces")
DescribePlacementGroups = Action("DescribePlacementGroups")
DescribePrefixLists = Action("DescribePrefixLists")
DescribePrincipalIdFormat = Action("DescribePrincipalIdFormat")
DescribePublicIpv4Pools = Action("DescribePublicIpv4Pools")
DescribeRegions = Action("DescribeRegions")
DescribeReplaceRootVolumeTasks = Action("DescribeReplaceRootVolumeTasks")
DescribeReservedInstances = Action("DescribeReservedInstances")
DescribeReservedInstancesListings = Action("DescribeReservedInstancesListings")
DescribeReservedInstancesModifications = Action(
    "DescribeReservedInstancesModifications"
)
DescribeReservedInstancesOfferings = Action("DescribeReservedInstancesOfferings")
DescribeRouteTables = Action("DescribeRouteTables")
DescribeScheduledInstanceAvailability = Action("DescribeScheduledInstanceAvailability")
DescribeScheduledInstances = Action("DescribeScheduledInstances")
DescribeSecurityGroupReferences = Action("DescribeSecurityGroupReferences")
DescribeSecurityGroupRules = Action("DescribeSecurityGroupRules")
DescribeSecurityGroupVpcAssociations = Action("DescribeSecurityGroupVpcAssociations")
DescribeSecurityGroups = Action("DescribeSecurityGroups")
DescribeSnapshotAttribute = Action("DescribeSnapshotAttribute")
DescribeSnapshotTierStatus = Action("DescribeSnapshotTierStatus")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeSpotDatafeedSubscription = Action("DescribeSpotDatafeedSubscription")
DescribeSpotFleetInstances = Action("DescribeSpotFleetInstances")
DescribeSpotFleetRequestHistory = Action("DescribeSpotFleetRequestHistory")
DescribeSpotFleetRequests = Action("DescribeSpotFleetRequests")
DescribeSpotInstanceRequests = Action("DescribeSpotInstanceRequests")
DescribeSpotPriceHistory = Action("DescribeSpotPriceHistory")
DescribeStaleSecurityGroups = Action("DescribeStaleSecurityGroups")
DescribeStoreImageTasks = Action("DescribeStoreImageTasks")
DescribeSubnets = Action("DescribeSubnets")
DescribeTags = Action("DescribeTags")
DescribeTrafficMirrorFilterRules = Action("DescribeTrafficMirrorFilterRules")
DescribeTrafficMirrorFilters = Action("DescribeTrafficMirrorFilters")
DescribeTrafficMirrorSessions = Action("DescribeTrafficMirrorSessions")
DescribeTrafficMirrorTargets = Action("DescribeTrafficMirrorTargets")
DescribeTransitGatewayAttachments = Action("DescribeTransitGatewayAttachments")
DescribeTransitGatewayConnectPeers = Action("DescribeTransitGatewayConnectPeers")
DescribeTransitGatewayConnects = Action("DescribeTransitGatewayConnects")
DescribeTransitGatewayMulticastDomains = Action(
    "DescribeTransitGatewayMulticastDomains"
)
DescribeTransitGatewayPeeringAttachments = Action(
    "DescribeTransitGatewayPeeringAttachments"
)
DescribeTransitGatewayPolicyTables = Action("DescribeTransitGatewayPolicyTables")
DescribeTransitGatewayRouteTableAnnouncements = Action(
    "DescribeTransitGatewayRouteTableAnnouncements"
)
DescribeTransitGatewayRouteTables = Action("DescribeTransitGatewayRouteTables")
DescribeTransitGatewayVpcAttachments = Action("DescribeTransitGatewayVpcAttachments")
DescribeTransitGateways = Action("DescribeTransitGateways")
DescribeTrunkInterfaceAssociations = Action("DescribeTrunkInterfaceAssociations")
DescribeVerifiedAccessEndpoints = Action("DescribeVerifiedAccessEndpoints")
DescribeVerifiedAccessGroups = Action("DescribeVerifiedAccessGroups")
DescribeVerifiedAccessInstanceLoggingConfigurations = Action(
    "DescribeVerifiedAccessInstanceLoggingConfigurations"
)
DescribeVerifiedAccessInstanceWebAclAssociations = Action(
    "DescribeVerifiedAccessInstanceWebAclAssociations"
)
DescribeVerifiedAccessInstances = Action("DescribeVerifiedAccessInstances")
DescribeVerifiedAccessTrustProviders = Action("DescribeVerifiedAccessTrustProviders")
DescribeVolumeAttribute = Action("DescribeVolumeAttribute")
DescribeVolumeStatus = Action("DescribeVolumeStatus")
DescribeVolumes = Action("DescribeVolumes")
DescribeVolumesModifications = Action("DescribeVolumesModifications")
DescribeVpcAttribute = Action("DescribeVpcAttribute")
DescribeVpcBlockPublicAccessExclusions = Action(
    "DescribeVpcBlockPublicAccessExclusions"
)
DescribeVpcBlockPublicAccessOptions = Action("DescribeVpcBlockPublicAccessOptions")
DescribeVpcClassicLink = Action("DescribeVpcClassicLink")
DescribeVpcClassicLinkDnsSupport = Action("DescribeVpcClassicLinkDnsSupport")
DescribeVpcEndpointAssociations = Action("DescribeVpcEndpointAssociations")
DescribeVpcEndpointConnectionNotifications = Action(
    "DescribeVpcEndpointConnectionNotifications"
)
DescribeVpcEndpointConnections = Action("DescribeVpcEndpointConnections")
DescribeVpcEndpointServiceConfigurations = Action(
    "DescribeVpcEndpointServiceConfigurations"
)
DescribeVpcEndpointServicePermissions = Action("DescribeVpcEndpointServicePermissions")
DescribeVpcEndpointServices = Action("DescribeVpcEndpointServices")
DescribeVpcEndpoints = Action("DescribeVpcEndpoints")
DescribeVpcPeeringConnections = Action("DescribeVpcPeeringConnections")
DescribeVpcs = Action("DescribeVpcs")
DescribeVpnConnections = Action("DescribeVpnConnections")
DescribeVpnGateways = Action("DescribeVpnGateways")
DetachClassicLinkVpc = Action("DetachClassicLinkVpc")
DetachInternetGateway = Action("DetachInternetGateway")
DetachNetworkInterface = Action("DetachNetworkInterface")
DetachVerifiedAccessTrustProvider = Action("DetachVerifiedAccessTrustProvider")
DetachVolume = Action("DetachVolume")
DetachVpnGateway = Action("DetachVpnGateway")
DisableAddressTransfer = Action("DisableAddressTransfer")
DisableAllowedImagesSettings = Action("DisableAllowedImagesSettings")
DisableAwsNetworkPerformanceMetricSubscription = Action(
    "DisableAwsNetworkPerformanceMetricSubscription"
)
DisableEbsEncryptionByDefault = Action("DisableEbsEncryptionByDefault")
DisableFastLaunch = Action("DisableFastLaunch")
DisableFastSnapshotRestores = Action("DisableFastSnapshotRestores")
DisableImage = Action("DisableImage")
DisableImageBlockPublicAccess = Action("DisableImageBlockPublicAccess")
DisableImageDeprecation = Action("DisableImageDeprecation")
DisableImageDeregistrationProtection = Action("DisableImageDeregistrationProtection")
DisableIpamOrganizationAdminAccount = Action("DisableIpamOrganizationAdminAccount")
DisableSerialConsoleAccess = Action("DisableSerialConsoleAccess")
DisableSnapshotBlockPublicAccess = Action("DisableSnapshotBlockPublicAccess")
DisableTransitGatewayRouteTablePropagation = Action(
    "DisableTransitGatewayRouteTablePropagation"
)
DisableVgwRoutePropagation = Action("DisableVgwRoutePropagation")
DisableVpcClassicLink = Action("DisableVpcClassicLink")
DisableVpcClassicLinkDnsSupport = Action("DisableVpcClassicLinkDnsSupport")
DisassociateAddress = Action("DisassociateAddress")
DisassociateCapacityReservationBillingOwner = Action(
    "DisassociateCapacityReservationBillingOwner"
)
DisassociateClientVpnTargetNetwork = Action("DisassociateClientVpnTargetNetwork")
DisassociateEnclaveCertificateIamRole = Action("DisassociateEnclaveCertificateIamRole")
DisassociateIamInstanceProfile = Action("DisassociateIamInstanceProfile")
DisassociateInstanceEventWindow = Action("DisassociateInstanceEventWindow")
DisassociateIpamByoasn = Action("DisassociateIpamByoasn")
DisassociateIpamResourceDiscovery = Action("DisassociateIpamResourceDiscovery")
DisassociateNatGatewayAddress = Action("DisassociateNatGatewayAddress")
DisassociateRouteTable = Action("DisassociateRouteTable")
DisassociateSecurityGroupVpc = Action("DisassociateSecurityGroupVpc")
DisassociateSubnetCidrBlock = Action("DisassociateSubnetCidrBlock")
DisassociateTransitGatewayMulticastDomain = Action(
    "DisassociateTransitGatewayMulticastDomain"
)
DisassociateTransitGatewayPolicyTable = Action("DisassociateTransitGatewayPolicyTable")
DisassociateTransitGatewayRouteTable = Action("DisassociateTransitGatewayRouteTable")
DisassociateTrunkInterface = Action("DisassociateTrunkInterface")
DisassociateVerifiedAccessInstanceWebAcl = Action(
    "DisassociateVerifiedAccessInstanceWebAcl"
)
DisassociateVpcCidrBlock = Action("DisassociateVpcCidrBlock")
EnableAddressTransfer = Action("EnableAddressTransfer")
EnableAllowedImagesSettings = Action("EnableAllowedImagesSettings")
EnableAwsNetworkPerformanceMetricSubscription = Action(
    "EnableAwsNetworkPerformanceMetricSubscription"
)
EnableEbsEncryptionByDefault = Action("EnableEbsEncryptionByDefault")
EnableFastLaunch = Action("EnableFastLaunch")
EnableFastSnapshotRestores = Action("EnableFastSnapshotRestores")
EnableImage = Action("EnableImage")
EnableImageBlockPublicAccess = Action("EnableImageBlockPublicAccess")
EnableImageDeprecation = Action("EnableImageDeprecation")
EnableImageDeregistrationProtection = Action("EnableImageDeregistrationProtection")
EnableIpamOrganizationAdminAccount = Action("EnableIpamOrganizationAdminAccount")
EnableReachabilityAnalyzerOrganizationSharing = Action(
    "EnableReachabilityAnalyzerOrganizationSharing"
)
EnableSerialConsoleAccess = Action("EnableSerialConsoleAccess")
EnableSnapshotBlockPublicAccess = Action("EnableSnapshotBlockPublicAccess")
EnableTransitGatewayRouteTablePropagation = Action(
    "EnableTransitGatewayRouteTablePropagation"
)
EnableVgwRoutePropagation = Action("EnableVgwRoutePropagation")
EnableVolumeIO = Action("EnableVolumeIO")
EnableVpcClassicLink = Action("EnableVpcClassicLink")
EnableVpcClassicLinkDnsSupport = Action("EnableVpcClassicLinkDnsSupport")
ExportClientVpnClientCertificateRevocationList = Action(
    "ExportClientVpnClientCertificateRevocationList"
)
ExportClientVpnClientConfiguration = Action("ExportClientVpnClientConfiguration")
ExportImage = Action("ExportImage")
ExportTransitGatewayRoutes = Action("ExportTransitGatewayRoutes")
ExportVerifiedAccessInstanceClientConfiguration = Action(
    "ExportVerifiedAccessInstanceClientConfiguration"
)
GetAllowedImagesSettings = Action("GetAllowedImagesSettings")
GetAssociatedEnclaveCertificateIamRoles = Action(
    "GetAssociatedEnclaveCertificateIamRoles"
)
GetAssociatedIpv6PoolCidrs = Action("GetAssociatedIpv6PoolCidrs")
GetAwsNetworkPerformanceData = Action("GetAwsNetworkPerformanceData")
GetCapacityReservationUsage = Action("GetCapacityReservationUsage")
GetCoipPoolUsage = Action("GetCoipPoolUsage")
GetConsoleOutput = Action("GetConsoleOutput")
GetConsoleScreenshot = Action("GetConsoleScreenshot")
GetDeclarativePoliciesReportSummary = Action("GetDeclarativePoliciesReportSummary")
GetDefaultCreditSpecification = Action("GetDefaultCreditSpecification")
GetEbsDefaultKmsKeyId = Action("GetEbsDefaultKmsKeyId")
GetEbsEncryptionByDefault = Action("GetEbsEncryptionByDefault")
GetFlowLogsIntegrationTemplate = Action("GetFlowLogsIntegrationTemplate")
GetGroupsForCapacityReservation = Action("GetGroupsForCapacityReservation")
GetHostReservationPurchasePreview = Action("GetHostReservationPurchasePreview")
GetImageBlockPublicAccessState = Action("GetImageBlockPublicAccessState")
GetInstanceMetadataDefaults = Action("GetInstanceMetadataDefaults")
GetInstanceTpmEkPub = Action("GetInstanceTpmEkPub")
GetInstanceTypesFromInstanceRequirements = Action(
    "GetInstanceTypesFromInstanceRequirements"
)
GetInstanceUefiData = Action("GetInstanceUefiData")
GetIpamAddressHistory = Action("GetIpamAddressHistory")
GetIpamDiscoveredAccounts = Action("GetIpamDiscoveredAccounts")
GetIpamDiscoveredPublicAddresses = Action("GetIpamDiscoveredPublicAddresses")
GetIpamDiscoveredResourceCidrs = Action("GetIpamDiscoveredResourceCidrs")
GetIpamPoolAllocations = Action("GetIpamPoolAllocations")
GetIpamPoolCidrs = Action("GetIpamPoolCidrs")
GetIpamResourceCidrs = Action("GetIpamResourceCidrs")
GetLaunchTemplateData = Action("GetLaunchTemplateData")
GetManagedPrefixListAssociations = Action("GetManagedPrefixListAssociations")
GetManagedPrefixListEntries = Action("GetManagedPrefixListEntries")
GetNetworkInsightsAccessScopeAnalysisFindings = Action(
    "GetNetworkInsightsAccessScopeAnalysisFindings"
)
GetNetworkInsightsAccessScopeContent = Action("GetNetworkInsightsAccessScopeContent")
GetPasswordData = Action("GetPasswordData")
GetReservedInstancesExchangeQuote = Action("GetReservedInstancesExchangeQuote")
GetResourcePolicy = Action("GetResourcePolicy")
GetSecurityGroupsForVpc = Action("GetSecurityGroupsForVpc")
GetSerialConsoleAccessStatus = Action("GetSerialConsoleAccessStatus")
GetSnapshotBlockPublicAccessState = Action("GetSnapshotBlockPublicAccessState")
GetSpotPlacementScores = Action("GetSpotPlacementScores")
GetSubnetCidrReservations = Action("GetSubnetCidrReservations")
GetTransitGatewayAttachmentPropagations = Action(
    "GetTransitGatewayAttachmentPropagations"
)
GetTransitGatewayMulticastDomainAssociations = Action(
    "GetTransitGatewayMulticastDomainAssociations"
)
GetTransitGatewayPolicyTableAssociations = Action(
    "GetTransitGatewayPolicyTableAssociations"
)
GetTransitGatewayPolicyTableEntries = Action("GetTransitGatewayPolicyTableEntries")
GetTransitGatewayPrefixListReferences = Action("GetTransitGatewayPrefixListReferences")
GetTransitGatewayRouteTableAssociations = Action(
    "GetTransitGatewayRouteTableAssociations"
)
GetTransitGatewayRouteTablePropagations = Action(
    "GetTransitGatewayRouteTablePropagations"
)
GetVerifiedAccessEndpointPolicy = Action("GetVerifiedAccessEndpointPolicy")
GetVerifiedAccessEndpointTargets = Action("GetVerifiedAccessEndpointTargets")
GetVerifiedAccessGroupPolicy = Action("GetVerifiedAccessGroupPolicy")
GetVerifiedAccessInstanceWebAcl = Action("GetVerifiedAccessInstanceWebAcl")
GetVpnConnectionDeviceSampleConfiguration = Action(
    "GetVpnConnectionDeviceSampleConfiguration"
)
GetVpnConnectionDeviceTypes = Action("GetVpnConnectionDeviceTypes")
GetVpnTunnelReplacementStatus = Action("GetVpnTunnelReplacementStatus")
ImportByoipCidrToIpam = Action("ImportByoipCidrToIpam")
ImportClientVpnClientCertificateRevocationList = Action(
    "ImportClientVpnClientCertificateRevocationList"
)
ImportImage = Action("ImportImage")
ImportInstance = Action("ImportInstance")
ImportKeyPair = Action("ImportKeyPair")
ImportSnapshot = Action("ImportSnapshot")
ImportVolume = Action("ImportVolume")
InjectApiError = Action("InjectApiError")
ListImagesInRecycleBin = Action("ListImagesInRecycleBin")
ListSnapshotsInRecycleBin = Action("ListSnapshotsInRecycleBin")
LockSnapshot = Action("LockSnapshot")
ModifyAddressAttribute = Action("ModifyAddressAttribute")
ModifyAvailabilityZoneGroup = Action("ModifyAvailabilityZoneGroup")
ModifyCapacityReservation = Action("ModifyCapacityReservation")
ModifyCapacityReservationFleet = Action("ModifyCapacityReservationFleet")
ModifyClientVpnEndpoint = Action("ModifyClientVpnEndpoint")
ModifyDefaultCreditSpecification = Action("ModifyDefaultCreditSpecification")
ModifyEbsDefaultKmsKeyId = Action("ModifyEbsDefaultKmsKeyId")
ModifyFleet = Action("ModifyFleet")
ModifyFpgaImageAttribute = Action("ModifyFpgaImageAttribute")
ModifyHosts = Action("ModifyHosts")
ModifyIdFormat = Action("ModifyIdFormat")
ModifyIdentityIdFormat = Action("ModifyIdentityIdFormat")
ModifyImageAttribute = Action("ModifyImageAttribute")
ModifyInstanceAttribute = Action("ModifyInstanceAttribute")
ModifyInstanceCapacityReservationAttributes = Action(
    "ModifyInstanceCapacityReservationAttributes"
)
ModifyInstanceCpuOptions = Action("ModifyInstanceCpuOptions")
ModifyInstanceCreditSpecification = Action("ModifyInstanceCreditSpecification")
ModifyInstanceEventStartTime = Action("ModifyInstanceEventStartTime")
ModifyInstanceEventWindow = Action("ModifyInstanceEventWindow")
ModifyInstanceMaintenanceOptions = Action("ModifyInstanceMaintenanceOptions")
ModifyInstanceMetadataDefaults = Action("ModifyInstanceMetadataDefaults")
ModifyInstanceMetadataOptions = Action("ModifyInstanceMetadataOptions")
ModifyInstancePlacement = Action("ModifyInstancePlacement")
ModifyIpam = Action("ModifyIpam")
ModifyIpamPool = Action("ModifyIpamPool")
ModifyIpamResourceCidr = Action("ModifyIpamResourceCidr")
ModifyIpamResourceDiscovery = Action("ModifyIpamResourceDiscovery")
ModifyIpamScope = Action("ModifyIpamScope")
ModifyLaunchTemplate = Action("ModifyLaunchTemplate")
ModifyLocalGatewayRoute = Action("ModifyLocalGatewayRoute")
ModifyManagedPrefixList = Action("ModifyManagedPrefixList")
ModifyNetworkInterfaceAttribute = Action("ModifyNetworkInterfaceAttribute")
ModifyPrivateDnsNameOptions = Action("ModifyPrivateDnsNameOptions")
ModifyReservedInstances = Action("ModifyReservedInstances")
ModifySecurityGroupRules = Action("ModifySecurityGroupRules")
ModifySnapshotAttribute = Action("ModifySnapshotAttribute")
ModifySnapshotTier = Action("ModifySnapshotTier")
ModifySpotFleetRequest = Action("ModifySpotFleetRequest")
ModifySubnetAttribute = Action("ModifySubnetAttribute")
ModifyTrafficMirrorFilterNetworkServices = Action(
    "ModifyTrafficMirrorFilterNetworkServices"
)
ModifyTrafficMirrorFilterRule = Action("ModifyTrafficMirrorFilterRule")
ModifyTrafficMirrorSession = Action("ModifyTrafficMirrorSession")
ModifyTransitGateway = Action("ModifyTransitGateway")
ModifyTransitGatewayPrefixListReference = Action(
    "ModifyTransitGatewayPrefixListReference"
)
ModifyTransitGatewayVpcAttachment = Action("ModifyTransitGatewayVpcAttachment")
ModifyVerifiedAccessEndpoint = Action("ModifyVerifiedAccessEndpoint")
ModifyVerifiedAccessEndpointPolicy = Action("ModifyVerifiedAccessEndpointPolicy")
ModifyVerifiedAccessGroup = Action("ModifyVerifiedAccessGroup")
ModifyVerifiedAccessGroupPolicy = Action("ModifyVerifiedAccessGroupPolicy")
ModifyVerifiedAccessInstance = Action("ModifyVerifiedAccessInstance")
ModifyVerifiedAccessInstanceLoggingConfiguration = Action(
    "ModifyVerifiedAccessInstanceLoggingConfiguration"
)
ModifyVerifiedAccessTrustProvider = Action("ModifyVerifiedAccessTrustProvider")
ModifyVolume = Action("ModifyVolume")
ModifyVolumeAttribute = Action("ModifyVolumeAttribute")
ModifyVpcAttribute = Action("ModifyVpcAttribute")
ModifyVpcBlockPublicAccessExclusion = Action("ModifyVpcBlockPublicAccessExclusion")
ModifyVpcBlockPublicAccessOptions = Action("ModifyVpcBlockPublicAccessOptions")
ModifyVpcEndpoint = Action("ModifyVpcEndpoint")
ModifyVpcEndpointConnectionNotification = Action(
    "ModifyVpcEndpointConnectionNotification"
)
ModifyVpcEndpointServiceConfiguration = Action("ModifyVpcEndpointServiceConfiguration")
ModifyVpcEndpointServicePayerResponsibility = Action(
    "ModifyVpcEndpointServicePayerResponsibility"
)
ModifyVpcEndpointServicePermissions = Action("ModifyVpcEndpointServicePermissions")
ModifyVpcPeeringConnectionOptions = Action("ModifyVpcPeeringConnectionOptions")
ModifyVpcTenancy = Action("ModifyVpcTenancy")
ModifyVpnConnection = Action("ModifyVpnConnection")
ModifyVpnConnectionOptions = Action("ModifyVpnConnectionOptions")
ModifyVpnTunnelCertificate = Action("ModifyVpnTunnelCertificate")
ModifyVpnTunnelOptions = Action("ModifyVpnTunnelOptions")
MonitorInstances = Action("MonitorInstances")
MoveAddressToVpc = Action("MoveAddressToVpc")
MoveByoipCidrToIpam = Action("MoveByoipCidrToIpam")
MoveCapacityReservationInstances = Action("MoveCapacityReservationInstances")
PauseVolumeIO = Action("PauseVolumeIO")
ProvisionByoipCidr = Action("ProvisionByoipCidr")
ProvisionIpamByoasn = Action("ProvisionIpamByoasn")
ProvisionIpamPoolCidr = Action("ProvisionIpamPoolCidr")
ProvisionPublicIpv4PoolCidr = Action("ProvisionPublicIpv4PoolCidr")
PurchaseCapacityBlock = Action("PurchaseCapacityBlock")
PurchaseCapacityBlockExtension = Action("PurchaseCapacityBlockExtension")
PurchaseHostReservation = Action("PurchaseHostReservation")
PurchaseReservedInstancesOffering = Action("PurchaseReservedInstancesOffering")
PurchaseScheduledInstances = Action("PurchaseScheduledInstances")
PutResourcePolicy = Action("PutResourcePolicy")
RebootInstances = Action("RebootInstances")
RegisterImage = Action("RegisterImage")
RegisterInstanceEventNotificationAttributes = Action(
    "RegisterInstanceEventNotificationAttributes"
)
RegisterTransitGatewayMulticastGroupMembers = Action(
    "RegisterTransitGatewayMulticastGroupMembers"
)
RegisterTransitGatewayMulticastGroupSources = Action(
    "RegisterTransitGatewayMulticastGroupSources"
)
RejectCapacityReservationBillingOwnership = Action(
    "RejectCapacityReservationBillingOwnership"
)
RejectTransitGatewayMulticastDomainAssociations = Action(
    "RejectTransitGatewayMulticastDomainAssociations"
)
RejectTransitGatewayPeeringAttachment = Action("RejectTransitGatewayPeeringAttachment")
RejectTransitGatewayVpcAttachment = Action("RejectTransitGatewayVpcAttachment")
RejectVpcEndpointConnections = Action("RejectVpcEndpointConnections")
RejectVpcPeeringConnection = Action("RejectVpcPeeringConnection")
ReleaseAddress = Action("ReleaseAddress")
ReleaseHosts = Action("ReleaseHosts")
ReleaseIpamPoolAllocation = Action("ReleaseIpamPoolAllocation")
ReplaceIamInstanceProfileAssociation = Action("ReplaceIamInstanceProfileAssociation")
ReplaceImageCriteriaInAllowedImagesSettings = Action(
    "ReplaceImageCriteriaInAllowedImagesSettings"
)
ReplaceNetworkAclAssociation = Action("ReplaceNetworkAclAssociation")
ReplaceNetworkAclEntry = Action("ReplaceNetworkAclEntry")
ReplaceRoute = Action("ReplaceRoute")
ReplaceRouteTableAssociation = Action("ReplaceRouteTableAssociation")
ReplaceTransitGatewayRoute = Action("ReplaceTransitGatewayRoute")
ReplaceVpnTunnel = Action("ReplaceVpnTunnel")
ReportInstanceStatus = Action("ReportInstanceStatus")
RequestSpotFleet = Action("RequestSpotFleet")
RequestSpotInstances = Action("RequestSpotInstances")
ResetAddressAttribute = Action("ResetAddressAttribute")
ResetEbsDefaultKmsKeyId = Action("ResetEbsDefaultKmsKeyId")
ResetFpgaImageAttribute = Action("ResetFpgaImageAttribute")
ResetImageAttribute = Action("ResetImageAttribute")
ResetInstanceAttribute = Action("ResetInstanceAttribute")
ResetNetworkInterfaceAttribute = Action("ResetNetworkInterfaceAttribute")
ResetSnapshotAttribute = Action("ResetSnapshotAttribute")
RestoreAddressToClassic = Action("RestoreAddressToClassic")
RestoreImageFromRecycleBin = Action("RestoreImageFromRecycleBin")
RestoreManagedPrefixListVersion = Action("RestoreManagedPrefixListVersion")
RestoreSnapshotFromRecycleBin = Action("RestoreSnapshotFromRecycleBin")
RestoreSnapshotTier = Action("RestoreSnapshotTier")
RevokeClientVpnIngress = Action("RevokeClientVpnIngress")
RevokeSecurityGroupEgress = Action("RevokeSecurityGroupEgress")
RevokeSecurityGroupIngress = Action("RevokeSecurityGroupIngress")
RunInstances = Action("RunInstances")
RunScheduledInstances = Action("RunScheduledInstances")
SearchLocalGatewayRoutes = Action("SearchLocalGatewayRoutes")
SearchTransitGatewayMulticastGroups = Action("SearchTransitGatewayMulticastGroups")
SearchTransitGatewayRoutes = Action("SearchTransitGatewayRoutes")
SendDiagnosticInterrupt = Action("SendDiagnosticInterrupt")
SendSpotInstanceInterruptions = Action("SendSpotInstanceInterruptions")
StartDeclarativePoliciesReport = Action("StartDeclarativePoliciesReport")
StartInstances = Action("StartInstances")
StartNetworkInsightsAccessScopeAnalysis = Action(
    "StartNetworkInsightsAccessScopeAnalysis"
)
StartNetworkInsightsAnalysis = Action("StartNetworkInsightsAnalysis")
StartVpcEndpointServicePrivateDnsVerification = Action(
    "StartVpcEndpointServicePrivateDnsVerification"
)
StopInstances = Action("StopInstances")
TerminateClientVpnConnections = Action("TerminateClientVpnConnections")
TerminateInstances = Action("TerminateInstances")
UnassignIpv6Addresses = Action("UnassignIpv6Addresses")
UnassignPrivateIpAddresses = Action("UnassignPrivateIpAddresses")
UnassignPrivateNatGatewayAddress = Action("UnassignPrivateNatGatewayAddress")
UnlockSnapshot = Action("UnlockSnapshot")
UnmonitorInstances = Action("UnmonitorInstances")
UpdateSecurityGroupRuleDescriptionsEgress = Action(
    "UpdateSecurityGroupRuleDescriptionsEgress"
)
UpdateSecurityGroupRuleDescriptionsIngress = Action(
    "UpdateSecurityGroupRuleDescriptionsIngress"
)
WithdrawByoipCidr = Action("WithdrawByoipCidr")
