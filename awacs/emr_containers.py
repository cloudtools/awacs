# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EMR on EKS (EMR Containers)'
prefix = 'emr-containers'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelJobRun = Action('CancelJobRun')
CreateVirtualCluster = Action('CreateVirtualCluster')
DeleteVirtualCluster = Action('DeleteVirtualCluster')
DescribeJobRun = Action('DescribeJobRun')
DescribeVirtualCluster = Action('DescribeVirtualCluster')
ListJobRuns = Action('ListJobRuns')
ListTagsForResource = Action('ListTagsForResource')
ListVirtualClusters = Action('ListVirtualClusters')
StartJobRun = Action('StartJobRun')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
