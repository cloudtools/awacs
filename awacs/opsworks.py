# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS OpsWorks'
prefix = 'opsworks'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssignInstance = Action('AssignInstance')
AssignVolume = Action('AssignVolume')
AssociateElasticIp = Action('AssociateElasticIp')
AttachElasticLoadBalancer = Action('AttachElasticLoadBalancer')
CloneStack = Action('CloneStack')
CreateApp = Action('CreateApp')
CreateDeployment = Action('CreateDeployment')
CreateInstance = Action('CreateInstance')
CreateLayer = Action('CreateLayer')
CreateStack = Action('CreateStack')
CreateUserProfile = Action('CreateUserProfile')
DeleteApp = Action('DeleteApp')
DeleteInstance = Action('DeleteInstance')
DeleteLayer = Action('DeleteLayer')
DeleteStack = Action('DeleteStack')
DeleteUserProfile = Action('DeleteUserProfile')
DeregisterEcsCluster = Action('DeregisterEcsCluster')
DeregisterElasticIp = Action('DeregisterElasticIp')
DeregisterInstance = Action('DeregisterInstance')
DeregisterVolume = Action('DeregisterVolume')
DescribeApps = Action('DescribeApps')
DescribeCommands = Action('DescribeCommands')
DescribeDeployments = Action('DescribeDeployments')
DescribeEcsClusters = Action('DescribeEcsClusters')
DescribeElasticIps = Action('DescribeElasticIps')
DescribeElasticLoadBalancers = Action('DescribeElasticLoadBalancers')
DescribeInstances = Action('DescribeInstances')
DescribeLayers = Action('DescribeLayers')
DescribeLoadBasedAutoScaling = Action('DescribeLoadBasedAutoScaling')
DescribePermissions = Action('DescribePermissions')
DescribeRaidArrays = Action('DescribeRaidArrays')
DescribeRdsDbInstances = Action('DescribeRdsDbInstances')
DescribeServiceErrors = Action('DescribeServiceErrors')
DescribeStackProvisioningParameters = \
    Action('DescribeStackProvisioningParameters')
DescribeStackSummary = Action('DescribeStackSummary')
DescribeStacks = Action('DescribeStacks')
DescribeTimeBasedAutoScaling = Action('DescribeTimeBasedAutoScaling')
DescribeUserProfiles = Action('DescribeUserProfiles')
DescribeVolumes = Action('DescribeVolumes')
DetachElasticLoadBalancer = Action('DetachElasticLoadBalancer')
DisassociateElasticIp = Action('DisassociateElasticIp')
GetHostnameSuggestion = Action('GetHostnameSuggestion')
GrantAccess = Action('GrantAccess')
RebootInstance = Action('RebootInstance')
RegisterEcsCluster = Action('RegisterEcsCluster')
RegisterElasticIp = Action('RegisterElasticIp')
RegisterInstance = Action('RegisterInstance')
RegisterRdsDbInstance = Action('RegisterRdsDbInstance')
RegisterVolume = Action('RegisterVolume')
SetLoadBasedAutoScaling = Action('SetLoadBasedAutoScaling')
SetPermission = Action('SetPermission')
SetTimeBasedAutoScaling = Action('SetTimeBasedAutoScaling')
StartInstance = Action('StartInstance')
StartStack = Action('StartStack')
StopInstance = Action('StopInstance')
StopStack = Action('StopStack')
UnassignInstance = Action('UnassignInstance')
UnassignVolume = Action('UnassignVolume')
UpdateApp = Action('UpdateApp')
UpdateElasticIp = Action('UpdateElasticIp')
UpdateInstance = Action('UpdateInstance')
UpdateLayer = Action('UpdateLayer')
UpdateMyUserProfile = Action('UpdateMyUserProfile')
UpdateRdsDbInstance = Action('UpdateRdsDbInstance')
UpdateStack = Action('UpdateStack')
UpdateUserProfile = Action('UpdateUserProfile')
UpdateVolume = Action('UpdateVolume')
