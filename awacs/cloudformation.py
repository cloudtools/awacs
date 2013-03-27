# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action


CreateStack = Action("cloudformation:CreateStack")
DeleteStack = Action("cloudformation:DeleteStack")
DescribeStackEvents = Action("cloudformation:DescribeStackEvents")
DescribeStackResource = Action("cloudformation:DescribeStackResource")
DescribeStackResources = Action("cloudformation:DescribeStackResources")
DescribeStacks = Action("cloudformation:DescribeStacks")
EstimateTemplateCost = Action("cloudformation:EstimateTemplateCost")
GetTemplate = Action("cloudformation:GetTemplate")
ListStackResources = Action("cloudformation:ListStackResources")
ListStacks = Action("cloudformation:ListStacks")
UpdateStack = Action("cloudformation:UpdateStack")
ValidateTemplate = Action("cloudformation:ValidateTemplate")
