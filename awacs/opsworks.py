# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS OpsWorks'
prefix = 'opsworks'

AssignVolume = Action(prefix, 'AssignVolume')
AssociateElasticIp = Action(prefix, 'AssociateElasticIp')
AttachElasticLoadBalancer = Action(prefix, 'AttachElasticLoadBalancer')
CloneStack = Action(prefix, 'CloneStack')
CreateApp = Action(prefix, 'CreateApp')
CreateDeployment = Action(prefix, 'CreateDeployment')
CreateInstance = Action(prefix, 'CreateInstance')
CreateLayer = Action(prefix, 'CreateLayer')
CreateStack = Action(prefix, 'CreateStack')
CreateUserProfile = Action(prefix, 'CreateUserProfile')
DeleteApp = Action(prefix, 'DeleteApp')
DeleteInstance = Action(prefix, 'DeleteInstance')
DeleteLayer = Action(prefix, 'DeleteLayer')
DeleteStack = Action(prefix, 'DeleteStack')
DeleteUserProfile = Action(prefix, 'DeleteUserProfile')
DeregisterElasticIp = Action(prefix, 'DeregisterElasticIp')
DeregisterVolume = Action(prefix, 'DeregisterVolume')
DescribeApps = Action(prefix, 'DescribeApps')
DescribeCommands = Action(prefix, 'DescribeCommands')
DescribeDeployments = Action(prefix, 'DescribeDeployments')
DescribeElasticIps = Action(prefix, 'DescribeElasticIps')
DescribeElasticLoadBalancers = \
    Action(prefix, 'DescribeElasticLoadBalancers')
DescribeInstances = Action(prefix, 'DescribeInstances')
DescribeLayers = Action(prefix, 'DescribeLayers')
DescribeLoadBasedAutoScaling = \
    Action(prefix, 'DescribeLoadBasedAutoScaling')
DescribePermissions = Action(prefix, 'DescribePermissions')
DescribeRaidArrays = Action(prefix, 'DescribeRaidArrays')
DescribeServiceErrors = Action(prefix, 'DescribeServiceErrors')
DescribeStacks = Action(prefix, 'DescribeStacks')
DescribeTimeBasedAutoScaling = \
    Action(prefix, 'DescribeTimeBasedAutoScaling')
DescribeUserProfiles = Action(prefix, 'DescribeUserProfiles')
DescribeVolumes = Action(prefix, 'DescribeVolumes')
DetachElasticLoadBalancer = Action(prefix, 'DetachElasticLoadBalancer')
DisassociateElasticIp = Action(prefix, 'DisassociateElasticIp')
GetHostnameSuggestion = Action(prefix, 'GetHostnameSuggestion')
RebootInstance = Action(prefix, 'RebootInstance')
RegisterElasticIp = Action(prefix, 'RegisterElasticIp')
RegisterVolume = Action(prefix, 'RegisterVolume')
SetLoadBasedAutoScaling = Action(prefix, 'SetLoadBasedAutoScaling')
SetPermission = Action(prefix, 'SetPermission')
SetTimeBasedAutoScaling = Action(prefix, 'SetTimeBasedAutoScaling')
StartInstance = Action(prefix, 'StartInstance')
StartStack = Action(prefix, 'StartStack')
StopInstance = Action(prefix, 'StopInstance')
StopStack = Action(prefix, 'StopStack')
UnassignVolume = Action(prefix, 'UnassignVolume')
UpdateApp = Action(prefix, 'UpdateApp')
UpdateElasticIp = Action(prefix, 'UpdateElasticIp')
UpdateInstance = Action(prefix, 'UpdateInstance')
UpdateLayer = Action(prefix, 'UpdateLayer')
UpdateStack = Action(prefix, 'UpdateStack')
UpdateUserProfile = Action(prefix, 'UpdateUserProfile')
UpdateVolume = Action(prefix, 'UpdateVolume')
