# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EC2'
prefix = 'ec2'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptReservedInstancesExchangeQuote = \
    Action('AcceptReservedInstancesExchangeQuote')
AcceptTransitGatewayPeeringAttachment = \
    Action('AcceptTransitGatewayPeeringAttachment')
AcceptTransitGatewayVpcAttachment = \
    Action('AcceptTransitGatewayVpcAttachment')
AcceptVpcEndpointConnections = Action('AcceptVpcEndpointConnections')
AcceptVpcPeeringConnection = Action('AcceptVpcPeeringConnection')
AdvertiseByoipCidr = Action('AdvertiseByoipCidr')
AllocateAddress = Action('AllocateAddress')
AllocateHosts = Action('AllocateHosts')
ApplySecurityGroupsToClientVpnTargetNetwork = \
    Action('ApplySecurityGroupsToClientVpnTargetNetwork')
AssignIpv6Addresses = Action('AssignIpv6Addresses')
AssignPrivateIpAddresses = Action('AssignPrivateIpAddresses')
AssociateAddress = Action('AssociateAddress')
AssociateClientVpnTargetNetwork = \
    Action('AssociateClientVpnTargetNetwork')
AssociateDhcpOptions = Action('AssociateDhcpOptions')
AssociateIamInstanceProfile = Action('AssociateIamInstanceProfile')
AssociateRouteTable = Action('AssociateRouteTable')
AssociateSubnetCidrBlock = Action('AssociateSubnetCidrBlock')
AssociateTransitGatewayMulticastDomain = \
    Action('AssociateTransitGatewayMulticastDomain')
AssociateTransitGatewayRouteTable = \
    Action('AssociateTransitGatewayRouteTable')
AssociateVpcCidrBlock = Action('AssociateVpcCidrBlock')
AttachClassicLinkVpc = Action('AttachClassicLinkVpc')
AttachInternetGateway = Action('AttachInternetGateway')
AttachNetworkInterface = Action('AttachNetworkInterface')
AttachVolume = Action('AttachVolume')
AttachVpnGateway = Action('AttachVpnGateway')
AuthorizeClientVpnIngress = Action('AuthorizeClientVpnIngress')
AuthorizeSecurityGroupEgress = Action('AuthorizeSecurityGroupEgress')
AuthorizeSecurityGroupIngress = Action('AuthorizeSecurityGroupIngress')
BundleInstance = Action('BundleInstance')
CancelBundleTask = Action('CancelBundleTask')
CancelCapacityReservation = Action('CancelCapacityReservation')
CancelConversionTask = Action('CancelConversionTask')
CancelExportTask = Action('CancelExportTask')
CancelImportTask = Action('CancelImportTask')
CancelReservedInstancesListing = Action('CancelReservedInstancesListing')
CancelSpotFleetRequests = Action('CancelSpotFleetRequests')
CancelSpotInstanceRequests = Action('CancelSpotInstanceRequests')
ConfirmProductInstance = Action('ConfirmProductInstance')
CopyFpgaImage = Action('CopyFpgaImage')
CopyImage = Action('CopyImage')
CopySnapshot = Action('CopySnapshot')
CreateCapacityReservation = Action('CreateCapacityReservation')
CreateCarrierGateway = Action('CreateCarrierGateway')
CreateClientVpnEndpoint = Action('CreateClientVpnEndpoint')
CreateClientVpnRoute = Action('CreateClientVpnRoute')
CreateCustomerGateway = Action('CreateCustomerGateway')
CreateDefaultSubnet = Action('CreateDefaultSubnet')
CreateDefaultVpc = Action('CreateDefaultVpc')
CreateDhcpOptions = Action('CreateDhcpOptions')
CreateEgressOnlyInternetGateway = \
    Action('CreateEgressOnlyInternetGateway')
CreateFleet = Action('CreateFleet')
CreateFlowLogs = Action('CreateFlowLogs')
CreateFpgaImage = Action('CreateFpgaImage')
CreateImage = Action('CreateImage')
CreateInstanceExportTask = Action('CreateInstanceExportTask')
CreateInternetGateway = Action('CreateInternetGateway')
CreateKeyPair = Action('CreateKeyPair')
CreateLaunchTemplate = Action('CreateLaunchTemplate')
CreateLaunchTemplateVersion = Action('CreateLaunchTemplateVersion')
CreateLocalGatewayRoute = Action('CreateLocalGatewayRoute')
CreateLocalGatewayRouteTableVpcAssociation = \
    Action('CreateLocalGatewayRouteTableVpcAssociation')
CreateManagedPrefixList = Action('CreateManagedPrefixList')
CreateNatGateway = Action('CreateNatGateway')
CreateNetworkAcl = Action('CreateNetworkAcl')
CreateNetworkAclEntry = Action('CreateNetworkAclEntry')
CreateNetworkInterface = Action('CreateNetworkInterface')
CreateNetworkInterfacePermission = \
    Action('CreateNetworkInterfacePermission')
CreatePlacementGroup = Action('CreatePlacementGroup')
CreateReservedInstancesListing = Action('CreateReservedInstancesListing')
CreateRoute = Action('CreateRoute')
CreateRouteTable = Action('CreateRouteTable')
CreateSecurityGroup = Action('CreateSecurityGroup')
CreateSnapshot = Action('CreateSnapshot')
CreateSnapshots = Action('CreateSnapshots')
CreateSpotDatafeedSubscription = Action('CreateSpotDatafeedSubscription')
CreateSubnet = Action('CreateSubnet')
CreateTags = Action('CreateTags')
CreateTrafficMirrorFilter = Action('CreateTrafficMirrorFilter')
CreateTrafficMirrorFilterRule = Action('CreateTrafficMirrorFilterRule')
CreateTrafficMirrorSession = Action('CreateTrafficMirrorSession')
CreateTrafficMirrorTarget = Action('CreateTrafficMirrorTarget')
CreateTransitGateway = Action('CreateTransitGateway')
CreateTransitGatewayMulticastDomain = \
    Action('CreateTransitGatewayMulticastDomain')
CreateTransitGatewayPeeringAttachment = \
    Action('CreateTransitGatewayPeeringAttachment')
CreateTransitGatewayPrefixListReference = \
    Action('CreateTransitGatewayPrefixListReference')
CreateTransitGatewayRoute = Action('CreateTransitGatewayRoute')
CreateTransitGatewayRouteTable = Action('CreateTransitGatewayRouteTable')
CreateTransitGatewayVpcAttachment = \
    Action('CreateTransitGatewayVpcAttachment')
CreateVolume = Action('CreateVolume')
CreateVpc = Action('CreateVpc')
CreateVpcEndpoint = Action('CreateVpcEndpoint')
CreateVpcEndpointConnectionNotification = \
    Action('CreateVpcEndpointConnectionNotification')
CreateVpcEndpointServiceConfiguration = \
    Action('CreateVpcEndpointServiceConfiguration')
CreateVpcPeeringConnection = Action('CreateVpcPeeringConnection')
CreateVpnConnection = Action('CreateVpnConnection')
CreateVpnConnectionRoute = Action('CreateVpnConnectionRoute')
CreateVpnGateway = Action('CreateVpnGateway')
DeleteCarrierGateway = Action('DeleteCarrierGateway')
DeleteClientVpnEndpoint = Action('DeleteClientVpnEndpoint')
DeleteClientVpnRoute = Action('DeleteClientVpnRoute')
DeleteCustomerGateway = Action('DeleteCustomerGateway')
DeleteDhcpOptions = Action('DeleteDhcpOptions')
DeleteEgressOnlyInternetGateway = \
    Action('DeleteEgressOnlyInternetGateway')
DeleteFleets = Action('DeleteFleets')
DeleteFlowLogs = Action('DeleteFlowLogs')
DeleteFpgaImage = Action('DeleteFpgaImage')
DeleteInternetGateway = Action('DeleteInternetGateway')
DeleteKeyPair = Action('DeleteKeyPair')
DeleteLaunchTemplate = Action('DeleteLaunchTemplate')
DeleteLaunchTemplateVersions = Action('DeleteLaunchTemplateVersions')
DeleteLocalGatewayRoute = Action('DeleteLocalGatewayRoute')
DeleteLocalGatewayRouteTableVpcAssociation = \
    Action('DeleteLocalGatewayRouteTableVpcAssociation')
DeleteManagedPrefixList = Action('DeleteManagedPrefixList')
DeleteNatGateway = Action('DeleteNatGateway')
DeleteNetworkAcl = Action('DeleteNetworkAcl')
DeleteNetworkAclEntry = Action('DeleteNetworkAclEntry')
DeleteNetworkInterface = Action('DeleteNetworkInterface')
DeleteNetworkInterfacePermission = \
    Action('DeleteNetworkInterfacePermission')
DeletePlacementGroup = Action('DeletePlacementGroup')
DeleteRoute = Action('DeleteRoute')
DeleteRouteTable = Action('DeleteRouteTable')
DeleteSecurityGroup = Action('DeleteSecurityGroup')
DeleteSnapshot = Action('DeleteSnapshot')
DeleteSpotDatafeedSubscription = Action('DeleteSpotDatafeedSubscription')
DeleteSubnet = Action('DeleteSubnet')
DeleteTags = Action('DeleteTags')
DeleteTrafficMirrorFilter = Action('DeleteTrafficMirrorFilter')
DeleteTrafficMirrorFilterRule = Action('DeleteTrafficMirrorFilterRule')
DeleteTrafficMirrorSession = Action('DeleteTrafficMirrorSession')
DeleteTrafficMirrorTarget = Action('DeleteTrafficMirrorTarget')
DeleteTransitGateway = Action('DeleteTransitGateway')
DeleteTransitGatewayMulticastDomain = \
    Action('DeleteTransitGatewayMulticastDomain')
DeleteTransitGatewayPeeringAttachment = \
    Action('DeleteTransitGatewayPeeringAttachment')
DeleteTransitGatewayPrefixListReference = \
    Action('DeleteTransitGatewayPrefixListReference')
DeleteTransitGatewayRoute = Action('DeleteTransitGatewayRoute')
DeleteTransitGatewayRouteTable = Action('DeleteTransitGatewayRouteTable')
DeleteTransitGatewayVpcAttachment = \
    Action('DeleteTransitGatewayVpcAttachment')
DeleteVolume = Action('DeleteVolume')
DeleteVpc = Action('DeleteVpc')
DeleteVpcEndpointConnectionNotifications = \
    Action('DeleteVpcEndpointConnectionNotifications')
DeleteVpcEndpointServiceConfigurations = \
    Action('DeleteVpcEndpointServiceConfigurations')
DeleteVpcEndpoints = Action('DeleteVpcEndpoints')
DeleteVpcPeeringConnection = Action('DeleteVpcPeeringConnection')
DeleteVpnConnection = Action('DeleteVpnConnection')
DeleteVpnConnectionRoute = Action('DeleteVpnConnectionRoute')
DeleteVpnGateway = Action('DeleteVpnGateway')
DeprovisionByoipCidr = Action('DeprovisionByoipCidr')
DeregisterImage = Action('DeregisterImage')
DeregisterInstanceEventNotificationAttributes = \
    Action('DeregisterInstanceEventNotificationAttributes')
DeregisterTransitGatewayMulticastGroupMembers = \
    Action('DeregisterTransitGatewayMulticastGroupMembers')
DeregisterTransitGatewayMulticastGroupSources = \
    Action('DeregisterTransitGatewayMulticastGroupSources')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeAddresses = Action('DescribeAddresses')
DescribeAggregateIdFormat = Action('DescribeAggregateIdFormat')
DescribeAvailabilityZones = Action('DescribeAvailabilityZones')
DescribeBundleTasks = Action('DescribeBundleTasks')
DescribeByoipCidrs = Action('DescribeByoipCidrs')
DescribeCapacityReservations = Action('DescribeCapacityReservations')
DescribeCarrierGateways = Action('DescribeCarrierGateways')
DescribeClassicLinkInstances = Action('DescribeClassicLinkInstances')
DescribeClientVpnAuthorizationRules = \
    Action('DescribeClientVpnAuthorizationRules')
DescribeClientVpnConnections = Action('DescribeClientVpnConnections')
DescribeClientVpnEndpoints = Action('DescribeClientVpnEndpoints')
DescribeClientVpnRoutes = Action('DescribeClientVpnRoutes')
DescribeClientVpnTargetNetworks = \
    Action('DescribeClientVpnTargetNetworks')
DescribeCoipPools = Action('DescribeCoipPools')
DescribeConversionTasks = Action('DescribeConversionTasks')
DescribeCustomerGateways = Action('DescribeCustomerGateways')
DescribeDhcpOptions = Action('DescribeDhcpOptions')
DescribeEgressOnlyInternetGateways = \
    Action('DescribeEgressOnlyInternetGateways')
DescribeElasticGpus = Action('DescribeElasticGpus')
DescribeExportImageTasks = Action('DescribeExportImageTasks')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeFastSnapshotRestores = Action('DescribeFastSnapshotRestores')
DescribeFleetHistory = Action('DescribeFleetHistory')
DescribeFleetInstances = Action('DescribeFleetInstances')
DescribeFleets = Action('DescribeFleets')
DescribeFlowLogs = Action('DescribeFlowLogs')
DescribeFpgaImageAttribute = Action('DescribeFpgaImageAttribute')
DescribeFpgaImages = Action('DescribeFpgaImages')
DescribeHostReservationOfferings = \
    Action('DescribeHostReservationOfferings')
DescribeHostReservations = Action('DescribeHostReservations')
DescribeHosts = Action('DescribeHosts')
DescribeIamInstanceProfileAssociations = \
    Action('DescribeIamInstanceProfileAssociations')
DescribeIdFormat = Action('DescribeIdFormat')
DescribeIdentityIdFormat = Action('DescribeIdentityIdFormat')
DescribeImageAttribute = Action('DescribeImageAttribute')
DescribeImages = Action('DescribeImages')
DescribeImportImageTasks = Action('DescribeImportImageTasks')
DescribeImportSnapshotTasks = Action('DescribeImportSnapshotTasks')
DescribeInstanceAttribute = Action('DescribeInstanceAttribute')
DescribeInstanceCreditSpecifications = \
    Action('DescribeInstanceCreditSpecifications')
DescribeInstanceEventNotificationAttributes = \
    Action('DescribeInstanceEventNotificationAttributes')
DescribeInstanceStatus = Action('DescribeInstanceStatus')
DescribeInstanceTypeOfferings = Action('DescribeInstanceTypeOfferings')
DescribeInstanceTypes = Action('DescribeInstanceTypes')
DescribeInstances = Action('DescribeInstances')
DescribeInternetGateways = Action('DescribeInternetGateways')
DescribeKeyPairs = Action('DescribeKeyPairs')
DescribeLaunchTemplateVersions = Action('DescribeLaunchTemplateVersions')
DescribeLaunchTemplates = Action('DescribeLaunchTemplates')
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations = \
    Action('DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations')
DescribeLocalGatewayRouteTableVpcAssociations = \
    Action('DescribeLocalGatewayRouteTableVpcAssociations')
DescribeLocalGatewayRouteTables = \
    Action('DescribeLocalGatewayRouteTables')
DescribeLocalGatewayVirtualInterfaceGroups = \
    Action('DescribeLocalGatewayVirtualInterfaceGroups')
DescribeLocalGatewayVirtualInterfaces = \
    Action('DescribeLocalGatewayVirtualInterfaces')
DescribeLocalGateways = Action('DescribeLocalGateways')
DescribeManagedPrefixLists = Action('DescribeManagedPrefixLists')
DescribeMovingAddresses = Action('DescribeMovingAddresses')
DescribeNatGateways = Action('DescribeNatGateways')
DescribeNetworkAcls = Action('DescribeNetworkAcls')
DescribeNetworkInterfaceAttribute = \
    Action('DescribeNetworkInterfaceAttribute')
DescribeNetworkInterfacePermissions = \
    Action('DescribeNetworkInterfacePermissions')
DescribeNetworkInterfaces = Action('DescribeNetworkInterfaces')
DescribePlacementGroups = Action('DescribePlacementGroups')
DescribePrefixLists = Action('DescribePrefixLists')
DescribePrincipalIdFormat = Action('DescribePrincipalIdFormat')
DescribePublicIpv4Pools = Action('DescribePublicIpv4Pools')
DescribeRegions = Action('DescribeRegions')
DescribeReservedInstances = Action('DescribeReservedInstances')
DescribeReservedInstancesListings = \
    Action('DescribeReservedInstancesListings')
DescribeReservedInstancesModifications = \
    Action('DescribeReservedInstancesModifications')
DescribeReservedInstancesOfferings = \
    Action('DescribeReservedInstancesOfferings')
DescribeRouteTables = Action('DescribeRouteTables')
DescribeScheduledInstanceAvailability = \
    Action('DescribeScheduledInstanceAvailability')
DescribeScheduledInstances = Action('DescribeScheduledInstances')
DescribeSecurityGroupReferences = \
    Action('DescribeSecurityGroupReferences')
DescribeSecurityGroups = Action('DescribeSecurityGroups')
DescribeSnapshotAttribute = Action('DescribeSnapshotAttribute')
DescribeSnapshots = Action('DescribeSnapshots')
DescribeSpotDatafeedSubscription = \
    Action('DescribeSpotDatafeedSubscription')
DescribeSpotFleetInstances = Action('DescribeSpotFleetInstances')
DescribeSpotFleetRequestHistory = \
    Action('DescribeSpotFleetRequestHistory')
DescribeSpotFleetRequests = Action('DescribeSpotFleetRequests')
DescribeSpotInstanceRequests = Action('DescribeSpotInstanceRequests')
DescribeSpotPriceHistory = Action('DescribeSpotPriceHistory')
DescribeStaleSecurityGroups = Action('DescribeStaleSecurityGroups')
DescribeSubnets = Action('DescribeSubnets')
DescribeTags = Action('DescribeTags')
DescribeTrafficMirrorFilters = Action('DescribeTrafficMirrorFilters')
DescribeTrafficMirrorSessions = Action('DescribeTrafficMirrorSessions')
DescribeTrafficMirrorTargets = Action('DescribeTrafficMirrorTargets')
DescribeTransitGatewayAttachments = \
    Action('DescribeTransitGatewayAttachments')
DescribeTransitGatewayMulticastDomains = \
    Action('DescribeTransitGatewayMulticastDomains')
DescribeTransitGatewayPeeringAttachments = \
    Action('DescribeTransitGatewayPeeringAttachments')
DescribeTransitGatewayRouteTables = \
    Action('DescribeTransitGatewayRouteTables')
DescribeTransitGatewayVpcAttachments = \
    Action('DescribeTransitGatewayVpcAttachments')
DescribeTransitGateways = Action('DescribeTransitGateways')
DescribeVolumeAttribute = Action('DescribeVolumeAttribute')
DescribeVolumeStatus = Action('DescribeVolumeStatus')
DescribeVolumes = Action('DescribeVolumes')
DescribeVolumesModifications = Action('DescribeVolumesModifications')
DescribeVpcAttribute = Action('DescribeVpcAttribute')
DescribeVpcClassicLink = Action('DescribeVpcClassicLink')
DescribeVpcClassicLinkDnsSupport = \
    Action('DescribeVpcClassicLinkDnsSupport')
DescribeVpcEndpointConnectionNotifications = \
    Action('DescribeVpcEndpointConnectionNotifications')
DescribeVpcEndpointConnections = Action('DescribeVpcEndpointConnections')
DescribeVpcEndpointServiceConfigurations = \
    Action('DescribeVpcEndpointServiceConfigurations')
DescribeVpcEndpointServicePermissions = \
    Action('DescribeVpcEndpointServicePermissions')
DescribeVpcEndpointServices = Action('DescribeVpcEndpointServices')
DescribeVpcEndpoints = Action('DescribeVpcEndpoints')
DescribeVpcPeeringConnections = Action('DescribeVpcPeeringConnections')
DescribeVpcs = Action('DescribeVpcs')
DescribeVpnConnections = Action('DescribeVpnConnections')
DescribeVpnGateways = Action('DescribeVpnGateways')
DetachClassicLinkVpc = Action('DetachClassicLinkVpc')
DetachInternetGateway = Action('DetachInternetGateway')
DetachNetworkInterface = Action('DetachNetworkInterface')
DetachVolume = Action('DetachVolume')
DetachVpnGateway = Action('DetachVpnGateway')
DisableEbsEncryptionByDefault = Action('DisableEbsEncryptionByDefault')
DisableFastSnapshotRestores = Action('DisableFastSnapshotRestores')
DisableTransitGatewayRouteTablePropagation = \
    Action('DisableTransitGatewayRouteTablePropagation')
DisableVgwRoutePropagation = Action('DisableVgwRoutePropagation')
DisableVpcClassicLink = Action('DisableVpcClassicLink')
DisableVpcClassicLinkDnsSupport = \
    Action('DisableVpcClassicLinkDnsSupport')
DisassociateAddress = Action('DisassociateAddress')
DisassociateClientVpnTargetNetwork = \
    Action('DisassociateClientVpnTargetNetwork')
DisassociateIamInstanceProfile = Action('DisassociateIamInstanceProfile')
DisassociateRouteTable = Action('DisassociateRouteTable')
DisassociateSubnetCidrBlock = Action('DisassociateSubnetCidrBlock')
DisassociateTransitGatewayMulticastDomain = \
    Action('DisassociateTransitGatewayMulticastDomain')
DisassociateTransitGatewayRouteTable = \
    Action('DisassociateTransitGatewayRouteTable')
DisassociateVpcCidrBlock = Action('DisassociateVpcCidrBlock')
EnableEbsEncryptionByDefault = Action('EnableEbsEncryptionByDefault')
EnableFastSnapshotRestores = Action('EnableFastSnapshotRestores')
EnableTransitGatewayRouteTablePropagation = \
    Action('EnableTransitGatewayRouteTablePropagation')
EnableVgwRoutePropagation = Action('EnableVgwRoutePropagation')
EnableVolumeIO = Action('EnableVolumeIO')
EnableVpcClassicLink = Action('EnableVpcClassicLink')
EnableVpcClassicLinkDnsSupport = Action('EnableVpcClassicLinkDnsSupport')
ExportClientVpnClientCertificateRevocationList = \
    Action('ExportClientVpnClientCertificateRevocationList')
ExportClientVpnClientConfiguration = \
    Action('ExportClientVpnClientConfiguration')
ExportImage = Action('ExportImage')
ExportTransitGatewayRoutes = Action('ExportTransitGatewayRoutes')
GetCapacityReservationUsage = Action('GetCapacityReservationUsage')
GetCoipPoolUsage = Action('GetCoipPoolUsage')
GetConsoleOutput = Action('GetConsoleOutput')
GetConsoleScreenshot = Action('GetConsoleScreenshot')
GetDefaultCreditSpecification = Action('GetDefaultCreditSpecification')
GetEbsDefaultKmsKeyId = Action('GetEbsDefaultKmsKeyId')
GetEbsEncryptionByDefault = Action('GetEbsEncryptionByDefault')
GetHostReservationPurchasePreview = \
    Action('GetHostReservationPurchasePreview')
GetLaunchTemplateData = Action('GetLaunchTemplateData')
GetManagedPrefixListAssociations = \
    Action('GetManagedPrefixListAssociations')
GetManagedPrefixListEntries = Action('GetManagedPrefixListEntries')
GetPasswordData = Action('GetPasswordData')
GetReservedInstancesExchangeQuote = \
    Action('GetReservedInstancesExchangeQuote')
GetTransitGatewayAttachmentPropagations = \
    Action('GetTransitGatewayAttachmentPropagations')
GetTransitGatewayMulticastDomainAssociations = \
    Action('GetTransitGatewayMulticastDomainAssociations')
GetTransitGatewayPrefixListReferences = \
    Action('GetTransitGatewayPrefixListReferences')
GetTransitGatewayRouteTableAssociations = \
    Action('GetTransitGatewayRouteTableAssociations')
GetTransitGatewayRouteTablePropagations = \
    Action('GetTransitGatewayRouteTablePropagations')
ImportClientVpnClientCertificateRevocationList = \
    Action('ImportClientVpnClientCertificateRevocationList')
ImportImage = Action('ImportImage')
ImportInstance = Action('ImportInstance')
ImportKeyPair = Action('ImportKeyPair')
ImportSnapshot = Action('ImportSnapshot')
ImportVolume = Action('ImportVolume')
ModifyCapacityReservation = Action('ModifyCapacityReservation')
ModifyClientVpnEndpoint = Action('ModifyClientVpnEndpoint')
ModifyDefaultCreditSpecification = \
    Action('ModifyDefaultCreditSpecification')
ModifyEbsDefaultKmsKeyId = Action('ModifyEbsDefaultKmsKeyId')
ModifyFleet = Action('ModifyFleet')
ModifyFpgaImageAttribute = Action('ModifyFpgaImageAttribute')
ModifyHosts = Action('ModifyHosts')
ModifyIdFormat = Action('ModifyIdFormat')
ModifyIdentityIdFormat = Action('ModifyIdentityIdFormat')
ModifyImageAttribute = Action('ModifyImageAttribute')
ModifyInstanceAttribute = Action('ModifyInstanceAttribute')
ModifyInstanceCapacityReservationAttributes = \
    Action('ModifyInstanceCapacityReservationAttributes')
ModifyInstanceCreditSpecification = \
    Action('ModifyInstanceCreditSpecification')
ModifyInstanceEventStartTime = Action('ModifyInstanceEventStartTime')
ModifyInstanceMetadataOptions = Action('ModifyInstanceMetadataOptions')
ModifyInstancePlacement = Action('ModifyInstancePlacement')
ModifyLaunchTemplate = Action('ModifyLaunchTemplate')
ModifyManagedPrefixList = Action('ModifyManagedPrefixList')
ModifyNetworkInterfaceAttribute = \
    Action('ModifyNetworkInterfaceAttribute')
ModifyReservedInstances = Action('ModifyReservedInstances')
ModifySnapshotAttribute = Action('ModifySnapshotAttribute')
ModifySpotFleetRequest = Action('ModifySpotFleetRequest')
ModifySubnetAttribute = Action('ModifySubnetAttribute')
ModifyTrafficMirrorFilterNetworkServices = \
    Action('ModifyTrafficMirrorFilterNetworkServices')
ModifyTrafficMirrorFilterRule = Action('ModifyTrafficMirrorFilterRule')
ModifyTrafficMirrorSession = Action('ModifyTrafficMirrorSession')
ModifyTransitGateway = Action('ModifyTransitGateway')
ModifyTransitGatewayPrefixListReference = \
    Action('ModifyTransitGatewayPrefixListReference')
ModifyTransitGatewayVpcAttachment = \
    Action('ModifyTransitGatewayVpcAttachment')
ModifyVolume = Action('ModifyVolume')
ModifyVolumeAttribute = Action('ModifyVolumeAttribute')
ModifyVpcAttribute = Action('ModifyVpcAttribute')
ModifyVpcEndpoint = Action('ModifyVpcEndpoint')
ModifyVpcEndpointConnectionNotification = \
    Action('ModifyVpcEndpointConnectionNotification')
ModifyVpcEndpointServiceConfiguration = \
    Action('ModifyVpcEndpointServiceConfiguration')
ModifyVpcEndpointServicePermissions = \
    Action('ModifyVpcEndpointServicePermissions')
ModifyVpcPeeringConnectionOptions = \
    Action('ModifyVpcPeeringConnectionOptions')
ModifyVpcTenancy = Action('ModifyVpcTenancy')
ModifyVpnConnection = Action('ModifyVpnConnection')
ModifyVpnTunnelCertificate = Action('ModifyVpnTunnelCertificate')
ModifyVpnTunnelOptions = Action('ModifyVpnTunnelOptions')
MonitorInstances = Action('MonitorInstances')
MoveAddressToVpc = Action('MoveAddressToVpc')
ProvisionByoipCidr = Action('ProvisionByoipCidr')
PurchaseHostReservation = Action('PurchaseHostReservation')
PurchaseReservedInstancesOffering = \
    Action('PurchaseReservedInstancesOffering')
PurchaseScheduledInstances = Action('PurchaseScheduledInstances')
RebootInstances = Action('RebootInstances')
RegisterImage = Action('RegisterImage')
RegisterInstanceEventNotificationAttributes = \
    Action('RegisterInstanceEventNotificationAttributes')
RegisterTransitGatewayMulticastGroupMembers = \
    Action('RegisterTransitGatewayMulticastGroupMembers')
RegisterTransitGatewayMulticastGroupSources = \
    Action('RegisterTransitGatewayMulticastGroupSources')
RejectTransitGatewayPeeringAttachment = \
    Action('RejectTransitGatewayPeeringAttachment')
RejectTransitGatewayVpcAttachment = \
    Action('RejectTransitGatewayVpcAttachment')
RejectVpcEndpointConnections = Action('RejectVpcEndpointConnections')
RejectVpcPeeringConnection = Action('RejectVpcPeeringConnection')
ReleaseAddress = Action('ReleaseAddress')
ReleaseHosts = Action('ReleaseHosts')
ReplaceIamInstanceProfileAssociation = \
    Action('ReplaceIamInstanceProfileAssociation')
ReplaceNetworkAclAssociation = Action('ReplaceNetworkAclAssociation')
ReplaceNetworkAclEntry = Action('ReplaceNetworkAclEntry')
ReplaceRoute = Action('ReplaceRoute')
ReplaceRouteTableAssociation = Action('ReplaceRouteTableAssociation')
ReplaceTransitGatewayRoute = Action('ReplaceTransitGatewayRoute')
ReportInstanceStatus = Action('ReportInstanceStatus')
RequestSpotFleet = Action('RequestSpotFleet')
RequestSpotInstances = Action('RequestSpotInstances')
ResetEbsDefaultKmsKeyId = Action('ResetEbsDefaultKmsKeyId')
ResetFpgaImageAttribute = Action('ResetFpgaImageAttribute')
ResetImageAttribute = Action('ResetImageAttribute')
ResetInstanceAttribute = Action('ResetInstanceAttribute')
ResetNetworkInterfaceAttribute = Action('ResetNetworkInterfaceAttribute')
ResetSnapshotAttribute = Action('ResetSnapshotAttribute')
RestoreAddressToClassic = Action('RestoreAddressToClassic')
RestoreManagedPrefixListVersion = \
    Action('RestoreManagedPrefixListVersion')
RevokeClientVpnIngress = Action('RevokeClientVpnIngress')
RevokeSecurityGroupEgress = Action('RevokeSecurityGroupEgress')
RevokeSecurityGroupIngress = Action('RevokeSecurityGroupIngress')
RunInstances = Action('RunInstances')
RunScheduledInstances = Action('RunScheduledInstances')
SearchLocalGatewayRoutes = Action('SearchLocalGatewayRoutes')
SearchTransitGatewayMulticastGroups = \
    Action('SearchTransitGatewayMulticastGroups')
SearchTransitGatewayRoutes = Action('SearchTransitGatewayRoutes')
SendDiagnosticInterrupt = Action('SendDiagnosticInterrupt')
StartInstances = Action('StartInstances')
StartVpcEndpointServicePrivateDnsVerification = \
    Action('StartVpcEndpointServicePrivateDnsVerification')
StopInstances = Action('StopInstances')
TerminateClientVpnConnections = Action('TerminateClientVpnConnections')
TerminateInstances = Action('TerminateInstances')
UnassignIpv6Addresses = Action('UnassignIpv6Addresses')
UnassignPrivateIpAddresses = Action('UnassignPrivateIpAddresses')
UnmonitorInstances = Action('UnmonitorInstances')
UpdateSecurityGroupRuleDescriptionsEgress = \
    Action('UpdateSecurityGroupRuleDescriptionsEgress')
UpdateSecurityGroupRuleDescriptionsIngress = \
    Action('UpdateSecurityGroupRuleDescriptionsIngress')
WithdrawByoipCidr = Action('WithdrawByoipCidr')
