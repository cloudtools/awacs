#!/usr/bin/env python
#
# Generate Actions from AWS static configuration
#
import json
import os
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit.visitors.ecmavisitor import ECMAVisitor
from slimit import ast


header = """\
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN
"""

extra_classes = """\
class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)
"""

extra_classes_s3 = """\
class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        # account is empty for S3
        account = ''
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)
"""

arn = """\
class %(upper)s_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(%(upper)s_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use %(lower)s.ARN instead.",
                      FutureWarning)
"""

legacy_arns = ['iam', 's3', 'sdb', 'sns', 'sqs']

aws_url = \
    "https://awsiamconsole.s3.amazonaws.com/iam/assets/js/bundles/policies.js"

basedir = 'generated'

response = urlopen(aws_url)
config = response.read()


class JSONVisitor(ECMAVisitor):
    def visit_Identifier(self, node):
        return '"%s"' % node.value

    def visit_Number(self, node):
        return '"%s"' % node.value

    def visit_UnaryOp(self, node):
        s = self.visit(node.value)
        if node.op == '!' and s == 0:
            return '"true"'
        else:
            return s


visitor = JSONVisitor()
parser = Parser()
tree = parser.parse(config.decode('utf-8'))

flag = False
policy_editor_config = ""
for node in nodevisitor.visit(tree):
    if (isinstance(node, ast.Identifier) and
            node.value == 'PolicyEditorConfig'):
        flag = True
    elif flag:
        policy_editor_config = visitor.visit(node)
        break

d = json.loads(policy_editor_config)

try:
    os.mkdir(basedir)
except OSError:
    pass


# Extra services are for those not advertised in policies.js,
# but are available to be called via AWS apis. If/When these
# services are added to policies.js, the entry in extra_services
# will be ignored. IE, policies.js takes priority over
# extra_services entries.

extra_services = {
    'AWS Certificate Manager Private Certificate Authority': {
        'StringPrefix': 'acm-pca',
        'Actions': [
            'CreateCertificateAuthority',
            'CreateCertificateAuthorityAuditReport',
            'DeleteCertificateAuthority',
            'DescribeCertificateAuthority',
            'DescribeCertificateAuthorityAuditReport',
            'GetCertificate',
            'GetCertificateAuthorityCertificate',
            'GetCertificateAuthorityCsr',
            'ImportCertificateAuthorityCertificate',
            'IssueCertificate',
            'ListCertificateAuthorities',
            'ListTags',
            'RestoreCertificateAuthority',
            'RevokeCertificate',
            'TagCertificateAuthority',
            'UntagCertificateAuthority',
            'UpdateCertificateAuthority',
        ],
    },
    'AWS Amplify': {
        'StringPrefix': 'amplify',
        'Actions': [
            'CreateApp',
            'CreateBranch',
            'CreateDomainAssociation',
            'DeleteApp',
            'DeleteBranch',
            'DeleteDomainAssociation',
            'DeleteJob',
            'GetApp',
            'GetBranch',
            'GetDomainAssociation',
            'GetJob',
            'ListApps',
            'ListBranches',
            'ListDomainAssociations',
            'ListJobs',
            'StartJob',
            'StopJob',
            'UpdateApp',
            'UpdateBranch',
            'UpdateDomainAssociation',
        ],
    },
    'AWS Backup': {
        'StringPrefix': 'backup',
        'Actions': [
            'CreateBackupPlan',
            'CreateBackupSelection',
            'CreateBackupVault',
            'DeleteBackupPlan',
            'DeleteBackupSelection',
            'DeleteBackupVault',
            'DeleteBackupVaultAccessPolicy',
            'DeleteBackupVaultNotifications',
            'DeleteRecoveryPoint',
            'DescribeBackupJob',
            'DescribeBackupVault',
            'DescribeProtectedResource',
            'DescribeRecoveryPoint',
            'DescribeRestoreJob',
            'ExportBackupPlanTemplate',
            'GetBackupPlan',
            'GetBackupPlanFromJSON',
            'GetBackupPlanFromTemplate',
            'GetBackupSelection',
            'GetBackupVaultAccessPolicy',
            'GetBackupVaultNotifications',
            'GetRecoveryPointRestoreMetadata',
            'GetSupportedResourceTypes',
            'ListBackupJobs',
            'ListBackupPlanTemplates',
            'ListBackupPlanVersions',
            'ListBackupPlans',
            'ListBackupSelections',
            'ListBackupVaults',
            'ListProtectedResources',
            'ListRecoveryPointsByBackupVault',
            'ListRecoveryPointsByResource',
            'ListRestoreJobs',
            'ListTags',
            'PutBackupVaultAccessPolicy',
            'PutBackupVaultNotifications',
            'StartBackupJob',
            'StartRestoreJob',
            'StopBackupJob',
            'TagResource',
            'UntagResource',
            'UpdateBackupPlan',
            'UpdateRecoveryPointLifecycle',
        ],
    },
    'Comprehend Medical': {
        'StringPrefix': 'comprehendmedical',
        'Actions': [
            'DetectEntities',
            'DetectPHI',
        ],
    },
    'DataSync': {
        'StringPrefix': 'datasync',
        'Actions': [
            'CancelTaskExecution',
            'CreateAgent',
            'CreateLocationEfs',
            'CreateLocationNfs',
            'CreateLocationS3',
            'CreateTask',
            'DeleteAgent',
            'DeleteLocation',
            'DeleteTask',
            'DescribeAgent',
            'DescribeLocationEfs',
            'DescribeLocationNfs',
            'DescribeLocationS3',
            'DescribeTask',
            'DescribeTaskExecution',
            'ListAgents',
            'ListLocations',
            'ListTagsForResource',
            'ListTaskExecutions',
            'ListTasks',
            'StartTaskExecution',
            'TagResource',
            'UntagResource',
            'UpdateAgent',
            'UpdateTask',
        ],
    },
    'AWS DeepLens': {
        'StringPrefix': 'deeplens',
        'Actions': [
            'AssociateServiceRoleToAccount',
            'BatchGetDevice',
            'BatchGetModel',
            'BatchGetProject',
            'CreateDeviceCertificates',
            'CreateModel',
            'CreateProject',
            'DeleteModel',
            'DeleteProject',
            'DeployProject',
            'DeregisterDevice',
            'GetAssociatedResources',
            'GetDeploymentStatus',
            'GetDevice',
            'GetModel',
            'GetProject',
            'ImportProjectFromTemplate',
            'ListDeployments',
            'ListDevices',
            'ListModels',
            'ListProjects',
            'RegisterDevice',
            'RemoveProject',
            'UpdateProject',
        ],
    },
    'Amazon Data Lifecycle Manager': {
        'StringPrefix': 'dlm',
        'Actions': [
            'CreateLifecyclePolicy',
            'DeleteLifecyclePolicy',
            'GetLifecyclePolicies',
            'GetLifecyclePolicy',
            'UpdateLifecyclePolicy',
        ],
    },
    'Amazon Elastic Container Service for Kubernetes': {
        'StringPrefix': 'eks',
        'Actions': [
            'CreateCluster',
            'DeleteCluster',
            'DescribeCluster',
            'DescribeUpdate',
            'ListClusters',
            'ListUpdates',
            'UpdateClusterVersion',
        ],
    },
    'Amazon Elastic Inference': {
        'StringPrefix': 'elastic-inference',
        'Actions': [
            'Connect',
        ],
    },
    'AWS Firewall Manager': {
        'StringPrefix': 'fms',
        'Actions': [
            'AssociateAdminAccount',
            'DeleteNotificationChannel',
            'DeletePolicy',
            'DisassociateAdminAccount',
            'GetAdminAccount',
            'GetComplianceDetail',
            'GetNotificationChannel',
            'GetPolicy',
            'ListComplianceStatus',
            'ListMemberAccounts',
            'ListPolicies',
            'PutNotificationChannel',
            'PutPolicy',
        ],
    },
    'Amazon FSx': {
        'StringPrefix': 'fsx',
        'Actions': [
            'CreateBackup',
            'CreateFileSystem',
            'CreateFileSystemFromBackup',
            'DeleteBackup',
            'DeleteFileSystem',
            'DescribeBackups',
            'DescribeFileSystems',
            'ListTagsForResource',
            'TagResource',
            'UntagResource',
            'UpdateFileSystem',
        ],
    },
    'Global Accelerator': {
        'StringPrefix': 'globalaccelerator',
        'Actions': [
            'CreateAccelerator',
            'CreateEndpointGroup',
            'CreateListener',
            'DeleteAccelerator',
            'DeleteEndpointGroup',
            'DeleteListener',
            'DescribeAccelerator',
            'DescribeAcceleratorAttributes',
            'DescribeEndpointGroup',
            'DescribeListener',
            'ListAccelerators',
            'ListEndpointGroups',
            'ListListeners',
            'UpdateAccelerator',
            'UpdateAcceleratorAttributes',
            'UpdateEndpointGroup',
            'UpdateListener',
        ],
    },
    'Amazon GroundTruth Labeling': {
        'StringPrefix': 'groundtruthlabeling',
        'Actions': [
            'DescribeConsoleJob',
            'ListDatasetObjects',
            'RunFilterOrSampleDatasetJob',
            'RunGenerateManifestByCrawlingJob',
        ],
    },
    'AWS IoT 1-Click': {
        'StringPrefix': 'iot1click',
        'Actions': [
            'AssociateDeviceWithPlacement',
            'ClaimDevicesByClaimCode',
            'CreatePlacement',
            'CreateProject',
            'DeletePlacement',
            'DeleteProject',
            'DescribeDevice',
            'DescribePlacement',
            'DescribeProject',
            'DisassociateDeviceFromPlacement',
            'FinalizeDeviceClaim',
            'GetDeviceMethods',
            'GetDevicesInPlacement',
            'InitializeDeviceClaim',
            'InvokeDeviceMethod',
            'ListDeviceEvents',
            'ListDevices',
            'ListPlacements',
            'ListProjects',
            'UnclaimDevice',
            'UpdateDeviceState',
            'UpdatePlacement',
            'UpdateProject',
        ],
    },
    'AWS IoT Events': {
        'StringPrefix': 'iotevents',
        'Actions': [
            'BatchPutMessage',
            'CreateDetectorModel',
            'CreateInput',
            'DeleteDetectorModel',
            'DeleteInput',
            'DescribeDetector',
            'DescribeDetectorModel',
            'DescribeInput',
            'DescribeLoggingOptions',
            'ListDetectorModelVersions',
            'ListDetectorModels',
            'ListDetectors',
            'ListInputs',
            'PutLoggingOptions',
            'UpdateDetectorModel',
            'UpdateInput',
        ],
    },
    'AWS IoT SiteWise': {
        'StringPrefix': 'iotsitewise',
        'Actions': [
            'AssociateGatewaySink',
            'AssociateGatewaySource',
            'AssociateViewEntities',
            'CreateAsset',
            'CreateAssetTemplate',
            'CreateGateway',
            'CreateGroup',
            'CreateMeasurementDataStore',
            'CreateMetricType',
            'CreateView',
            'DeleteAsset',
            'DeleteAssetTemplate',
            'DeleteGateway',
            'DeleteGroup',
            'DeleteMeasurementDataStore',
            'DeleteMetricType',
            'DeleteView',
            'DeregisterViewEntities',
            'DescribeAssetTemplates',
            'DescribeAssets',
            'DescribeGateways',
            'DescribeGroups',
            'DescribeMeasurementDataStores',
            'DescribeMetricTypes',
            'DescribeViews',
            'DisassociateGatewaySink',
            'DisassociateGatewaySource',
            'DisassociateViewEntities',
            'GetMeasurementData',
            'GetMetricData',
            'ListAssetTemplates',
            'ListAssets',
            'ListGateways',
            'ListGroups',
            'ListMeasurementDataStores',
            'ListMeasurementDataStreams',
            'ListMetricTypes',
            'ListViewEntities',
            'ListViews',
            'RegisterViewEntities',
            'UpdateAsset',
            'UpdateAssetTemplate',
            'UpdateGateway',
            'UpdateGroup',
            'UpdateMeasurementDataStore',
            'UpdateView',
        ],
    },
    'Amazon Managed Streaming for Kafka': {
        'StringPrefix': 'kafka',
        'Actions': [
            'CreateCluster',
            'DeleteCluster',
            'DescribeCluster',
            'GetBootstrapBrokers',
            'ListClusters',
            'ListNodes',
        ],
    },
    'AWS License Manager': {
        'StringPrefix': 'license-manager',
        'Actions': [
            'CreateLicenseConfiguration',
            'DeleteLicenseConfiguration',
            'GetLicenseConfiguration',
            'GetServiceSettings',
            'ListAssociationsForLicenseConfiguration',
            'ListLicenseConfigurations',
            'ListLicenseSpecificationsForResource',
            'ListResourceInventory',
            'ListTagsForResource',
            'ListUsageForLicenseConfiguration',
            'TagResource',
            'UntagResource',
            'UpdateLicenseConfiguration',
            'UpdateLicenseSpecificationsForResource',
            'UpdateServiceSettings',
        ],
    },
    'Amazon Macie': {
        'StringPrefix': 'macie',
        'Actions': [
            'AssociateMemberAccount',
            'AssociateS3Resources',
            'DisassociateMemberAccount',
            'DisassociateS3Resources',
            'ListMemberAccounts',
            'ListS3Resources',
            'UpdateS3Resources',
        ],
    },
    'AWS Elemental MediaConnect': {
        'StringPrefix': 'mediaconnect',
        'Actions': [
            'AddFlowOutputs',
            'CreateFlow',
            'DeleteFlow',
            'DescribeFlow',
            'GrantFlowEntitlements',
            'ListEntitlements',
            'ListFlows',
            'RemoveFlowOutput',
            'RevokeFlowEntitlement',
            'StartFlow',
            'StopFlow',
            'UpdateFlowEntitlement',
            'UpdateFlowOutput',
            'UpdateFlowSource',
        ],
    },
    'Amazon Neptune': {
        'StringPrefix': 'neptune-db',
        'Actions': [
            'connect',
        ],
    },
    'AWS Performance Insights': {
        'StringPrefix': 'pi',
        'Actions': [
            'DescribeDimensionKeys',
            'GetResourceMetrics',
        ],
    },
    'AWS Resource Access Manager': {
        'StringPrefix': 'ram',
        'Actions': [
            'AcceptResourceShareInvitation',
            'AssociateResourceShare',
            'CreateResourceShare',
            'DeleteResourceShare',
            'DisassociateResourceShare',
            'EnableSharingWithAwsOrganization',
            'GetResourceShareAssociations',
            'GetResourceShareInvitations',
            'GetResourceShares',
            'ListPrincipals',
            'ListResources',
            'RejectResourceShareInvitation',
            'TagResource',
            'UntagResource',
            'UpdateResourceShare',
        ],
    },
    'AWS RoboMaker': {
        'StringPrefix': 'robomaker',
        'Actions': [
            'BatchDescribeSimulationJob',
            'CancelSimulationJob',
            'CreateDeploymentJob',
            'CreateFleet',
            'CreateRobot',
            'CreateRobotApplication',
            'CreateRobotApplicationVersion',
            'CreateSimulationApplication',
            'CreateSimulationApplicationVersion',
            'CreateSimulationJob',
            'DeleteRobot',
            'DeleteRobotApplication',
            'DeleteSimulationApplication',
            'DeregisterRobot',
            'DescribeDeploymentJob',
            'DescribeFleet',
            'DescribeRobot',
            'DescribeRobotApplication',
            'DescribeSimulationApplication',
            'DescribeSimulationJob',
            'ListDeploymentJobs',
            'ListFleets',
            'ListRobotApplications',
            'ListRobots',
            'ListSimulationApplications',
            'ListSimulationJobs',
            'RegisterRobot',
            'RestartSimulationJob',
            'SyncDeploymentJob',
            'UpdateRobotApplication',
            'UpdateSimulationApplication',
        ],
    },
    'Amazon Route 53 Resolver': {
        'StringPrefix': 'route53resolver',
        'Actions': [
            'AssociateResolverEndpointIpAddress',
            'AssociateResolverRule',
            'CreateResolverEndpoint',
            'CreateResolverRule',
            'DeleteResolverEndpoint',
            'DeleteResolverRule',
            'DisassociateResolverEndpointIpAddress',
            'DisassociateResolverRule',
            'GetResolverEndpoint',
            'GetResolverRule',
            'GetResolverRuleAssociation',
            'GetResolverRulePolicy',
            'ListResolverEndpointIpAddresses',
            'ListResolverEndpoints',
            'ListResolverRuleAssociations',
            'ListResolverRules',
            'ListTagsForResource',
            'PutResolverRulePolicy',
            'TagResource',
            'UntagResource',
            'UpdateResolverEndpoint',
            'UpdateResolverRule',
        ],
    },
    'AWS Security Hub': {
        'StringPrefix': 'securityhub',
        'Actions': [
            'AcceptInvitation',
            'BatchDisableStandards',
            'BatchEnableStandards',
            'BatchImportFindings',
            'CreateInsight',
            'CreateMembers',
            'DeclineInvitations',
            'DeleteInsight',
            'DeleteInvitations',
            'DeleteMembers',
            'DisableImportFindingsForProduct',
            'DisableSecurityHub',
            'DisassociateFromMasterAccount',
            'DisassociateMembers',
            'EnableImportFindingsForProduct',
            'EnableSecurityHub',
            'GetEnabledStandards',
            'GetFindings',
            'GetInsightResults',
            'GetInsights',
            'GetInvitationsCount',
            'GetMasterAccount',
            'GetMembers',
            'InviteMembers',
            'ListEnabledProductsForImport',
            'ListInvitations',
            'ListMembers',
            'UpdateFindings',
            'UpdateInsight',
        ],
    },
    'AWS Server Migration Service': {
        'StringPrefix': 'sms',
        'Actions': [
            'CreateApp',
            'CreateReplicationJob',
            'DeleteApp',
            'DeleteAppLaunchConfiguration',
            'DeleteAppReplicationConfiguration',
            'DeleteReplicationJob',
            'DeleteServerCatalog',
            'DisassociateConnectors',
            'GenerateChangeSet',
            'GenerateTemplate',
            'GetApp',
            'GetAppLaunchConfiguration',
            'GetAppReplicationConfiguration',
            'GetConnectors',
            'GetReplicationJobs',
            'GetReplicationRuns',
            'GetServers',
            'ImportServerCatalog',
            'LaunchApp',
            'ListApps',
            'PutAppLaunchConfiguration',
            'PutAppReplicationConfiguration',
            'StartAppReplication',
            'StartOnDemandReplicationRun',
            'StopAppReplication',
            'TerminateApp',
            'UpdateApp',
            'UpdateReplicationJob',
        ],
    },
    'Amazon Pinpoint SMS and Voice Service': {
        'StringPrefix': 'sms-voice',
        'Actions': [
            'CreateConfigurationSet',
            'CreateConfigurationSetEventDestination',
            'DeleteConfigurationSet',
            'DeleteConfigurationSetEventDestination',
            'GetConfigurationSetEventDestinations',
            'ListConfigurationSets',
            'SendVoiceMessage',
            'UpdateConfigurationSetEventDestination',
        ],
    },
    'AWS SSO Directory': {
        'StringPrefix': 'sso-directory',
        'Actions': [
            'AddMemberToGroup',
            'CreateAlias',
            'CreateGroup',
            'CreateUser',
            'DeleteGroup',
            'DeleteUser',
            'DescribeDirectory',
            'DescribeGroups',
            'DescribeUsers',
            'DisableUser',
            'EnableUser',
            'ListGroupsForUser',
            'ListMembersInGroup',
            'RemoveMemberFromGroup',
            'UpdateGroup',
            'UpdatePassword',
            'UpdateUser',
            'VerifyEmail',
        ],
    },
    'Amazon Sumerian': {
        'StringPrefix': 'sumerian',
        'Actions': [
            'Login',
            'ViewRelease',
        ],
    },
    'Amazon Textract': {
        'StringPrefix': 'textract',
        'Actions': [
            'AnalyzeDocument',
            'DetectDocumentText',
            'GetDocumentAnalysis',
            'GetDocumentTextDetection',
            'StartDocumentAnalysis',
            'StartDocumentTextDetection',
        ],
    },
    'AWS Transfer for SFTP': {
        'StringPrefix': 'transfer',
        'Actions': [
            'CreateServer',
            'CreateUser',
            'DeleteServer',
            'DeleteSshPublicKey',
            'DeleteUser',
            'DescribeServer',
            'DescribeUser',
            'ImportSshPublicKey',
            'ListServers',
            'ListTagsForResource',
            'ListUsers',
            'StartServer',
            'StopServer',
            'TagResource',
            'TestIdentityProvider',
            'UntagResource',
            'UpdateServer',
            'UpdateUser',
        ],
    },
    'AWS Well-Architected Tool': {
        'StringPrefix': 'wellarchitected',
        'Actions': [
            'CreateWorkload',
            'GetWorkload',
            'ListWorkloads',
        ],
    },
    'Amazon WorkLink': {
        'StringPrefix': 'worklink',
        'Actions': [
            'AssociateWebsiteCertificateAuthority',
            'CreateFleet',
            'DeleteFleet',
            'DescribeCompanyNetworkConfiguration',
            'DescribeDevice',
            'DescribeDevicePolicyConfiguration',
            'DescribeFleetMetadata',
            'DescribeIdentityProviderConfiguration',
            'DescribeWebsiteCertificateAuthority',
            'DisassociateWebsiteCertificateAuthority',
            'ListDevices',
            'ListFleets',
            'ListWebsiteCertificateAuthorities',
            'SignOutUser',
            'UpdateCompanyNetworkConfiguration',
            'UpdateDevicePolicyConfiguration',
            'UpdateFleetMetadata',
            'UpdateIdentityProviderConfiguration',
        ],
    },
    'SMM Messages': {
        'StringPrefix': 'ssmmessages',
        'Actions': [
            'CreateControlChannel',
            'CreateDataChannel',
            'OpenControlChannel',
            'OpenDataChannel',
        ],
    },
    'AWS Secrets Manager': {
        'ARNFormat': 'arn:aws:secretsmanager:'
                     '<region>:<account>'
                     ':secret:<resourceType>/<resourcePath>',
        'ARNRegex': '^arn:aws:secretsmanager:.+',
        'Actions': [
            'CancelRotateSecret', 'CreateSecret', 'DeleteResourcePolicy',
            'DeleteSecret', 'DescribeSecret', 'GetRandomPassword',
            'GetResourcePolicy', 'GetSecretValue', 'ListSecrets',
            'ListSecretVersionIds', 'PutResourcePolicy',
            'PutSecretValue', 'RestoreSecret', 'RotateSecret',
            'TagResource', 'UntagResource', 'UpdateSecret',
            'UpdateSecretVersionStage'
        ],
        'HasResource': '!0',
        'StringPrefix': 'secretsmanager',
        'conditionKeys': [
            'secretsmanager:Resource/AllowRotationLambdaArn',
            'secretsmanager:Description',
            'secretsmanager:ForceDeleteWithoutRecovery',
            'secretsmanager:KmsKeyId',
            'secretsmanager:Name',
            'secretsmanager:RecoveryWindowInDays',
            'secretsmanager:ResourceTag/<tagname>',
            'secretsmanager:RotationLambdaArn',
            'secretsmanager:SecretId',
            'secretsmanager:VersionId',
            'secretsmanager:VersionStage'
        ],
    },
    'QuickSight': {
        'StringPrefix': 'quicksight',
        'Actions': [
            'ListGroupMemberships', 'ListGroups', 'ListUserGroups',
            'ListUsers', 'DescribeGroup', 'DescribeUser', 'CreateAdmin',
            'CreateGroup', 'CreateGroupMembership', 'CreateReader',
            'CreateUser', 'DeleteGroup', 'DeleteGroupMembership',
            'DeleteUser', 'GetGroupMapping', 'RegisterUser',
            'SearchDirectoryGroups', 'SetGroupMapping', 'Subscribe',
            'Unsubscribe', 'UpdateGroup'
        ]
    }
}


extra_actions = {
    'cloudformation': [
        'DeleteChangeSet',
    ],
    'cloudwatch': [
        'DeleteDashboards', 'GetDashboard', 'ListDashboards', 'PutDashboard',
    ],
    'codecommit': [
        'CancelUploadArchive', 'GetUploadArchiveStatus', 'UploadArchive',
    ],
    'dynamodb': [
        'DescribeTimeToLive', 'UpdateTimeToLive',
    ],
    'es': [
        'ESHttpDelete', 'ESHttpGet', 'ESHttpHead', 'ESHttpPost', 'ESHttpPut',
    ],
    'firehose': [
        'ListTagsForDeliveryStream', 'StartDeliveryStreamEncryption',
        'StopDeliveryStreamEncryption', 'TagDeliveryStream',
        'UntagDeliveryStream',
    ],
    'iam': [
        'FinalizeSmsMfaRegistration', 'RequestSmsMfaRegistration',
    ],
    'kinesis': [
        'DeregisterStreamConsumer', 'DescribeStreamConsumer',
        'DescribeStreamSummary', 'ListShards', 'ListStreamConsumers',
        'RegisterStreamConsumer', 'SubscribeToShard',
    ],
    's3': [
        'ObjectOwnerOverrideToBucketOwner', 'ReplicateTags',
    ],
    'ssm': [
        'UpdateInstanceInformation',
    ],
}


# Some actions appear to be deleted but still in the docs. This grouping
# will keep them available as it gets sorted out.

deleted_actions = {
    'cloudsearch': [
        'DefineIndexFields',
    ],
    'cognito-idp': [
        'ListUserPools', 'ListUsers',
    ],
    'dax': [
        'DefineAttributeList', 'DefineAttributeListId', 'DefineKeySchema',
    ],
    'ec2': [
        'ModifySpotFleetRequest',
    ],
    'elasticbeanstalk': [
        'AddTags', 'ListTagsForResource', 'RemoveTags',
    ],
    'glue': [
        'GetDataCatalogEncryptionSettings', 'PutDataCatalogEncryptionSettings',
        'CreateSecurityConfiguration', 'GetSecurityConfiguration',
        'GetSecurityConfigurations', 'DeleteSecurityConfiguration',
    ],
    'kinesis': [
        'StartStreamEncryption', 'StopStreamEncryption',
    ],
    'kinesisanalytics': [
        'GetApplicationState',
    ],
    'kms': [
        'ReEncrypt',
    ],
    'mechanicalturk': [
        'AcceptQualificationRequest', 'AssociateQualificationWithWorker',
        'CreateHITType', 'CreateHITWithHITType', 'CreateWorkerBlock',
        'DeleteHIT', 'DeleteQualificationType', 'DeleteWorkerBlock',
        'DisassociateQualificationFromWorker', 'ListAssignmentsForHIT',
        'ListBonusPayments', 'ListHITs', 'ListHITsForQualificationType',
        'ListQualificationRequests', 'ListQualificationTypes',
        'ListReviewPolicyResultsForHIT', 'ListReviewableHITs',
        'ListWorkerBlocks', 'ListWorkersWithQualificationType',
        'SendBonus', 'UpdateExpirationForHIT', 'UpdateHITReviewStatus',
        'UpdateHITTypeOfHIT', 'UpdateNotificationSettings',

    ],
    'mobilehub': [
        'ValidateProject',
    ],
    'mobiletargeting': [
        'DeleteAdmChannel', 'DeleteAdmChannel', 'DeleteApnsSandboxChannel',
        'GetAdmChannel', 'GetApnsSandboxChannel', 'UpdateAdmChannel',
        'UpdateApnsSandboxChannel',
    ],
    'route53': [
        'CreateVPCAssociationAuthorization',
        'DeleteVPCAssociationAuthorization',
        'ListVPCAssociationAuthorizations',
    ],
    'route53domain': [
        'DeleteDomain',
    ],
    'tag': [
        'AddResourceTags', 'RemoveResourceTags',
    ],
}

# patch in the extra_services if they are not present in policies.js
for service_name in extra_services:
    if not d['serviceMap'].get(service_name):
        d['serviceMap'][service_name] = extra_services[service_name]


filename_seen = {}
for serviceName, serviceValue in d['serviceMap'].items():
    prefix = serviceValue['StringPrefix']
    service = prefix
    # Handle prefix such as "directconnect:"
    if prefix[-1] == ':':
        service = prefix[:-1]
    if service == 'lambda':
        service = 'awslambda'
    service = service.replace("-", "_")
    filename = ''.join([basedir, "/", service, ".py"])
    with open(filename, "a") as fp:
        if filename not in filename_seen:
            filename_seen[filename] = True
            if prefix in legacy_arns:
                fp.write("import warnings\n")
            fp.write(header)
            fp.write("\n")
            fp.write("service_name = '%s'\n" % (serviceName,))
            fp.write("prefix = '%s'\n" % (prefix,))
            fp.write("\n\n")
            if service == "s3":
                fp.write(extra_classes_s3)
            else:
                fp.write(extra_classes)
            fp.write("\n\n")
            if prefix in legacy_arns:
                fp.write(arn % {
                    'lower': prefix,
                    'upper': prefix.upper(),
                })
                fp.write("\n\n")

        # Add actions AWS hasn't added yet
        if service in extra_actions:
            serviceValue['Actions'].extend(extra_actions[service])

        # Add actions AWS may have inadvertantly deleted
        if service in deleted_actions:
            serviceValue['Actions'].extend(deleted_actions[service])

        # Make the set sorted and unique
        serviceValue['Actions'] = sorted(set(serviceValue['Actions']))

        for action in serviceValue['Actions']:
            action = action.strip()
            # Handle action such as "ReEncrypt*"
            if action[-1] == '*':
                action = action[:-1]
            # Wrap lines for pep8
            if len(action) > 30:
                format = "%s = \\\n    Action('%s')\n"
            else:
                format = "%s = Action('%s')\n"
            fp.write(format % (action, action))
