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


AcceptMatch = Action('AcceptMatch')
ClaimGameServer = Action('ClaimGameServer')
CreateAlias = Action('CreateAlias')
CreateBuild = Action('CreateBuild')
CreateFleet = Action('CreateFleet')
CreateGameServerGroup = Action('CreateGameServerGroup')
CreateGameSession = Action('CreateGameSession')
CreateGameSessionQueue = Action('CreateGameSessionQueue')
CreateMatchmakingConfiguration = Action('CreateMatchmakingConfiguration')
CreateMatchmakingRuleSet = Action('CreateMatchmakingRuleSet')
CreatePlayerSession = Action('CreatePlayerSession')
CreatePlayerSessions = Action('CreatePlayerSessions')
CreateScript = Action('CreateScript')
CreateVpcPeeringAuthorization = Action('CreateVpcPeeringAuthorization')
CreateVpcPeeringConnection = Action('CreateVpcPeeringConnection')
DeleteAlias = Action('DeleteAlias')
DeleteBuild = Action('DeleteBuild')
DeleteFleet = Action('DeleteFleet')
DeleteGameServerGroup = Action('DeleteGameServerGroup')
DeleteGameSessionQueue = Action('DeleteGameSessionQueue')
DeleteMatchmakingConfiguration = Action('DeleteMatchmakingConfiguration')
DeleteMatchmakingRuleSet = Action('DeleteMatchmakingRuleSet')
DeleteScalingPolicy = Action('DeleteScalingPolicy')
DeleteScript = Action('DeleteScript')
DeleteVpcPeeringAuthorization = Action('DeleteVpcPeeringAuthorization')
DeleteVpcPeeringConnection = Action('DeleteVpcPeeringConnection')
DeregisterGameServer = Action('DeregisterGameServer')
DescribeAlias = Action('DescribeAlias')
DescribeBuild = Action('DescribeBuild')
DescribeEC2InstanceLimits = Action('DescribeEC2InstanceLimits')
DescribeFleetAttributes = Action('DescribeFleetAttributes')
DescribeFleetCapacity = Action('DescribeFleetCapacity')
DescribeFleetEvents = Action('DescribeFleetEvents')
DescribeFleetPortSettings = Action('DescribeFleetPortSettings')
DescribeFleetUtilization = Action('DescribeFleetUtilization')
DescribeGameServer = Action('DescribeGameServer')
DescribeGameServerGroup = Action('DescribeGameServerGroup')
DescribeGameServerInstances = Action('DescribeGameServerInstances')
DescribeGameSessionDetails = Action('DescribeGameSessionDetails')
DescribeGameSessionPlacement = Action('DescribeGameSessionPlacement')
DescribeGameSessionQueues = Action('DescribeGameSessionQueues')
DescribeGameSessions = Action('DescribeGameSessions')
DescribeInstances = Action('DescribeInstances')
DescribeMatchmaking = Action('DescribeMatchmaking')
DescribeMatchmakingConfigurations = \
    Action('DescribeMatchmakingConfigurations')
DescribeMatchmakingRuleSets = Action('DescribeMatchmakingRuleSets')
DescribePlayerSessions = Action('DescribePlayerSessions')
DescribeRuntimeConfiguration = Action('DescribeRuntimeConfiguration')
DescribeScalingPolicies = Action('DescribeScalingPolicies')
DescribeScript = Action('DescribeScript')
DescribeVpcPeeringAuthorizations = \
    Action('DescribeVpcPeeringAuthorizations')
DescribeVpcPeeringConnections = Action('DescribeVpcPeeringConnections')
GetGameSessionLogUrl = Action('GetGameSessionLogUrl')
GetInstanceAccess = Action('GetInstanceAccess')
ListAliases = Action('ListAliases')
ListBuilds = Action('ListBuilds')
ListFleets = Action('ListFleets')
ListGameServerGroups = Action('ListGameServerGroups')
ListGameServers = Action('ListGameServers')
ListScripts = Action('ListScripts')
ListTagsForResource = Action('ListTagsForResource')
PutScalingPolicy = Action('PutScalingPolicy')
RegisterGameServer = Action('RegisterGameServer')
RequestUploadCredentials = Action('RequestUploadCredentials')
ResolveAlias = Action('ResolveAlias')
ResumeGameServerGroup = Action('ResumeGameServerGroup')
SearchGameSessions = Action('SearchGameSessions')
StartFleetActions = Action('StartFleetActions')
StartGameSessionPlacement = Action('StartGameSessionPlacement')
StartMatchBackfill = Action('StartMatchBackfill')
StartMatchmaking = Action('StartMatchmaking')
StopFleetActions = Action('StopFleetActions')
StopGameSessionPlacement = Action('StopGameSessionPlacement')
StopMatchmaking = Action('StopMatchmaking')
SuspendGameServerGroup = Action('SuspendGameServerGroup')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAlias = Action('UpdateAlias')
UpdateBuild = Action('UpdateBuild')
UpdateFleetAttributes = Action('UpdateFleetAttributes')
UpdateFleetCapacity = Action('UpdateFleetCapacity')
UpdateFleetPortSettings = Action('UpdateFleetPortSettings')
UpdateGameServer = Action('UpdateGameServer')
UpdateGameServerGroup = Action('UpdateGameServerGroup')
UpdateGameSession = Action('UpdateGameSession')
UpdateGameSessionQueue = Action('UpdateGameSessionQueue')
UpdateMatchmakingConfiguration = Action('UpdateMatchmakingConfiguration')
UpdateRuntimeConfiguration = Action('UpdateRuntimeConfiguration')
UpdateScript = Action('UpdateScript')
ValidateMatchmakingRuleSet = Action('ValidateMatchmakingRuleSet')
