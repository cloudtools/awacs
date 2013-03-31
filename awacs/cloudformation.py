# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS CloudFormation'
prefix = 'cloudformation'

CreateStack = Action(prefix, 'CreateStack')
DeleteStack = Action(prefix, 'DeleteStack')
DescribeStackEvents = Action(prefix, 'DescribeStackEvents')
DescribeStackResource = Action(prefix, 'DescribeStackResource')
DescribeStackResources = Action(prefix, 'DescribeStackResources')
DescribeStacks = Action(prefix, 'DescribeStacks')
EstimateTemplateCost = Action(prefix, 'EstimateTemplateCost')
GetTemplate = Action(prefix, 'GetTemplate')
ListStacks = Action(prefix, 'ListStacks')
ListStackResources = Action(prefix, 'ListStackResources')
UpdateStack = Action(prefix, 'UpdateStack')
ValidateTemplate = Action(prefix, 'ValidateTemplate')
