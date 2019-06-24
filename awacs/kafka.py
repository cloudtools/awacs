# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Managed Streaming for Kafka'
prefix = 'kafka'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateCluster = Action('CreateCluster')
CreateConfiguration = Action('CreateConfiguration')
DeleteCluster = Action('DeleteCluster')
DescribeCluster = Action('DescribeCluster')
DescribeClusterOperation = Action('DescribeClusterOperation')
DescribeConfiguration = Action('DescribeConfiguration')
DescribeConfigurationRevision = Action('DescribeConfigurationRevision')
GetBootstrapBrokers = Action('GetBootstrapBrokers')
ListClusterOperations = Action('ListClusterOperations')
ListClusters = Action('ListClusters')
ListConfigurations = Action('ListConfigurations')
ListNodes = Action('ListNodes')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateBrokerStorage = Action('UpdateBrokerStorage')
UpdateClusterConfiguration = Action('UpdateClusterConfiguration')
