# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS DeepLens'
prefix = 'deeplens'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateServiceRoleToAccount = Action('AssociateServiceRoleToAccount')
BatchGetDevice = Action('BatchGetDevice')
BatchGetModel = Action('BatchGetModel')
BatchGetProject = Action('BatchGetProject')
CreateDeviceCertificates = Action('CreateDeviceCertificates')
CreateModel = Action('CreateModel')
CreateProject = Action('CreateProject')
DeleteModel = Action('DeleteModel')
DeleteProject = Action('DeleteProject')
DeployProject = Action('DeployProject')
DeregisterDevice = Action('DeregisterDevice')
GetAssociatedResources = Action('GetAssociatedResources')
GetDeploymentStatus = Action('GetDeploymentStatus')
GetDevice = Action('GetDevice')
GetModel = Action('GetModel')
GetProject = Action('GetProject')
ImportProjectFromTemplate = Action('ImportProjectFromTemplate')
ListDeployments = Action('ListDeployments')
ListDevices = Action('ListDevices')
ListModels = Action('ListModels')
ListProjects = Action('ListProjects')
RegisterDevice = Action('RegisterDevice')
RemoveProject = Action('RemoveProject')
UpdateProject = Action('UpdateProject')
