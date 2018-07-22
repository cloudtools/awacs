# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Snowball'
prefix = 'snowball'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelCluster = Action('CancelCluster')
CancelJob = Action('CancelJob')
CreateAddress = Action('CreateAddress')
CreateCluster = Action('CreateCluster')
CreateJob = Action('CreateJob')
DescribeAddress = Action('DescribeAddress')
DescribeAddresses = Action('DescribeAddresses')
DescribeCluster = Action('DescribeCluster')
DescribeJob = Action('DescribeJob')
GetJobManifest = Action('GetJobManifest')
GetJobUnlockCode = Action('GetJobUnlockCode')
GetSnowballUsage = Action('GetSnowballUsage')
ListClusterJobs = Action('ListClusterJobs')
ListClusters = Action('ListClusters')
ListJobs = Action('ListJobs')
UpdateCluster = Action('UpdateCluster')
UpdateJob = Action('UpdateJob')
