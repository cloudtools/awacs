# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Elastic MapReduce'
prefix = 'elasticmapreduce'

AddInstanceGroups = Action(prefix, 'AddInstanceGroups')
AddJobFlowSteps = Action(prefix, 'AddJobFlowSteps')
DescribeJobFlows = Action(prefix, 'DescribeJobFlows')
ModifyInstanceGroups = Action(prefix, 'ModifyInstanceGroups')
RunJobFlow = Action(prefix, 'RunJobFlow')
SetTerminationProtection = Action(prefix, 'SetTerminationProtection')
TerminateJobFlows = Action(prefix, 'TerminateJobFlows')
