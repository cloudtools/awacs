# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic MapReduce'
prefix = 'elasticmapreduce'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddInstanceGroups = Action('AddInstanceGroups')
AddTags = Action('AddTags')
AddJobFlowSteps = Action('AddJobFlowSteps')
CreateSecurityConfiguration = Action('CreateSecurityConfiguration')
DeleteSecurityConfiguration = Action('DeleteSecurityConfiguration')
DescribeCluster = Action('DescribeCluster')
DescribeJobFlows = Action('DescribeJobFlows')
DescribeSecurityConfiguration = Action('DescribeSecurityConfiguration')
DescribeStep = Action('DescribeStep')
ListBootstrapActions = Action('ListBootstrapActions')
ListClusters = Action('ListClusters')
ListInstanceGroups = Action('ListInstanceGroups')
ListInstances = Action('ListInstances')
ListSecurityConfigurations = Action('ListSecurityConfigurations')
ListSteps = Action('ListSteps')
ModifyInstanceGroups = Action('ModifyInstanceGroups')
RemoveTags = Action('RemoveTags')
RunJobFlow = Action('RunJobFlow')
SetTerminationProtection = Action('SetTerminationProtection')
SetVisibleToAllUsers = Action('SetVisibleToAllUsers')
TerminateJobFlows = Action('TerminateJobFlows')
