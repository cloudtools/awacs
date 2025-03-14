# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Redshift"
prefix = "redshift"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptReservedNodeExchange = Action("AcceptReservedNodeExchange")
AddPartner = Action("AddPartner")
AssociateDataShareConsumer = Action("AssociateDataShareConsumer")
AuthorizeClusterSecurityGroupIngress = Action("AuthorizeClusterSecurityGroupIngress")
AuthorizeDataShare = Action("AuthorizeDataShare")
AuthorizeEndpointAccess = Action("AuthorizeEndpointAccess")
AuthorizeInboundIntegration = Action("AuthorizeInboundIntegration")
AuthorizeSnapshotAccess = Action("AuthorizeSnapshotAccess")
BatchDeleteClusterSnapshots = Action("BatchDeleteClusterSnapshots")
BatchModifyClusterSnapshots = Action("BatchModifyClusterSnapshots")
CancelQuery = Action("CancelQuery")
CancelQuerySession = Action("CancelQuerySession")
CancelResize = Action("CancelResize")
CopyClusterSnapshot = Action("CopyClusterSnapshot")
CreateAuthenticationProfile = Action("CreateAuthenticationProfile")
CreateCluster = Action("CreateCluster")
CreateClusterParameterGroup = Action("CreateClusterParameterGroup")
CreateClusterSecurityGroup = Action("CreateClusterSecurityGroup")
CreateClusterSnapshot = Action("CreateClusterSnapshot")
CreateClusterSubnetGroup = Action("CreateClusterSubnetGroup")
CreateClusterUser = Action("CreateClusterUser")
CreateCustomDomainAssociation = Action("CreateCustomDomainAssociation")
CreateEndpointAccess = Action("CreateEndpointAccess")
CreateEventSubscription = Action("CreateEventSubscription")
CreateHsmClientCertificate = Action("CreateHsmClientCertificate")
CreateHsmConfiguration = Action("CreateHsmConfiguration")
CreateInboundIntegration = Action("CreateInboundIntegration")
CreateIntegration = Action("CreateIntegration")
CreateQev2IdcApplication = Action("CreateQev2IdcApplication")
CreateRedshiftIdcApplication = Action("CreateRedshiftIdcApplication")
CreateSavedQuery = Action("CreateSavedQuery")
CreateScheduledAction = Action("CreateScheduledAction")
CreateSnapshotCopyGrant = Action("CreateSnapshotCopyGrant")
CreateSnapshotSchedule = Action("CreateSnapshotSchedule")
CreateTags = Action("CreateTags")
CreateUsageLimit = Action("CreateUsageLimit")
DeauthorizeDataShare = Action("DeauthorizeDataShare")
DeleteAuthenticationProfile = Action("DeleteAuthenticationProfile")
DeleteCluster = Action("DeleteCluster")
DeleteClusterParameterGroup = Action("DeleteClusterParameterGroup")
DeleteClusterSecurityGroup = Action("DeleteClusterSecurityGroup")
DeleteClusterSnapshot = Action("DeleteClusterSnapshot")
DeleteClusterSubnetGroup = Action("DeleteClusterSubnetGroup")
DeleteCustomDomainAssociation = Action("DeleteCustomDomainAssociation")
DeleteEndpointAccess = Action("DeleteEndpointAccess")
DeleteEventSubscription = Action("DeleteEventSubscription")
DeleteHsmClientCertificate = Action("DeleteHsmClientCertificate")
DeleteHsmConfiguration = Action("DeleteHsmConfiguration")
DeleteIntegration = Action("DeleteIntegration")
DeletePartner = Action("DeletePartner")
DeleteQev2IdcApplication = Action("DeleteQev2IdcApplication")
DeleteRedshiftIdcApplication = Action("DeleteRedshiftIdcApplication")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSavedQueries = Action("DeleteSavedQueries")
DeleteScheduledAction = Action("DeleteScheduledAction")
DeleteSnapshotCopyGrant = Action("DeleteSnapshotCopyGrant")
DeleteSnapshotSchedule = Action("DeleteSnapshotSchedule")
DeleteTags = Action("DeleteTags")
DeleteUsageLimit = Action("DeleteUsageLimit")
DeregisterNamespace = Action("DeregisterNamespace")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeAuthenticationProfiles = Action("DescribeAuthenticationProfiles")
DescribeClusterDbRevisions = Action("DescribeClusterDbRevisions")
DescribeClusterParameterGroups = Action("DescribeClusterParameterGroups")
DescribeClusterParameters = Action("DescribeClusterParameters")
DescribeClusterSecurityGroups = Action("DescribeClusterSecurityGroups")
DescribeClusterSnapshots = Action("DescribeClusterSnapshots")
DescribeClusterSubnetGroups = Action("DescribeClusterSubnetGroups")
DescribeClusterTracks = Action("DescribeClusterTracks")
DescribeClusterVersions = Action("DescribeClusterVersions")
DescribeClusters = Action("DescribeClusters")
DescribeCustomDomainAssociations = Action("DescribeCustomDomainAssociations")
DescribeDataShares = Action("DescribeDataShares")
DescribeDataSharesForConsumer = Action("DescribeDataSharesForConsumer")
DescribeDataSharesForProducer = Action("DescribeDataSharesForProducer")
DescribeDefaultClusterParameters = Action("DescribeDefaultClusterParameters")
DescribeEndpointAccess = Action("DescribeEndpointAccess")
DescribeEndpointAuthorization = Action("DescribeEndpointAuthorization")
DescribeEventCategories = Action("DescribeEventCategories")
DescribeEventSubscriptions = Action("DescribeEventSubscriptions")
DescribeEvents = Action("DescribeEvents")
DescribeHsmClientCertificates = Action("DescribeHsmClientCertificates")
DescribeHsmConfigurations = Action("DescribeHsmConfigurations")
DescribeInboundIntegrations = Action("DescribeInboundIntegrations")
DescribeIntegrations = Action("DescribeIntegrations")
DescribeLoggingStatus = Action("DescribeLoggingStatus")
DescribeNodeConfigurationOptions = Action("DescribeNodeConfigurationOptions")
DescribeOrderableClusterOptions = Action("DescribeOrderableClusterOptions")
DescribePartners = Action("DescribePartners")
DescribeQev2IdcApplications = Action("DescribeQev2IdcApplications")
DescribeQuery = Action("DescribeQuery")
DescribeRedshiftIdcApplications = Action("DescribeRedshiftIdcApplications")
DescribeReservedNodeExchangeStatus = Action("DescribeReservedNodeExchangeStatus")
DescribeReservedNodeOfferings = Action("DescribeReservedNodeOfferings")
DescribeReservedNodes = Action("DescribeReservedNodes")
DescribeResize = Action("DescribeResize")
DescribeSavedQueries = Action("DescribeSavedQueries")
DescribeScheduledActions = Action("DescribeScheduledActions")
DescribeSnapshotCopyGrants = Action("DescribeSnapshotCopyGrants")
DescribeSnapshotSchedules = Action("DescribeSnapshotSchedules")
DescribeStorage = Action("DescribeStorage")
DescribeTable = Action("DescribeTable")
DescribeTableRestoreStatus = Action("DescribeTableRestoreStatus")
DescribeTags = Action("DescribeTags")
DescribeUsageLimits = Action("DescribeUsageLimits")
DisableLogging = Action("DisableLogging")
DisableSnapshotCopy = Action("DisableSnapshotCopy")
DisassociateDataShareConsumer = Action("DisassociateDataShareConsumer")
EnableLogging = Action("EnableLogging")
EnableSnapshotCopy = Action("EnableSnapshotCopy")
ExecuteQuery = Action("ExecuteQuery")
FailoverPrimaryCompute = Action("FailoverPrimaryCompute")
FetchResults = Action("FetchResults")
GetClusterCredentials = Action("GetClusterCredentials")
GetClusterCredentialsWithIAM = Action("GetClusterCredentialsWithIAM")
GetReservedNodeExchangeConfigurationOptions = Action(
    "GetReservedNodeExchangeConfigurationOptions"
)
GetReservedNodeExchangeOfferings = Action("GetReservedNodeExchangeOfferings")
GetResourcePolicy = Action("GetResourcePolicy")
JoinGroup = Action("JoinGroup")
ListDatabases = Action("ListDatabases")
ListRecommendations = Action("ListRecommendations")
ListSavedQueries = Action("ListSavedQueries")
ListSchemas = Action("ListSchemas")
ListTables = Action("ListTables")
ModifyAquaConfiguration = Action("ModifyAquaConfiguration")
ModifyAuthenticationProfile = Action("ModifyAuthenticationProfile")
ModifyCluster = Action("ModifyCluster")
ModifyClusterDbRevision = Action("ModifyClusterDbRevision")
ModifyClusterIamRoles = Action("ModifyClusterIamRoles")
ModifyClusterMaintenance = Action("ModifyClusterMaintenance")
ModifyClusterParameterGroup = Action("ModifyClusterParameterGroup")
ModifyClusterSnapshot = Action("ModifyClusterSnapshot")
ModifyClusterSnapshotSchedule = Action("ModifyClusterSnapshotSchedule")
ModifyClusterSubnetGroup = Action("ModifyClusterSubnetGroup")
ModifyCustomDomainAssociation = Action("ModifyCustomDomainAssociation")
ModifyEndpointAccess = Action("ModifyEndpointAccess")
ModifyEventSubscription = Action("ModifyEventSubscription")
ModifyIntegration = Action("ModifyIntegration")
ModifyQev2IdcApplication = Action("ModifyQev2IdcApplication")
ModifyRedshiftIdcApplication = Action("ModifyRedshiftIdcApplication")
ModifySavedQuery = Action("ModifySavedQuery")
ModifyScheduledAction = Action("ModifyScheduledAction")
ModifySnapshotCopyRetentionPeriod = Action("ModifySnapshotCopyRetentionPeriod")
ModifySnapshotSchedule = Action("ModifySnapshotSchedule")
ModifyUsageLimit = Action("ModifyUsageLimit")
PauseCluster = Action("PauseCluster")
PurchaseReservedNodeOffering = Action("PurchaseReservedNodeOffering")
PutResourcePolicy = Action("PutResourcePolicy")
RebootCluster = Action("RebootCluster")
RegisterNamespace = Action("RegisterNamespace")
RejectDataShare = Action("RejectDataShare")
ResetClusterParameterGroup = Action("ResetClusterParameterGroup")
ResizeCluster = Action("ResizeCluster")
RestoreFromClusterSnapshot = Action("RestoreFromClusterSnapshot")
RestoreTableFromClusterSnapshot = Action("RestoreTableFromClusterSnapshot")
ResumeCluster = Action("ResumeCluster")
RevokeClusterSecurityGroupIngress = Action("RevokeClusterSecurityGroupIngress")
RevokeEndpointAccess = Action("RevokeEndpointAccess")
RevokeSnapshotAccess = Action("RevokeSnapshotAccess")
RotateEncryptionKey = Action("RotateEncryptionKey")
UpdatePartnerStatus = Action("UpdatePartnerStatus")
ViewQueriesFromConsole = Action("ViewQueriesFromConsole")
ViewQueriesInConsole = Action("ViewQueriesInConsole")
