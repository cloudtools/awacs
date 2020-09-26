# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudFront'
prefix = 'cloudfront'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateCachePolicy = Action('CreateCachePolicy')
CreateCloudFrontOriginAccessIdentity = \
    Action('CreateCloudFrontOriginAccessIdentity')
CreateDistribution = Action('CreateDistribution')
CreateDistributionWithTags = Action('CreateDistributionWithTags')
CreateFieldLevelEncryptionConfig = \
    Action('CreateFieldLevelEncryptionConfig')
CreateFieldLevelEncryptionProfile = \
    Action('CreateFieldLevelEncryptionProfile')
CreateInvalidation = Action('CreateInvalidation')
CreateOriginRequestPolicy = Action('CreateOriginRequestPolicy')
CreatePublicKey = Action('CreatePublicKey')
CreateStreamingDistribution = Action('CreateStreamingDistribution')
CreateStreamingDistributionWithTags = \
    Action('CreateStreamingDistributionWithTags')
DeleteCachePolicy = Action('DeleteCachePolicy')
DeleteCloudFrontOriginAccessIdentity = \
    Action('DeleteCloudFrontOriginAccessIdentity')
DeleteDistribution = Action('DeleteDistribution')
DeleteFieldLevelEncryptionConfig = \
    Action('DeleteFieldLevelEncryptionConfig')
DeleteFieldLevelEncryptionProfile = \
    Action('DeleteFieldLevelEncryptionProfile')
DeleteOriginRequestPolicy = Action('DeleteOriginRequestPolicy')
DeletePublicKey = Action('DeletePublicKey')
DeleteStreamingDistribution = Action('DeleteStreamingDistribution')
GetCachePolicy = Action('GetCachePolicy')
GetCachePolicyConfig = Action('GetCachePolicyConfig')
GetCloudFrontOriginAccessIdentity = \
    Action('GetCloudFrontOriginAccessIdentity')
GetCloudFrontOriginAccessIdentityConfig = \
    Action('GetCloudFrontOriginAccessIdentityConfig')
GetDistribution = Action('GetDistribution')
GetDistributionConfig = Action('GetDistributionConfig')
GetFieldLevelEncryption = Action('GetFieldLevelEncryption')
GetFieldLevelEncryptionConfig = Action('GetFieldLevelEncryptionConfig')
GetFieldLevelEncryptionProfile = Action('GetFieldLevelEncryptionProfile')
GetFieldLevelEncryptionProfileConfig = \
    Action('GetFieldLevelEncryptionProfileConfig')
GetInvalidation = Action('GetInvalidation')
GetOriginRequestPolicy = Action('GetOriginRequestPolicy')
GetOriginRequestPolicyConfig = Action('GetOriginRequestPolicyConfig')
GetPublicKey = Action('GetPublicKey')
GetPublicKeyConfig = Action('GetPublicKeyConfig')
GetStreamingDistribution = Action('GetStreamingDistribution')
GetStreamingDistributionConfig = Action('GetStreamingDistributionConfig')
ListCachePolicies = Action('ListCachePolicies')
ListCloudFrontOriginAccessIdentities = \
    Action('ListCloudFrontOriginAccessIdentities')
ListDistributions = Action('ListDistributions')
ListDistributionsByCachePolicyId = \
    Action('ListDistributionsByCachePolicyId')
ListDistributionsByLambdaFunction = \
    Action('ListDistributionsByLambdaFunction')
ListDistributionsByOriginRequestPolicyId = \
    Action('ListDistributionsByOriginRequestPolicyId')
ListDistributionsByWebACLId = Action('ListDistributionsByWebACLId')
ListFieldLevelEncryptionConfigs = \
    Action('ListFieldLevelEncryptionConfigs')
ListFieldLevelEncryptionProfiles = \
    Action('ListFieldLevelEncryptionProfiles')
ListInvalidations = Action('ListInvalidations')
ListOriginRequestPolicies = Action('ListOriginRequestPolicies')
ListPublicKeys = Action('ListPublicKeys')
ListStreamingDistributions = Action('ListStreamingDistributions')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateCachePolicy = Action('UpdateCachePolicy')
UpdateCloudFrontOriginAccessIdentity = \
    Action('UpdateCloudFrontOriginAccessIdentity')
UpdateDistribution = Action('UpdateDistribution')
UpdateFieldLevelEncryptionConfig = \
    Action('UpdateFieldLevelEncryptionConfig')
UpdateFieldLevelEncryptionProfile = \
    Action('UpdateFieldLevelEncryptionProfile')
UpdateOriginRequestPolicy = Action('UpdateOriginRequestPolicy')
UpdatePublicKey = Action('UpdatePublicKey')
UpdateStreamingDistribution = Action('UpdateStreamingDistribution')
