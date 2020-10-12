# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Batch'
prefix = 'batch'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelJob = Action('CancelJob')
CreateComputeEnvironment = Action('CreateComputeEnvironment')
CreateJobQueue = Action('CreateJobQueue')
DeleteComputeEnvironment = Action('DeleteComputeEnvironment')
DeleteJobQueue = Action('DeleteJobQueue')
DeregisterJobDefinition = Action('DeregisterJobDefinition')
DescribeComputeEnvironments = Action('DescribeComputeEnvironments')
DescribeJobDefinitions = Action('DescribeJobDefinitions')
DescribeJobQueues = Action('DescribeJobQueues')
DescribeJobs = Action('DescribeJobs')
ListJobs = Action('ListJobs')
ListTagsForResource = Action('ListTagsForResource')
RegisterJobDefinition = Action('RegisterJobDefinition')
SubmitJob = Action('SubmitJob')
TagResource = Action('TagResource')
TerminateJob = Action('TerminateJob')
UntagResource = Action('UntagResource')
UpdateComputeEnvironment = Action('UpdateComputeEnvironment')
UpdateJobQueue = Action('UpdateJobQueue')
