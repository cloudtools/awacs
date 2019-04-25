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


AddTags = Action('AddTags')
CreateElasticsearchDomain = Action('CreateElasticsearchDomain')
DeleteElasticsearchDomain = Action('DeleteElasticsearchDomain')
DeleteElasticsearchServiceRole = Action('DeleteElasticsearchServiceRole')
DescribeElasticsearchDomain = Action('DescribeElasticsearchDomain')
DescribeElasticsearchDomainConfig = \
    Action('DescribeElasticsearchDomainConfig')
DescribeElasticsearchDomains = Action('DescribeElasticsearchDomains')
DescribeElasticsearchInstanceTypeLimits = \
    Action('DescribeElasticsearchInstanceTypeLimits')
DescribeReservedElasticsearchInstanceOfferings = \
    Action('DescribeReservedElasticsearchInstanceOfferings')
DescribeReservedElasticsearchInstances = \
    Action('DescribeReservedElasticsearchInstances')
ESHttpDelete = Action('ESHttpDelete')
ESHttpGet = Action('ESHttpGet')
ESHttpHead = Action('ESHttpHead')
ESHttpPost = Action('ESHttpPost')
ESHttpPut = Action('ESHttpPut')
GetCompatibleElasticsearchVersions = \
    Action('GetCompatibleElasticsearchVersions')
GetUpgradeHistory = Action('GetUpgradeHistory')
GetUpgradeStatus = Action('GetUpgradeStatus')
ListDomainNames = Action('ListDomainNames')
ListElasticsearchInstanceTypes = Action('ListElasticsearchInstanceTypes')
ListElasticsearchVersions = Action('ListElasticsearchVersions')
ListTags = Action('ListTags')
PurchaseReservedElasticsearchInstance = \
    Action('PurchaseReservedElasticsearchInstance')
RemoveTags = Action('RemoveTags')
UpdateElasticsearchDomainConfig = \
    Action('UpdateElasticsearchDomainConfig')
UpgradeElasticsearchDomain = Action('UpgradeElasticsearchDomain')
