# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elastic Beanstalk'
prefix = 'elasticbeanstalk'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AbortEnvironmentUpdate = Action('AbortEnvironmentUpdate')
AddTags = Action('AddTags')
ApplyEnvironmentManagedAction = Action('ApplyEnvironmentManagedAction')
CheckDNSAvailability = Action('CheckDNSAvailability')
ComposeEnvironments = Action('ComposeEnvironments')
CreateApplication = Action('CreateApplication')
CreateApplicationVersion = Action('CreateApplicationVersion')
CreateConfigurationTemplate = Action('CreateConfigurationTemplate')
CreateEnvironment = Action('CreateEnvironment')
CreatePlatformVersion = Action('CreatePlatformVersion')
CreateStorageLocation = Action('CreateStorageLocation')
DeleteApplication = Action('DeleteApplication')
DeleteApplicationVersion = Action('DeleteApplicationVersion')
DeleteConfigurationTemplate = Action('DeleteConfigurationTemplate')
DeleteEnvironmentConfiguration = Action('DeleteEnvironmentConfiguration')
DeletePlatformVersion = Action('DeletePlatformVersion')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeApplicationVersions = Action('DescribeApplicationVersions')
DescribeApplications = Action('DescribeApplications')
DescribeConfigurationOptions = Action('DescribeConfigurationOptions')
DescribeConfigurationSettings = Action('DescribeConfigurationSettings')
DescribeEnvironmentHealth = Action('DescribeEnvironmentHealth')
DescribeEnvironmentManagedActionHistory = \
    Action('DescribeEnvironmentManagedActionHistory')
DescribeEnvironmentManagedActions = \
    Action('DescribeEnvironmentManagedActions')
DescribeEnvironmentResources = Action('DescribeEnvironmentResources')
DescribeEnvironments = Action('DescribeEnvironments')
DescribeEvents = Action('DescribeEvents')
DescribeInstancesHealth = Action('DescribeInstancesHealth')
DescribePlatformVersion = Action('DescribePlatformVersion')
ListAvailableSolutionStacks = Action('ListAvailableSolutionStacks')
ListPlatformVersions = Action('ListPlatformVersions')
ListTagsForResource = Action('ListTagsForResource')
RebuildEnvironment = Action('RebuildEnvironment')
RemoveTags = Action('RemoveTags')
RequestEnvironmentInfo = Action('RequestEnvironmentInfo')
RestartAppServer = Action('RestartAppServer')
RetrieveEnvironmentInfo = Action('RetrieveEnvironmentInfo')
SwapEnvironmentCNAMEs = Action('SwapEnvironmentCNAMEs')
TerminateEnvironment = Action('TerminateEnvironment')
UpdateApplication = Action('UpdateApplication')
UpdateApplicationResourceLifecycle = \
    Action('UpdateApplicationResourceLifecycle')
UpdateApplicationVersion = Action('UpdateApplicationVersion')
UpdateConfigurationTemplate = Action('UpdateConfigurationTemplate')
UpdateEnvironment = Action('UpdateEnvironment')
ValidateConfigurationSettings = Action('ValidateConfigurationSettings')
