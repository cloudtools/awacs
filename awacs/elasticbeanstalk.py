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


ApplyEnvironmentManagedAction = Action('ApplyEnvironmentManagedAction')
CheckDNSAvailability = Action('CheckDNSAvailability')
CreateApplication = Action('CreateApplication')
CreateApplicationVersion = Action('CreateApplicationVersion')
CreateConfigurationTemplate = Action('CreateConfigurationTemplate')
CreateEnvironment = Action('CreateEnvironment')
CreateStorageLocation = Action('CreateStorageLocation')
DeleteApplication = Action('DeleteApplication')
DeleteApplicationVersion = Action('DeleteApplicationVersion')
DeleteConfigurationTemplate = Action('DeleteConfigurationTemplate')
DeleteEnvironmentConfiguration = Action('DeleteEnvironmentConfiguration')
DescribeApplicationVersions = Action('DescribeApplicationVersions')
DescribeApplications = Action('DescribeApplications')
DescribeConfigurationOptions = Action('DescribeConfigurationOptions')
DescribeConfigurationSettings = Action('DescribeConfigurationSettings')
DescribeEnvironmentHealth = Action('DescribeEnvironmentHealth')
DescribeEnvironmentManagedActions = \
    Action('DescribeEnvironmentManagedActions')
DescribeEnvironmentManagedActionHistory = \
    Action('DescribeEnvironmentManagedActionHistory')
DescribeEnvironmentResources = Action('DescribeEnvironmentResources')
DescribeEnvironments = Action('DescribeEnvironments')
DescribeEvents = Action('DescribeEvents')
DescribeInstancesHealth = Action('DescribeInstancesHealth')
ListAvailableSolutionStacks = Action('ListAvailableSolutionStacks')
RebuildEnvironment = Action('RebuildEnvironment')
RequestEnvironmentInfo = Action('RequestEnvironmentInfo')
RestartAppServer = Action('RestartAppServer')
RetrieveEnvironmentInfo = Action('RetrieveEnvironmentInfo')
SwapEnvironmentCNAMEs = Action('SwapEnvironmentCNAMEs')
TerminateEnvironment = Action('TerminateEnvironment')
UpdateApplication = Action('UpdateApplication')
UpdateApplicationVersion = Action('UpdateApplicationVersion')
UpdateConfigurationTemplate = Action('UpdateConfigurationTemplate')
UpdateEnvironment = Action('UpdateEnvironment')
ValidateConfigurationSettings = Action('ValidateConfigurationSettings')
