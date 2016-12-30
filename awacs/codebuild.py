# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeBuild '
prefix = 'codebuild'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetBuilds = Action('BatchGetBuilds')
BatchGetProjects = Action('BatchGetProjects')
CreateProject = Action('CreateProject')
DeleteProject = Action('DeleteProject')
ListBuilds = Action('ListBuilds')
ListBuildsForProject = Action('ListBuildsForProject')
ListConnectedOAuthAccounts = Action('ListConnectedOAuthAccounts')
ListProjects = Action('ListProjects')
ListRepositories = Action('ListRepositories')
PersistOAuthToken = Action('PersistOAuthToken')
StartBuild = Action('StartBuild')
StopBuild = Action('StopBuild')
UpdateProject = Action('UpdateProject')
