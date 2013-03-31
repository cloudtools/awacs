# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon CloudFront'
prefix = 'cloudfront'

CreateCloudFrontOriginAccessIdentity = \
    Action(prefix, 'CreateCloudFrontOriginAccessIdentity')
CreateDistribution = Action(prefix, 'CreateDistribution')
CreateInvalidation = Action(prefix, 'CreateInvalidation')
CreateStreamingDistribution = \
    Action(prefix, 'CreateStreamingDistribution')
DeleteCloudFrontOriginAccessIdentity = \
    Action(prefix, 'DeleteCloudFrontOriginAccessIdentity')
DeleteDistribution = Action(prefix, 'DeleteDistribution')
DeleteStreamingDistribution = \
    Action(prefix, 'DeleteStreamingDistribution')
GetCloudFrontOriginAccessIdentity = \
    Action(prefix, 'GetCloudFrontOriginAccessIdentity')
GetCloudFrontOriginAccessIdentityConfig = \
    Action(prefix, 'GetCloudFrontOriginAccessIdentityConfig')
GetDistribution = Action(prefix, 'GetDistribution')
GetDistributionConfig = Action(prefix, 'GetDistributionConfig')
GetInvalidation = Action(prefix, 'GetInvalidation')
GetStreamingDistribution = Action(prefix, 'GetStreamingDistribution')
GetStreamingDistributionConfig = \
    Action(prefix, 'GetStreamingDistributionConfig')
ListCloudFrontOriginAccessIdentities = \
    Action(prefix, 'ListCloudFrontOriginAccessIdentities')
ListDistributions = Action(prefix, 'ListDistributions')
ListInvalidations = Action(prefix, 'ListInvalidations')
ListStreamingDistributions = \
    Action(prefix, 'ListStreamingDistributions')
UpdateCloudFrontOriginAccessIdentity = \
    Action(prefix, 'UpdateCloudFrontOriginAccessIdentity')
UpdateDistribution = Action(prefix, 'UpdateDistribution')
UpdateStreamingDistribution = \
    Action(prefix, 'UpdateStreamingDistribution')
