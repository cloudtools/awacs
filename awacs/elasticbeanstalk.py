# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Elastic Beanstalk'
prefix = 'elasticbeanstalk'

CheckDNSAvailability = Action(prefix, 'CheckDNSAvailability')
CreateApplication = Action(prefix, 'CreateApplication')
CreateApplicationVersion = Action(prefix, 'CreateApplicationVersion')
CreateConfigurationTemplate = \
    Action(prefix, 'CreateConfigurationTemplate')
CreateEnvironment = Action(prefix, 'CreateEnvironment')
CreateStorageLocation = Action(prefix, 'CreateStorageLocation')
DeleteApplication = Action(prefix, 'DeleteApplication')
DeleteApplicationVersion = Action(prefix, 'DeleteApplicationVersion')
DeleteConfigurationTemplate = \
    Action(prefix, 'DeleteConfigurationTemplate')
DeleteEnvironmentConfiguration = \
    Action(prefix, 'DeleteEnvironmentConfiguration')
DescribeApplicationVersions = \
    Action(prefix, 'DescribeApplicationVersions')
DescribeApplications = Action(prefix, 'DescribeApplications')
DescribeConfigurationOptions = \
    Action(prefix, 'DescribeConfigurationOptions')
DescribeConfigurationSettings = \
    Action(prefix, 'DescribeConfigurationSettings')
DescribeEnvironmentResources = \
    Action(prefix, 'DescribeEnvironmentResources')
DescribeEnvironments = Action(prefix, 'DescribeEnvironments')
DescribeEvents = Action(prefix, 'DescribeEvents')
ListAvailableSolutionStacks = \
    Action(prefix, 'ListAvailableSolutionStacks')
RebuildEnvironment = Action(prefix, 'RebuildEnvironment')
RequestEnvironmentInfo = Action(prefix, 'RequestEnvironmentInfo')
RestartAppServer = Action(prefix, 'RestartAppServer')
RetrieveEnvironmentInfo = Action(prefix, 'RetrieveEnvironmentInfo')
SwapEnvironmentCNAMEs = Action(prefix, 'SwapEnvironmentCNAMEs')
TerminateEnvironment = Action(prefix, 'TerminateEnvironment')
UpdateApplication = Action(prefix, 'UpdateApplication')
UpdateApplicationVersion = Action(prefix, 'UpdateApplicationVersion')
UpdateConfigurationTemplate = \
    Action(prefix, 'UpdateConfigurationTemplate')
UpdateEnvironment = Action(prefix, 'UpdateEnvironment')
ValidateConfigurationSettings = \
    Action(prefix, 'ValidateConfigurationSettings')
