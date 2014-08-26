# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Elastic MapReduce'
prefix = 'elasticmapreduce'

AddInstanceGroups = Action(prefix, 'AddInstanceGroups')
AddTags = Action(prefix, 'AddTags')
AddJobFlowSteps = Action(prefix, 'AddJobFlowSteps')
DescribeCluster = Action(prefix, 'DescribeCluster')
DescribeJobFlows = Action(prefix, 'DescribeJobFlows')
DescribeStep = Action(prefix, 'DescribeStep')
ListBootstrapActions = Action(prefix, 'ListBootstrapActions')
ListClusters = Action(prefix, 'ListClusters')
ListInstanceGroups = Action(prefix, 'ListInstanceGroups')
ListInstances = Action(prefix, 'ListInstances')
ListSteps = Action(prefix, 'ListSteps')
ModifyInstanceGroups = Action(prefix, 'ModifyInstanceGroups')
RemoveTags = Action(prefix, 'RemoveTags')
RunJobFlow = Action(prefix, 'RunJobFlow')
SetTerminationProtection = Action(prefix, 'SetTerminationProtection')
TerminateJobFlows = Action(prefix, 'TerminateJobFlows')
