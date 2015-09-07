# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS CloudFormation'
prefix = 'cloudformation'


class CloudformationAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


CancelUpdateStack = CloudformationAction('CancelUpdateStack')
CreateStack = CloudformationAction('CreateStack')
DeleteStack = CloudformationAction('DeleteStack')
DescribeStackEvents = CloudformationAction('DescribeStackEvents')
DescribeStackResource = CloudformationAction('DescribeStackResource')
DescribeStackResources = CloudformationAction('DescribeStackResources')
DescribeStacks = CloudformationAction('DescribeStacks')
EstimateTemplateCost = CloudformationAction('EstimateTemplateCost')
GetStackPolicy = CloudformationAction('GetStackPolicy')
GetTemplate = CloudformationAction('GetTemplate')
GetTemplateSummary = CloudformationAction('GetTemplateSummary')
ListStackResources = CloudformationAction('ListStackResources')
ListStacks = CloudformationAction('ListStacks')
SetStackPolicy = CloudformationAction('SetStackPolicy')
SignalResource = CloudformationAction('SignalResource')
UpdateStack = CloudformationAction('UpdateStack')
ValidateTemplate = CloudformationAction('ValidateTemplate')
