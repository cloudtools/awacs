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


CreateCloudFrontOriginAccessIdentity = \
    Action('CreateCloudFrontOriginAccessIdentity')
CreateDistribution = Action('CreateDistribution')
CreateInvalidation = Action('CreateInvalidation')
CreateStreamingDistribution = Action('CreateStreamingDistribution')
DeleteCloudFrontOriginAccessIdentity = \
    Action('DeleteCloudFrontOriginAccessIdentity')
DeleteDistribution = Action('DeleteDistribution')
DeleteStreamingDistribution = Action('DeleteStreamingDistribution')
GetCloudFrontOriginAccessIdentity = \
    Action('GetCloudFrontOriginAccessIdentity')
GetCloudFrontOriginAccessIdentityConfig = \
    Action('GetCloudFrontOriginAccessIdentityConfig')
GetDistribution = Action('GetDistribution')
GetDistributionConfig = Action('GetDistributionConfig')
GetInvalidation = Action('GetInvalidation')
GetStreamingDistribution = Action('GetStreamingDistribution')
GetStreamingDistributionConfig = Action('GetStreamingDistributionConfig')
ListCloudFrontOriginAccessIdentities = \
    Action('ListCloudFrontOriginAccessIdentities')
ListDistributions = Action('ListDistributions')
ListDistributionsByWebACLId = Action('ListDistributionsByWebACLId')
ListInvalidations = Action('ListInvalidations')
ListStreamingDistributions = Action('ListStreamingDistributions')
UpdateCloudFrontOriginAccessIdentity = \
    Action('UpdateCloudFrontOriginAccessIdentity')
UpdateDistribution = Action('UpdateDistribution')
UpdateStreamingDistribution = Action('UpdateStreamingDistribution')
