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
CreateStackInstances = Action('CreateStackInstances')
CreateStackSet = Action('CreateStackSet')
CreateUploadBucket = Action('CreateUploadBucket')
DeleteChangeSet = Action('DeleteChangeSet')
DeleteStack = Action('DeleteStack')
DeleteStackInstances = Action('DeleteStackInstances')
DeleteStackSet = Action('DeleteStackSet')
DeregisterType = Action('DeregisterType')
DescribeAccountLimits = Action('DescribeAccountLimits')
DescribeChangeSet = Action('DescribeChangeSet')
DescribeStackDriftDetectionStatus = \
    Action('DescribeStackDriftDetectionStatus')
DescribeStackEvents = Action('DescribeStackEvents')
DescribeStackInstance = Action('DescribeStackInstance')
DescribeStackResource = Action('DescribeStackResource')
DescribeStackResourceDrifts = Action('DescribeStackResourceDrifts')
DescribeStackResources = Action('DescribeStackResources')
DescribeStackSet = Action('DescribeStackSet')
DescribeStackSetOperation = Action('DescribeStackSetOperation')
DescribeStacks = Action('DescribeStacks')
DescribeType = Action('DescribeType')
DescribeTypeRegistration = Action('DescribeTypeRegistration')
DetectStackDrift = Action('DetectStackDrift')
DetectStackResourceDrift = Action('DetectStackResourceDrift')
DetectStackSetDrift = Action('DetectStackSetDrift')
EstimateTemplateCost = Action('EstimateTemplateCost')
ExecuteChangeSet = Action('ExecuteChangeSet')
GetStackPolicy = Action('GetStackPolicy')
GetTemplate = Action('GetTemplate')
GetTemplateSummary = Action('GetTemplateSummary')
ListChangeSets = Action('ListChangeSets')
ListExports = Action('ListExports')
ListImports = Action('ListImports')
ListStackInstances = Action('ListStackInstances')
ListStackResources = Action('ListStackResources')
ListStackSetOperationResults = Action('ListStackSetOperationResults')
ListStackSetOperations = Action('ListStackSetOperations')
ListStackSets = Action('ListStackSets')
ListStacks = Action('ListStacks')
ListTypeRegistrations = Action('ListTypeRegistrations')
ListTypeVersions = Action('ListTypeVersions')
ListTypes = Action('ListTypes')
PreviewStackUpdate = Action('PreviewStackUpdate')
RegisterType = Action('RegisterType')
SetStackPolicy = Action('SetStackPolicy')
SetTypeDefaultVersion = Action('SetTypeDefaultVersion')
SignalResource = Action('SignalResource')
StopStackSetOperation = Action('StopStackSetOperation')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateStack = Action('UpdateStack')
UpdateStackInstances = Action('UpdateStackInstances')
UpdateStackSet = Action('UpdateStackSet')
UpdateTerminationProtection = Action('UpdateTerminationProtection')
ValidateTemplate = Action('ValidateTemplate')
