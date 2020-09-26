# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeDeploy'
prefix = 'codedeploy'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToOnPremisesInstances = Action('AddTagsToOnPremisesInstances')
BatchGetApplicationRevisions = Action('BatchGetApplicationRevisions')
BatchGetApplications = Action('BatchGetApplications')
BatchGetDeploymentGroups = Action('BatchGetDeploymentGroups')
BatchGetDeploymentInstances = Action('BatchGetDeploymentInstances')
BatchGetDeploymentTargets = Action('BatchGetDeploymentTargets')
BatchGetDeployments = Action('BatchGetDeployments')
BatchGetOnPremisesInstances = Action('BatchGetOnPremisesInstances')
ContinueDeployment = Action('ContinueDeployment')
CreateApplication = Action('CreateApplication')
CreateCloudFormationDeployment = Action('CreateCloudFormationDeployment')
CreateDeployment = Action('CreateDeployment')
CreateDeploymentConfig = Action('CreateDeploymentConfig')
CreateDeploymentGroup = Action('CreateDeploymentGroup')
DeleteApplication = Action('DeleteApplication')
DeleteDeploymentConfig = Action('DeleteDeploymentConfig')
DeleteDeploymentGroup = Action('DeleteDeploymentGroup')
DeleteGitHubAccountToken = Action('DeleteGitHubAccountToken')
DeleteResourcesByExternalId = Action('DeleteResourcesByExternalId')
DeregisterOnPremisesInstance = Action('DeregisterOnPremisesInstance')
GetApplication = Action('GetApplication')
GetApplicationRevision = Action('GetApplicationRevision')
GetDeployment = Action('GetDeployment')
GetDeploymentConfig = Action('GetDeploymentConfig')
GetDeploymentGroup = Action('GetDeploymentGroup')
GetDeploymentInstance = Action('GetDeploymentInstance')
GetDeploymentTarget = Action('GetDeploymentTarget')
GetOnPremisesInstance = Action('GetOnPremisesInstance')
ListApplicationRevisions = Action('ListApplicationRevisions')
ListApplications = Action('ListApplications')
ListDeploymentConfigs = Action('ListDeploymentConfigs')
ListDeploymentGroups = Action('ListDeploymentGroups')
ListDeploymentInstances = Action('ListDeploymentInstances')
ListDeploymentTargets = Action('ListDeploymentTargets')
ListDeployments = Action('ListDeployments')
ListGitHubAccountTokenNames = Action('ListGitHubAccountTokenNames')
ListOnPremisesInstances = Action('ListOnPremisesInstances')
ListTagsForResource = Action('ListTagsForResource')
PutLifecycleEventHookExecutionStatus = \
    Action('PutLifecycleEventHookExecutionStatus')
RegisterApplicationRevision = Action('RegisterApplicationRevision')
RegisterOnPremisesInstance = Action('RegisterOnPremisesInstance')
RemoveTagsFromOnPremisesInstances = \
    Action('RemoveTagsFromOnPremisesInstances')
SkipWaitTimeForInstanceTermination = \
    Action('SkipWaitTimeForInstanceTermination')
StopDeployment = Action('StopDeployment')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
UpdateDeploymentGroup = Action('UpdateDeploymentGroup')
