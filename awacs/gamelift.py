# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon GameLift'
prefix = 'gamelift'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAlias = Action('CreateAlias')
CreateBuild = Action('CreateBuild')
CreateFleet = Action('CreateFleet')
CreateGameSession = Action('CreateGameSession')
CreatePlayerSession = Action('CreatePlayerSession')
CreatePlayerSessions = Action('CreatePlayerSessions')
DeleteAlias = Action('DeleteAlias')
DeleteBuild = Action('DeleteBuild')
DeleteFleet = Action('DeleteFleet')
DeleteScalingPolicy = Action('DeleteScalingPolicy')
DescribeAlias = Action('DescribeAlias')
DescribeBuild = Action('DescribeBuild')
DescribeEC2InstanceLimits = Action('DescribeEC2InstanceLimits')
DescribeFleetAttributes = Action('DescribeFleetAttributes')
DescribeFleetCapacity = Action('DescribeFleetCapacity')
DescribeFleetEvents = Action('DescribeFleetEvents')
DescribeFleetPortSettings = Action('DescribeFleetPortSettings')
DescribeFleetUtilization = Action('DescribeFleetUtilization')
DescribeGameSessions = Action('DescribeGameSessions')
DescribeGameSessionDetails = Action('DescribeGameSessionDetails')
DescribeInstances = Action('DescribeInstances')
DescribePlayerSessions = Action('DescribePlayerSessions')
DescribeRuntimeConfiguration = Action('DescribeRuntimeConfiguration')
DescribeScalingPolicies = Action('DescribeScalingPolicies')
GetGameSessionLogUrl = Action('GetGameSessionLogUrl')
GetInstanceAccess = Action('GetInstanceAccess')
ListAliases = Action('ListAliases')
ListBuilds = Action('ListBuilds')
ListFleets = Action('ListFleets')
PutScalingPolicy = Action('PutScalingPolicy')
SearchGameSessions = Action('SearchGameSessions')
RequestUploadCredentials = Action('RequestUploadCredentials')
ResolveAlias = Action('ResolveAlias')
UpdateAlias = Action('UpdateAlias')
UpdateBuild = Action('UpdateBuild')
UpdateFleetAttributes = Action('UpdateFleetAttributes')
UpdateFleetCapacity = Action('UpdateFleetCapacity')
UpdateFleetPortSettings = Action('UpdateFleetPortSettings')
UpdateGameSession = Action('UpdateGameSession')
UpdateRuntimeConfiguration = Action('UpdateRuntimeConfiguration')
