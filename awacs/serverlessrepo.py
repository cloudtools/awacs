# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Serverless Application Repository'
prefix = 'serverlessrepo'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApplication = Action('CreateApplication')
CreateApplicationVersion = Action('CreateApplicationVersion')
CreateCloudFormationChangeSet = Action('CreateCloudFormationChangeSet')
CreateCloudFormationTemplate = Action('CreateCloudFormationTemplate')
DeleteApplication = Action('DeleteApplication')
GetApplication = Action('GetApplication')
GetApplicationPolicy = Action('GetApplicationPolicy')
GetCloudFormationTemplate = Action('GetCloudFormationTemplate')
ListApplicationDependencies = Action('ListApplicationDependencies')
ListApplicationVersions = Action('ListApplicationVersions')
ListApplications = Action('ListApplications')
PutApplicationPolicy = Action('PutApplicationPolicy')
SearchApplications = Action('SearchApplications')
UpdateApplication = Action('UpdateApplication')
