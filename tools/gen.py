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
    'acm': [
        'ExportCertificate',
        'UpdateCertificateOptions',
    ],
    'apigateway': [
        'UpdateRestApiPolicy',
    ],
    'appstream': [
        'BatchAssociateUserStack',
        'BatchDisassociateUserStack',
        'CopyImage',
        'CreateUser',
        'DeleteImagePermissions',
        'DeleteUser',
        'DescribeImagePermissions',
        'DescribeUserStackAssociations',
        'DescribeUsers',
        'DisableUser',
        'EnableUser',
        'UpdateImagePermissions',
    ],
    'appsync': [
        'CreateFunction',
        'DeleteFunction',
        'GetFunction',
        'ListFunctions',
        'UpdateFunction',
    ],
    'athena': [
        'CreateWorkGroup',
        'DeleteWorkGroup',
        'GetQueryResultsStream',
        'GetWorkGroup',
        'ListTagsForResource',
        'ListWorkGroups',
        'TagResource',
        'UntagResource',
        'UpdateWorkGroup',
    ],
    'autoscaling': [
        'BatchDeleteScheduledAction',
        'BatchPutScheduledUpdateGroupAction',
    ],
    'autoscaling_plans': [
        'GetScalingPlanResourceForecastData',
        'UpdateScalingPlan',
    ],
    'aws_marketplace': [
        'RegisterUsage',
    ],
    'aws_marketplace_management': [
        'viewSettings',
    ],
    'awslambda': [
        'AddLayerVersionPermission',
        'DeleteLayerVersion',
        'GetLayerVersion',
        'GetLayerVersionPolicy',
        'ListLayerVersions',
        'ListLayers',
        'PublishLayerVersion',
        'RemoveLayerVersionPermission',
    ],
    'chime': [
        'BatchSuspendUser',
        'BatchUnsuspendUser',
        'BatchUpdateUser',
        'CreateApiKey',
        'DeleteAccountOpenIdConfig',
        'DeleteApiKey',
        'GetAccountWithOpenIdConfig',
        'GetMeetingDetail',
        'GetUserActivityReportData',
        'ListAccountUsageReportData',
        'ListApiKeys',
        'ListMeetingEvents',
        'ListMeetingsReportData',
        'RetrieveDataExports',
        'StartDataExport',
        'UpdateAccount',
        'UpdateAccountOpenIdConfig',
        'UpdateCDRSettings',
        'UpdateUser',
    ],
    'clouddirectory': [
        'GetLinkAttributes',
        'GetObjectAttributes',
        'UpdateLinkAttributes',
    ],
    'cloudformation': [
        'CreateStackInstances',
        'CreateStackSet',
        'DeleteChangeSet',
        'DeleteStackInstances',
        'DeleteStackSet',
        'DescribeStackDriftDetectionStatus',
        'DescribeStackInstance',
        'DescribeStackResourceDrifts',
        'DescribeStackSet',
        'DescribeStackSetOperation',
        'DetectStackDrift',
        'DetectStackResourceDrift',
        'ListStackInstances',
        'ListStackSetOperationResults',
        'ListStackSetOperations',
        'ListStackSets',
        'StopStackSetOperation',
        'UpdateStackInstances',
        'UpdateStackSet',
    ],
    'cloudhsm': [
        'CreateCluster',
        'DeleteCluster',
        'DescribeBackups',
        'DescribeClusters',
        'InitializeCluster',
        'ListTags',
        'TagResource',
        'UntagResource',
    ],
    'cloudwatch': [
        'DeleteDashboards',
        'GetDashboard',
        'GetMetricWidgetImage',
        'ListDashboards',
        'PutDashboard',
    ],
    'codebuild': [
        'CreateWebhook',
        'DeleteSourceCredentials',
        'DeleteWebhook',
        'ImportSourceCredentials',
        'InvalidateProjectCache',
        'ListSourceCredentials',
        'UpdateWebhook',
    ],
    'codecommit': [
        'CancelUploadArchive',
        'DeleteFile',
        'GetFile',
        'GetFolder',
        'GetUploadArchiveStatus',
        'UploadArchive',
    ],
    'codedeploy': [
        'PutLifecycleEventHookExecutionStatus',
    ],
    'codepipeline': [
        'DeleteWebhook',
        'DeregisterWebhookWithThirdParty',
        'ListWebhooks',
        'PutWebhook',
        'RegisterWebhookWithThirdParty',
    ],
    'cognito_idp': [
        'AdminDisableProviderForUser',
        'AdminLinkProviderForUser',
        'AssociateSoftwareToken',
        'CreateIdentityProvider',
        'CreateResourceServer',
        'CreateUserPoolDomain',
        'DeleteIdentityProvider',
        'DeleteResourceServer',
        'DeleteUserPoolDomain',
        'DescribeIdentityProvider',
        'DescribeResourceServer',
        'DescribeUserPoolDomain',
        'GetIdentityProviderByIdentifier',
        'GetSigningCertificate',
        'GetUICustomization',
        'ListIdentityProviders',
        'ListResourceServers',
        'ListUserPools',
        'ListUsers',
        'SetUICustomization',
        'UpdateIdentityProvider',
        'UpdateResourceServer',
        'VerifySoftwareToken',
    ],
    'comprehend': [
        'BatchDetectSyntax',
        'CreateDocumentClassifier',
        'CreateEntityRecognizer',
        'DeleteDocumentClassifier',
        'DeleteEntityRecognizer',
        'DescribeDocumentClassificationJob',
        'DescribeDocumentClassifier',
        'DescribeDominantLanguageDetectionJob',
        'DescribeEntitiesDetectionJob',
        'DescribeEntityRecognizer',
        'DescribeKeyPhrasesDetectionJob',
        'DescribeSentimentDetectionJob',
        'DetectSyntax',
        'ListDocumentClassificationJobs',
        'ListDocumentClassifiers',
        'ListDominantLanguageDetectionJobs',
        'ListEntitiesDetectionJobs',
        'ListEntityRecognizers',
        'ListKeyPhrasesDetectionJobs',
        'ListSentimentDetectionJobs',
        'StartDocumentClassificationJob',
        'StartDominantLanguageDetectionJob',
        'StartEntitiesDetectionJob',
        'StartKeyPhrasesDetectionJob',
        'StartSentimentDetectionJob',
        'StopDominantLanguageDetectionJob',
        'StopEntitiesDetectionJob',
        'StopKeyPhrasesDetectionJob',
        'StopSentimentDetectionJob',
        'StopTrainingDocumentClassifier',
        'StopTrainingEntityRecognizer',
    ],
    'config': [
        'BatchGetAggregateResourceConfig',
        'BatchGetResourceConfig',
        'DeleteAggregationAuthorization',
        'DeleteConfigurationAggregator',
        'DeletePendingAggregationRequest',
        'DeleteRetentionConfiguration',
        'DescribeAggregateComplianceByConfigRules',
        'DescribeAggregationAuthorizations',
        'DescribeConfigurationAggregatorSourcesStatus',
        'DescribeConfigurationAggregators',
        'DescribePendingAggregationRequests',
        'DescribeRetentionConfigurations',
        'GetAggregateComplianceDetailsByConfigRule',
        'GetAggregateConfigRuleComplianceSummary',
        'GetAggregateDiscoveredResourceCounts',
        'GetAggregateResourceConfig',
        'GetDiscoveredResourceCounts',
        'ListAggregateDiscoveredResources',
        'PutAggregationAuthorization',
        'PutConfigurationAggregator',
        'PutRetentionConfiguration',
    ],
    'connect': [
        'GetCurrentMetricData',
        'GetMetricData',
        'StartOutboundVoiceContact',
        'StopContact',
    ],
    'crowd': [
        'ApproveAssignment',
        'ApproveRejectedAssignment',
        'AssignQualification',
        'BlockWorker',
        'ChangeHITTypeOfHIT',
        'CreateHIT',
        'CreateQualificationType',
        'DisableHIT',
        'DisposeHIT',
        'DisposeQualificationType',
        'ExtendHIT',
        'ForceExpireHIT',
        'GetAccountBalance',
        'GetAssignment',
        'GetAssignmentsForHIT',
        'GetBlockedWorkers',
        'GetBonusPayments',
        'GetFileUploadURL',
        'GetHIT',
        'GetHITsForQualificationType',
        'GetQualificationRequests',
        'GetQualificationScore',
        'GetQualificationType',
        'GetQualificationsForQualificationType',
        'GetRequesterStatistic',
        'GetRequesterWorkerStatistic',
        'GetReviewResultsForHIT',
        'GetReviewableHITs',
        'GrantBonus',
        'GrantQualification',
        'NotifyWorkers',
        'RegisterHITType',
        'RejectAssignment',
        'RejectQualificationRequest',
        'RevokeQualification',
        'SearchHITs',
        'SearchQualificationTypes',
        'SendTestEventNotification',
        'SetHITAsReviewing',
        'SetHITTypeNotification',
        'UnblockWorker',
        'UpdateQualificationScore',
        'UpdateQualificationType',
    ],
    'dax': [
        'ConditionCheckItem',
    ],
    'ds': [
        'AcceptSharedDirectory',
        'CreateLogSubscription',
        'DeleteLogSubscription',
        'DescribeDomainControllers',
        'DescribeSharedDirectories',
        'ListLogSubscriptions',
        'RejectSharedDirectory',
        'ResetUserPassword',
        'ShareDirectory',
        'UnshareDirectory',
        'UpdateNumberOfDomainControllers',
    ],
    'dynamodb': [
        'ConditionCheckItem',
        'CreateGlobalTable',
        'DescribeGlobalTable',
        'DescribeGlobalTableSettings',
        'DescribeTimeToLive',
        'ListGlobalTables',
        'UpdateGlobalTable',
        'UpdateGlobalTableSettings',
        'UpdateTimeToLive',
    ],
    'ec2': [
        'AcceptTransitGatewayVpcAttachment',
        'AdvertiseByoipCidr',
        'AssociateTransitGatewayRouteTable',
        'CancelCapacityReservation',
        'CreateCapacityReservation',
        'CreateFleet',
        'CreateTransitGateway',
        'CreateTransitGatewayRoute',
        'CreateTransitGatewayRouteTable',
        'CreateTransitGatewayVpcAttachment',
        'DeleteFleets',
        'DeleteTransitGateway',
        'DeleteTransitGatewayRoute',
        'DeleteTransitGatewayRouteTable',
        'DeleteTransitGatewayVpcAttachment',
        'DeprovisionByoipCidr',
        'DescribeAggregateIdFormat',
        'DescribeByoipCidrs',
        'DescribeCapacityReservations',
        'DescribeFleetHistory',
        'DescribeFleetInstances',
        'DescribeFleets',
        'DescribePrincipalIdFormat',
        'DescribePublicIpv4Pools',
        'DescribeTransitGatewayAttachments',
        'DescribeTransitGatewayRouteTables',
        'DescribeTransitGatewayVpcAttachments',
        'DescribeTransitGateways',
        'DisableTransitGatewayRouteTablePropagation',
        'DisassociateTransitGatewayRouteTable',
        'EnableTransitGatewayRouteTablePropagation',
        'ExportTransitGatewayRoutes',
        'GetTransitGatewayAttachmentPropagations',
        'GetTransitGatewayRouteTableAssociations',
        'GetTransitGatewayRouteTablePropagations',
        'ModifyCapacityReservation',
        'ModifyFleet',
        'ModifyInstanceCapacityReservationAttributes',
        'ModifyTransitGatewayVpcAttachment',
        'ProvisionByoipCidr',
        'RejectTransitGatewayVpcAttachment',
        'ReplaceTransitGatewayRoute',
        'SearchTransitGatewayRoutes',
        'WithdrawByoipCidr',
    ],
    'ecr': [
        'DeleteLifecyclePolicy',
        'GetLifecyclePolicy',
        'GetLifecyclePolicyPreview',
        'ListTagsForResource',
        'PutLifecyclePolicy',
        'StartLifecyclePolicyPreview',
        'TagResource',
        'UntagResource',
    ],
    'ecs': [
        'DeleteAccountSettings',
        'DeleteAttributes',
        'ListAccountSettings',
        'ListAttributes',
        'ListTagsForResource',
        'PutAccountSetting',
        'PutAccountSettingDefault',
        'PutAttributes',
        'TagResource',
        'UntagResource',
    ],
    'elasticache': [
        'DecreaseReplicaCount',
        'IncreaseReplicaCount',
        'ModifyReplicationGroupShardConfiguration',
        'TestFailover',
    ],
    'elasticbeanstalk': [
        'DescribeAccountAttributes',
    ],
    'elasticfilesystem': [
        'DescribeLifecycleConfiguration',
        'PutLifecycleConfiguration',
        'UpdateFileSystem',
    ],
    'elasticmapreduce': [
        'AddInstanceFleet',
        'CreateEditor',
        'DeleteEditor',
        'DescribeEditor',
        'ListEditors',
        'ListInstanceFleets',
        'ModifyInstanceFleet',
        'OpenEditorInConsole',
        'StartEditor',
        'StopEditor',
    ],
    'es': [
        'DeleteElasticsearchServiceRole',
        'DescribeElasticsearchInstanceTypeLimits',
        'DescribeReservedElasticsearchInstanceOfferings',
        'DescribeReservedElasticsearchInstances',
        'ESHttpDelete',
        'ESHttpGet',
        'ESHttpHead',
        'ESHttpPost',
        'ESHttpPut',
        'GetCompatibleElasticsearchVersions',
        'GetUpgradeHistory',
        'GetUpgradeStatus',
        'ListElasticsearchInstanceTypes',
        'ListElasticsearchVersions',
        'PurchaseReservedElasticsearchInstance',
        'UpgradeElasticsearchDomain',

    ],
    'events': [
        'DescribeEventBus',
        'PutPermission',
        'RemovePermission',
    ],
    'firehose': [
        'ListTagsForDeliveryStream', 'StartDeliveryStreamEncryption',
        'StopDeliveryStreamEncryption', 'TagDeliveryStream',
        'UntagDeliveryStream',
    ],
    'glue': [
        'DeleteResourcePolicy',
        'GetResourcePolicy',
        'PutResourcePolicy',
    ],
    'iam': [
        'DeleteRolePermissionsBoundary',
        'DeleteUserPermissionsBoundary',
        'FinalizeSmsMfaRegistration',
        'ListRoleTags',
        'ListUserTags',
        'PutRolePermissionsBoundary',
        'PutUserPermissionsBoundary',
        'RequestSmsMfaRegistration',
        'TagRole',
        'TagUser',
        'UntagRole',
        'UntagUser',
        'UpdateRole',
    ],
    'iot': [
        'AddThingToBillingGroup',
        'AddThingToThingGroup',
        'CancelJobExecution',
        'CreateBillingGroup',
        'CreateOTAUpdate',
        'CreateThingGroup',
        'DeleteBillingGroup',
        'DeleteJob',
        'DeleteJobExecution',
        'DeleteOTAUpdate',
        'DeleteThingGroup',
        'DeleteV2LoggingLevel',
        'DescribeBillingGroup',
        'DescribeEventConfigurations',
        'DescribeThingGroup',
        'DescribeThingRegistrationTask',
        'GetOTAUpdate',
        'GetPendingJobExecutions',
        'GetV2LoggingOptions',
        'ListBillingGroups',
        'ListOTAUpdates',
        'ListTagsForResource',
        'ListThingGroups',
        'ListThingGroupsForThing',
        'ListThingRegistrationTaskReports',
        'ListThingRegistrationTasks',
        'ListThingsInBillingGroup',
        'ListThingsInThingGroup',
        'ListV2LoggingLevels',
        'RegisterThing',
        'RemoveThingFromBillingGroup',
        'RemoveThingFromThingGroup',
        'SetV2LoggingLevel',
        'SetV2LoggingOptions',
        'StartNextPendingJobExecution',
        'StartThingRegistrationTask',
        'StopThingRegistrationTask',
        'TagResource',
        'UntagResource',
        'UpdateBillingGroup',
        'UpdateEventConfigurations',
        'UpdateJob',
        'UpdateJobExecution',
        'UpdateThingGroup',
        'UpdateThingGroupsForThing',
    ],
    'iotanalytics': [
        'BatchPutMessage',
        'CancelPipelineReprocessing',
        'DescribeLoggingOptions',
        'ListTagsForResource',
        'PutLoggingOptions',
        'RunPipelineActivity',
        'SampleChannelData',
        'StartPipelineReprocessing',
        'TagResource',
        'UntagResource',
        'UpdateChannel',
        'UpdateDatastore',
    ],
    'kinesis': [
        'DeregisterStreamConsumer', 'DescribeStreamConsumer',
        'DescribeStreamSummary', 'ListShards', 'ListStreamConsumers',
        'RegisterStreamConsumer', 'SubscribeToShard',
    ],
    'kinesisvideo': [
        'GetHLSStreamingSessionURL',
    ],
    'logs': [
        'CreateLogDelivery',
        'DeleteLogDelivery',
        'DescribeQueries',
        'GetLogDelivery',
        'GetLogGroupFields',
        'GetLogRecord',
        'GetQueryResults',
        'ListLogDeliveries',
        'StartQuery',
        'StopQuery',
        'UpdateLogDelivery',
    ],
    'mediaconvert': [
        'DescribeEndpoints',
    ],
    'medialive': [
        'BatchUpdateSchedule',
        'DeleteReservation',
        'DescribeOffering',
        'DescribeReservation',
        'DescribeSchedule',
        'ListOfferings',
        'ListReservations',
        'PurchaseOffering',
        'UpdateChannel',
        'UpdateInput',
        'UpdateInputSecurityGroup',
    ],
    'mediastore': [
        'DeleteCorsPolicy',
        'DeleteLifecyclePolicy',
        'GetCorsPolicy',
        'GetLifecyclePolicy',
        'PutCorsPolicy',
        'PutLifecyclePolicy',
        'StartAccessLogging',
        'StopAccessLogging',
    ],
    'mobilehub': [
        'DeleteProjectSnapshot',
        'InstallBundle',
        'ListProjectSnapshots',
    ],
    'mobiletargeting': [
        'CreateApp',
        'CreateExportJob',
        'DeleteApnsVoipChannel',
        'DeleteApnsVoipSandboxChannel',
        'DeleteApp',
        'DeleteBaiduChannel',
        'DeleteEmailChannel',
        'DeleteEndpoint',
        'DeleteEventStream',
        'DeleteSmsChannel',
        'DeleteUserEndpoints',
        'DeleteVoiceChannel',
        'GetApnsVoipChannel',
        'GetApnsVoipSandboxChannel',
        'GetApp',
        'GetApps',
        'GetBaiduChannel',
        'GetChannels',
        'GetEmailChannel',
        'GetEventStream',
        'GetExportJob',
        'GetExportJobs',
        'GetSegmentExportJobs',
        'GetSmsChannel',
        'GetUserEndpoints',
        'GetVoiceChannel',
        'ListTagsForResource',
        'PhoneNumberValidate',
        'PutEventStream',
        'PutEvents',
        'SendMessages',
        'SendUsersMessages',
        'TagResource',
        'UntagResource',
        'UpdateApnsVoipChannel',
        'UpdateApnsVoipSandboxChannel',
        'UpdateBaiduChannel',
        'UpdateEmailChannel',
        'UpdateSmsChannel',
        'UpdateVoiceChannel',
    ],
    'mq': [
        'CreateTags',
        'DeleteTags',
        'ListTags',
    ],
    'organizations': [
        'DisableAWSServiceAccess',
        'EnableAWSServiceAccess',
        'ListAWSServiceAccessForOrganization',
    ],
    'polly': [
        'GetSpeechSynthesisTask',
        'ListSpeechSynthesisTasks',
        'StartSpeechSynthesisTask',
    ],
    'rds': [
        'DescribeValidDBInstanceModifications',
        'ModifyCurrentDBClusterCapacity',
        'StartDBCluster',
        'StopDBCluster',
    ],
    'route53': [
        'CreateQueryLoggingConfig',
        'DeleteQueryLoggingConfig',
        'GetAccountLimit',
        'GetHostedZoneLimit',
        'GetQueryLoggingConfig',
        'GetReusableDelegationSetLimit',
        'ListQueryLoggingConfigs',
    ],
    's3': [
        'GetAccountPublicAccessBlock',
        'GetBucketPolicyStatus',
        'GetBucketPublicAccessBlock',
        'GetEncryptionConfiguration',
        'ObjectOwnerOverrideToBucketOwner',
        'PutAccountPublicAccessBlock',
        'PutBucketPublicAccessBlock',
        'PutEncryptionConfiguration',
        'ReplicateTags',
    ],
    'sagemaker': [
        'CreateAlgorithm',
        'CreateCodeRepository',
        'CreateCompilationJob',
        'CreateHyperParameterTuningJob',
        'CreateLabelingJob',
        'CreateModelPackage',
        'CreateNotebookInstanceLifecycleConfig',
        'CreateTransformJob',
        'CreateWorkteam',
        'DeleteAlgorithm',
        'DeleteCodeRepository',
        'DeleteModelPackage',
        'DeleteNotebookInstanceLifecycleConfig',
        'DeleteWorkteam',
        'DescribeAlgorithm',
        'DescribeCodeRepository',
        'DescribeCompilationJob',
        'DescribeHyperParameterTuningJob',
        'DescribeLabelingJob',
        'DescribeModelPackage',
        'DescribeNotebookInstanceLifecycleConfig',
        'DescribeSubscribedWorkteam',
        'DescribeTransformJob',
        'DescribeWorkteam',
        'GetSearchSuggestions',
        'ListAlgorithms',
        'ListCodeRepositories',
        'ListCompilationJobs',
        'ListHyperParameterTuningJobs',
        'ListLabelingJobs',
        'ListLabelingJobsForWorkteam',
        'ListModelPackages',
        'ListNotebookInstanceLifecycleConfigs',
        'ListSubscribedWorkteams',
        'ListTrainingJobsForHyperParameterTuningJob',
        'ListTransformJobs',
        'ListWorkteams',
        'RenderUiTemplate',
        'Search',
        'StopCompilationJob',
        'StopHyperParameterTuningJob',
        'StopLabelingJob',
        'StopTransformJob',
        'UpdateCodeRepository',
        'UpdateNotebookInstanceLifecycleConfig',
        'UpdateWorkteam',
    ],
    'serverlessrepo': [
        'CreateCloudFormationTemplate',
        'GetCloudFormationTemplate',
        'ListApplicationDependencies',
    ],
    'servicecatalog': [
        'CreateProvisionedProductPlan',
        'DeleteProvisionedProductPlan',
        'DescribeProvisionedProduct',
        'DescribeProvisionedProductPlan',
        'ExecuteProvisionedProductPlan',
        'ExecuteProvisionedProductServiceAction',
        'ListProvisionedProductPlans',
        'ListServiceActionsForProvisioningArtifact',
        'SearchProvisionedProducts',
    ],
    'servicediscovery': [
        'CreateHttpNamespace',
        'DiscoverInstances',
    ],
    'shield': [
        'AssociateDRTLogBucket',
        'AssociateDRTRole',
        'DescribeDRTAccess',
        'DescribeEmergencyContactSettings',
        'DisassociateDRTLogBucket',
        'DisassociateDRTRole',
        'GetSubscriptionState',
        'UpdateEmergencyContactSettings',
    ],
    'signer': [
        'CancelSigningProfile',
        'GetSigningPlatform',
        'GetSigningProfile',
        'ListSigningPlatforms',
        'ListSigningProfiles',
        'PutSigningProfile',
    ],
    'ssm': [
        'DescribeAssociationExecutions',
        'DescribeAssociationExecutionTargets',
        'DescribeSessions',
        'GetConnectionStatus',
        'ListComplianceItems',
        'ListComplianceSummaries',
        'ListResourceComplianceSummaries',
        'ResumeSession',
        'StartSession',
        'TerminateSession',
        'UpdateInstanceInformation',
    ],
    'sso': [
        'AddMemberToGroup',
        'CreateAlias',
        'CreateGroup',
        'CreateUser',
        'DeleteGroup',
        'DeleteUser',
        'DescribeGroups',
        'DescribeUsers',
        'DisableUser',
        'EnableUser',
        'GetPermissionsPolicy',
        'GetSSOConfiguration',
        'GetUserPoolInfo',
        'ListApplications',
        'ListGroupsForUser',
        'ListMembersInGroup',
        'RemoveMemberFromGroup',
        'SearchGroups',
        'SearchUsers',
        'SetTemporaryPassword',
        'UpdateGroup',
        'UpdateSSOConfiguration',
        'UpdateUser',
    ],
    'storagegateway': [
        'CreateSMBFileShare',
        'DescribeSMBFileShares',
        'DescribeSMBSettings',
        'JoinDomain',
        'NotifyWhenUploaded',
        'SetSMBGuestPassword',
        'UpdateSMBFileShare',
    ],
    'translate': [
        'DeleteTerminology',
        'GetTerminology',
        'ImportTerminology',
        'ListTerminologies',
    ],
    'waf': [
        'CreateRuleGroup',
        'DeletePermissionPolicy',
        'DeleteRuleGroup',
        'GetPermissionPolicy',
        'GetRuleGroup',
        'ListActivatedRulesInRuleGroup',
        'ListRuleGroups',
        'ListSubscribedRuleGroups',
        'PutPermissionPolicy',
        'UpdateRuleGroup',
    ],
    'waf_regional': [
        'CreateRuleGroup',
        'DeletePermissionPolicy',
        'DeleteRuleGroup',
        'GetPermissionPolicy',
        'GetRuleGroup',
        'ListActivatedRulesInRuleGroup',
        'ListRuleGroups',
        'ListSubscribedRuleGroups',
        'PutPermissionPolicy',
        'UpdateRuleGroup',
    ],
    'xray': [
        'CreateGroup',
        'CreateSamplingRule',
        'DeleteGroup',
        'DeleteSamplingRule',
        'GetEncryptionConfig',
        'GetGroup',
        'GetGroups',
        'GetSamplingRules',
        'GetSamplingStatisticSummaries',
        'GetSamplingTargets',
        'PutEncryptionConfig',
        'UpdateGroup',
        'UpdateSamplingRule',
    ]
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
