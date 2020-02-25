# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic Container Service for Kubernetes'
prefix = 'eks'


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
CreateFargateProfile = Action('CreateFargateProfile')
CreateNodegroup = Action('CreateNodegroup')
DeleteCluster = Action('DeleteCluster')
DeleteFargateProfile = Action('DeleteFargateProfile')
DeleteNodegroup = Action('DeleteNodegroup')
DescribeCluster = Action('DescribeCluster')
DescribeFargateProfile = Action('DescribeFargateProfile')
DescribeNodegroup = Action('DescribeNodegroup')
DescribeUpdate = Action('DescribeUpdate')
ListClusters = Action('ListClusters')
ListFargateProfiles = Action('ListFargateProfiles')
ListNodegroups = Action('ListNodegroups')
ListTagsForResource = Action('ListTagsForResource')
ListUpdates = Action('ListUpdates')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateClusterConfig = Action('UpdateClusterConfig')
UpdateClusterVersion = Action('UpdateClusterVersion')
UpdateNodegroupConfig = Action('UpdateNodegroupConfig')
UpdateNodegroupVersion = Action('UpdateNodegroupVersion')
