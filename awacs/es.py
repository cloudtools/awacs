# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elasticsearch Service'
prefix = 'es'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptInboundCrossClusterSearchConnection = \
    Action('AcceptInboundCrossClusterSearchConnection')
AddTags = Action('AddTags')
CreateElasticsearchDomain = Action('CreateElasticsearchDomain')
CreateElasticsearchServiceRole = Action('CreateElasticsearchServiceRole')
CreateOutboundCrossClusterSearchConnection = \
    Action('CreateOutboundCrossClusterSearchConnection')
DeleteElasticsearchDomain = Action('DeleteElasticsearchDomain')
DeleteElasticsearchServiceRole = Action('DeleteElasticsearchServiceRole')
DeleteInboundCrossClusterSearchConnection = \
    Action('DeleteInboundCrossClusterSearchConnection')
DeleteOutboundCrossClusterSearchConnection = \
    Action('DeleteOutboundCrossClusterSearchConnection')
DescribeElasticsearchDomain = Action('DescribeElasticsearchDomain')
DescribeElasticsearchDomainConfig = \
    Action('DescribeElasticsearchDomainConfig')
DescribeElasticsearchDomains = Action('DescribeElasticsearchDomains')
DescribeElasticsearchInstanceTypeLimits = \
    Action('DescribeElasticsearchInstanceTypeLimits')
DescribeInboundCrossClusterSearchConnections = \
    Action('DescribeInboundCrossClusterSearchConnections')
DescribeOutboundCrossClusterSearchConnections = \
    Action('DescribeOutboundCrossClusterSearchConnections')
DescribeReservedElasticsearchInstanceOfferings = \
    Action('DescribeReservedElasticsearchInstanceOfferings')
DescribeReservedElasticsearchInstances = \
    Action('DescribeReservedElasticsearchInstances')
ESCrossClusterGet = Action('ESCrossClusterGet')
ESHttpDelete = Action('ESHttpDelete')
ESHttpGet = Action('ESHttpGet')
ESHttpHead = Action('ESHttpHead')
ESHttpPatch = Action('ESHttpPatch')
ESHttpPost = Action('ESHttpPost')
ESHttpPut = Action('ESHttpPut')
GetCompatibleElasticsearchVersions = \
    Action('GetCompatibleElasticsearchVersions')
GetUpgradeHistory = Action('GetUpgradeHistory')
GetUpgradeStatus = Action('GetUpgradeStatus')
ListDomainNames = Action('ListDomainNames')
ListElasticsearchInstanceTypeDetails = \
    Action('ListElasticsearchInstanceTypeDetails')
ListElasticsearchInstanceTypes = Action('ListElasticsearchInstanceTypes')
ListElasticsearchVersions = Action('ListElasticsearchVersions')
ListTags = Action('ListTags')
PurchaseReservedElasticsearchInstance = \
    Action('PurchaseReservedElasticsearchInstance')
PurchaseReservedElasticsearchInstanceOffering = \
    Action('PurchaseReservedElasticsearchInstanceOffering')
RejectInboundCrossClusterSearchConnection = \
    Action('RejectInboundCrossClusterSearchConnection')
RemoveTags = Action('RemoveTags')
UpdateElasticsearchDomainConfig = \
    Action('UpdateElasticsearchDomainConfig')
UpgradeElasticsearchDomain = Action('UpgradeElasticsearchDomain')
