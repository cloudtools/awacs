# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, BaseARN

service_name = 'AWS CodeDeploy'
prefix = 'codedeploy'


class ARN(BaseARN):
    def __init__(self, region, account, resource):
        sup = super(ARN, self)
        sup.__init__(prefix, region=region, account=account,
                     resource=resource)


AddTagsToOnPremisesInstances = Action(prefix, 'AddTagsToOnPremisesInstance')
BatchGetApplications = Action(prefix, 'BatchGetApplications')
BatchGetDeployments = Action(prefix, 'BatchGetDeployments')
BatchGetOnPremisesInstances = Action(prefix, 'BatchGetOnPremisesInstances')
CreateApplication = Action(prefix, 'CreateApplication')
CreateDeployment = Action(prefix, 'CreateDeployment')
CreateDeploymentConfig = Action(prefix, 'CreateDeploymentConfig')
CreateDeploymentGroup = Action(prefix, 'CreateDeploymentGroup')
DeleteApplication = Action(prefix, 'DeleteApplication')
DeleteDeploymentConfig = Action(prefix, 'DeleteDeploymentConfig')
DeleteDeploymentGroup = Action(prefix, 'DeleteDeploymentGroup')
DeregisterOnPremisesInstance = Action(prefix, 'DeregisterOnPremisesInstance')
GetApplication = Action(prefix, 'GetApplication')
GetApplicationRevision = Action(prefix, 'GetApplicationRevision')
GetDeployment = Action(prefix, 'GetDeployment')
GetDeploymentConfig = Action(prefix, 'GetDeploymentConfig')
GetDeploymentGroup = Action(prefix, 'GetDeploymentGroup')
GetDeploymentInstance = Action(prefix, 'GetDeploymentInstance')
GetOnPremisesInstance = Action(prefix, 'GetOnPremisesInstance')
ListApplicationRevisions = Action(prefix, 'ListApplicationRevisions')
ListApplications = Action(prefix, 'ListApplications')
ListDeploymentConfigs = Action(prefix, 'ListDeploymentConfigs')
ListDeploymentGroups = Action(prefix, 'ListDeploymentGroups')
ListDeploymentInstances = Action(prefix, 'ListDeploymentInstances')
ListDeployments = Action(prefix, 'ListDeployments')
ListOnPremisesInstances = Action(prefix, 'ListOnPremisesInstances')
RegisterApplicationRevision = Action(prefix, 'RegisterApplicationRevision')
RegisterOnPremisesInstance = Action(prefix, 'RegisterOnPremisesInstance')
RemoveTagsFromOnPremisesInstances = \
    Action(prefix, 'RemoveTagsFromOnPremisesInstances')
StopDeployment = Action(prefix, 'StopDeployment')
UpdateApplication = Action(prefix, 'UpdateApplication')
UpdateDeploymentGroup = Action(prefix, 'UpdateDeploymentGroup')
