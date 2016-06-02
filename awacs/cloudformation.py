# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CloudFormation'
prefix = 'cloudformation'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelUpdateStack = Action('CancelUpdateStack')
ContinueUpdateRollback = Action('ContinueUpdateRollback')
CreateChangeSet = Action('CreateChangeSet')
CreateStack = Action('CreateStack')
CreateUploadBucket = Action('CreateUploadBucket')
DeleteStack = Action('DeleteStack')
DescribeAccountLimits = Action('DescribeAccountLimits')
DescribeChangeSet = Action('DescribeChangeSet')
DescribeStackEvents = Action('DescribeStackEvents')
DescribeStackResource = Action('DescribeStackResource')
DescribeStackResources = Action('DescribeStackResources')
DescribeStacks = Action('DescribeStacks')
EstimateTemplateCost = Action('EstimateTemplateCost')
ExecuteChangeSet = Action('ExecuteChangeSet')
GetStackPolicy = Action('GetStackPolicy')
GetTemplate = Action('GetTemplate')
GetTemplateSummary = Action('GetTemplateSummary')
ListChangeSets = Action('ListChangeSets')
ListStackResources = Action('ListStackResources')
ListStacks = Action('ListStacks')
PreviewStackUpdate = Action('PreviewStackUpdate')
SetStackPolicy = Action('SetStackPolicy')
SignalResource = Action('SignalResource')
UpdateStack = Action('UpdateStack')
ValidateTemplate = Action('ValidateTemplate')
