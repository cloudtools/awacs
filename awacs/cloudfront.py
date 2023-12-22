# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudFront"
prefix = "cloudfront"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAlias = Action("AssociateAlias")
CopyDistribution = Action("CopyDistribution")
CreateCachePolicy = Action("CreateCachePolicy")
CreateCloudFrontOriginAccessIdentity = Action("CreateCloudFrontOriginAccessIdentity")
CreateContinuousDeploymentPolicy = Action("CreateContinuousDeploymentPolicy")
CreateDistribution = Action("CreateDistribution")
CreateDistributionWithTags = Action("CreateDistributionWithTags")
CreateFieldLevelEncryptionConfig = Action("CreateFieldLevelEncryptionConfig")
CreateFieldLevelEncryptionProfile = Action("CreateFieldLevelEncryptionProfile")
CreateFunction = Action("CreateFunction")
CreateInvalidation = Action("CreateInvalidation")
CreateKeyGroup = Action("CreateKeyGroup")
CreateKeyValueStore = Action("CreateKeyValueStore")
CreateMonitoringSubscription = Action("CreateMonitoringSubscription")
CreateOriginAccessControl = Action("CreateOriginAccessControl")
CreateOriginRequestPolicy = Action("CreateOriginRequestPolicy")
CreatePublicKey = Action("CreatePublicKey")
CreateRealtimeLogConfig = Action("CreateRealtimeLogConfig")
CreateResponseHeadersPolicy = Action("CreateResponseHeadersPolicy")
CreateSavingsPlan = Action("CreateSavingsPlan")
CreateStreamingDistribution = Action("CreateStreamingDistribution")
CreateStreamingDistributionWithTags = Action("CreateStreamingDistributionWithTags")
DeleteCachePolicy = Action("DeleteCachePolicy")
DeleteCloudFrontOriginAccessIdentity = Action("DeleteCloudFrontOriginAccessIdentity")
DeleteContinuousDeploymentPolicy = Action("DeleteContinuousDeploymentPolicy")
DeleteDistribution = Action("DeleteDistribution")
DeleteFieldLevelEncryptionConfig = Action("DeleteFieldLevelEncryptionConfig")
DeleteFieldLevelEncryptionProfile = Action("DeleteFieldLevelEncryptionProfile")
DeleteFunction = Action("DeleteFunction")
DeleteKeyGroup = Action("DeleteKeyGroup")
DeleteKeyValueStore = Action("DeleteKeyValueStore")
DeleteMonitoringSubscription = Action("DeleteMonitoringSubscription")
DeleteOriginAccessControl = Action("DeleteOriginAccessControl")
DeleteOriginRequestPolicy = Action("DeleteOriginRequestPolicy")
DeletePublicKey = Action("DeletePublicKey")
DeleteRealtimeLogConfig = Action("DeleteRealtimeLogConfig")
DeleteResponseHeadersPolicy = Action("DeleteResponseHeadersPolicy")
DeleteStreamingDistribution = Action("DeleteStreamingDistribution")
DescribeFunction = Action("DescribeFunction")
DescribeKeyValueStore = Action("DescribeKeyValueStore")
GetCachePolicy = Action("GetCachePolicy")
GetCachePolicyConfig = Action("GetCachePolicyConfig")
GetCloudFrontOriginAccessIdentity = Action("GetCloudFrontOriginAccessIdentity")
GetCloudFrontOriginAccessIdentityConfig = Action(
    "GetCloudFrontOriginAccessIdentityConfig"
)
GetContinuousDeploymentPolicy = Action("GetContinuousDeploymentPolicy")
GetContinuousDeploymentPolicyConfig = Action("GetContinuousDeploymentPolicyConfig")
GetDistribution = Action("GetDistribution")
GetDistributionConfig = Action("GetDistributionConfig")
GetFieldLevelEncryption = Action("GetFieldLevelEncryption")
GetFieldLevelEncryptionConfig = Action("GetFieldLevelEncryptionConfig")
GetFieldLevelEncryptionProfile = Action("GetFieldLevelEncryptionProfile")
GetFieldLevelEncryptionProfileConfig = Action("GetFieldLevelEncryptionProfileConfig")
GetFunction = Action("GetFunction")
GetInvalidation = Action("GetInvalidation")
GetKeyGroup = Action("GetKeyGroup")
GetKeyGroupConfig = Action("GetKeyGroupConfig")
GetMonitoringSubscription = Action("GetMonitoringSubscription")
GetOriginAccessControl = Action("GetOriginAccessControl")
GetOriginAccessControlConfig = Action("GetOriginAccessControlConfig")
GetOriginRequestPolicy = Action("GetOriginRequestPolicy")
GetOriginRequestPolicyConfig = Action("GetOriginRequestPolicyConfig")
GetPublicKey = Action("GetPublicKey")
GetPublicKeyConfig = Action("GetPublicKeyConfig")
GetRealtimeLogConfig = Action("GetRealtimeLogConfig")
GetResponseHeadersPolicy = Action("GetResponseHeadersPolicy")
GetResponseHeadersPolicyConfig = Action("GetResponseHeadersPolicyConfig")
GetSavingsPlan = Action("GetSavingsPlan")
GetStreamingDistribution = Action("GetStreamingDistribution")
GetStreamingDistributionConfig = Action("GetStreamingDistributionConfig")
ListCachePolicies = Action("ListCachePolicies")
ListCloudFrontOriginAccessIdentities = Action("ListCloudFrontOriginAccessIdentities")
ListConflictingAliases = Action("ListConflictingAliases")
ListContinuousDeploymentPolicies = Action("ListContinuousDeploymentPolicies")
ListDistributions = Action("ListDistributions")
ListDistributionsByCachePolicyId = Action("ListDistributionsByCachePolicyId")
ListDistributionsByKeyGroup = Action("ListDistributionsByKeyGroup")
ListDistributionsByLambdaFunction = Action("ListDistributionsByLambdaFunction")
ListDistributionsByOriginRequestPolicyId = Action(
    "ListDistributionsByOriginRequestPolicyId"
)
ListDistributionsByRealtimeLogConfig = Action("ListDistributionsByRealtimeLogConfig")
ListDistributionsByResponseHeadersPolicyId = Action(
    "ListDistributionsByResponseHeadersPolicyId"
)
ListDistributionsByWebACLId = Action("ListDistributionsByWebACLId")
ListFieldLevelEncryptionConfigs = Action("ListFieldLevelEncryptionConfigs")
ListFieldLevelEncryptionProfiles = Action("ListFieldLevelEncryptionProfiles")
ListFunctions = Action("ListFunctions")
ListInvalidations = Action("ListInvalidations")
ListKeyGroups = Action("ListKeyGroups")
ListKeyValueStores = Action("ListKeyValueStores")
ListOriginAccessControls = Action("ListOriginAccessControls")
ListOriginRequestPolicies = Action("ListOriginRequestPolicies")
ListPublicKeys = Action("ListPublicKeys")
ListRateCards = Action("ListRateCards")
ListRealtimeLogConfigs = Action("ListRealtimeLogConfigs")
ListResponseHeadersPolicies = Action("ListResponseHeadersPolicies")
ListSavingsPlans = Action("ListSavingsPlans")
ListStreamingDistributions = Action("ListStreamingDistributions")
ListTagsForResource = Action("ListTagsForResource")
ListUsages = Action("ListUsages")
PublishFunction = Action("PublishFunction")
TagResource = Action("TagResource")
TestFunction = Action("TestFunction")
UntagResource = Action("UntagResource")
UpdateCachePolicy = Action("UpdateCachePolicy")
UpdateCloudFrontOriginAccessIdentity = Action("UpdateCloudFrontOriginAccessIdentity")
UpdateContinuousDeploymentPolicy = Action("UpdateContinuousDeploymentPolicy")
UpdateDistribution = Action("UpdateDistribution")
UpdateDistributionWithStagingConfig = Action("UpdateDistributionWithStagingConfig")
UpdateFieldLevelEncryptionConfig = Action("UpdateFieldLevelEncryptionConfig")
UpdateFieldLevelEncryptionProfile = Action("UpdateFieldLevelEncryptionProfile")
UpdateFunction = Action("UpdateFunction")
UpdateKeyGroup = Action("UpdateKeyGroup")
UpdateKeyValueStore = Action("UpdateKeyValueStore")
UpdateOriginAccessControl = Action("UpdateOriginAccessControl")
UpdateOriginRequestPolicy = Action("UpdateOriginRequestPolicy")
UpdatePublicKey = Action("UpdatePublicKey")
UpdateRealtimeLogConfig = Action("UpdateRealtimeLogConfig")
UpdateResponseHeadersPolicy = Action("UpdateResponseHeadersPolicy")
UpdateSavingsPlan = Action("UpdateSavingsPlan")
UpdateStreamingDistribution = Action("UpdateStreamingDistribution")
