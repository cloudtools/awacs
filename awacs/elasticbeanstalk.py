# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elastic Beanstalk"
prefix = "elasticbeanstalk"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortEnvironmentUpdate = Action("AbortEnvironmentUpdate")
AddTags = Action("AddTags")
ApplyEnvironmentManagedAction = Action("ApplyEnvironmentManagedAction")
AssociateEnvironmentOperationsRole = Action("AssociateEnvironmentOperationsRole")
CheckDNSAvailability = Action("CheckDNSAvailability")
ComposeEnvironments = Action("ComposeEnvironments")
CreateApplication = Action("CreateApplication")
CreateApplicationVersion = Action("CreateApplicationVersion")
CreateConfigurationTemplate = Action("CreateConfigurationTemplate")
CreateEnvironment = Action("CreateEnvironment")
CreatePlatformVersion = Action("CreatePlatformVersion")
CreateStorageLocation = Action("CreateStorageLocation")
DeleteApplication = Action("DeleteApplication")
DeleteApplicationVersion = Action("DeleteApplicationVersion")
DeleteConfigurationTemplate = Action("DeleteConfigurationTemplate")
DeleteEnvironmentConfiguration = Action("DeleteEnvironmentConfiguration")
DeletePlatformVersion = Action("DeletePlatformVersion")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeApplicationVersions = Action("DescribeApplicationVersions")
DescribeApplications = Action("DescribeApplications")
DescribeConfigurationOptions = Action("DescribeConfigurationOptions")
DescribeConfigurationSettings = Action("DescribeConfigurationSettings")
DescribeEnvironmentHealth = Action("DescribeEnvironmentHealth")
DescribeEnvironmentManagedActionHistory = Action(
    "DescribeEnvironmentManagedActionHistory"
)
DescribeEnvironmentManagedActions = Action("DescribeEnvironmentManagedActions")
DescribeEnvironmentResources = Action("DescribeEnvironmentResources")
DescribeEnvironments = Action("DescribeEnvironments")
DescribeEvents = Action("DescribeEvents")
DescribeInstancesHealth = Action("DescribeInstancesHealth")
DescribePlatformVersion = Action("DescribePlatformVersion")
DisassociateEnvironmentOperationsRole = Action("DisassociateEnvironmentOperationsRole")
ListAvailableSolutionStacks = Action("ListAvailableSolutionStacks")
ListPlatformBranches = Action("ListPlatformBranches")
ListPlatformVersions = Action("ListPlatformVersions")
ListTagsForResource = Action("ListTagsForResource")
PutInstanceStatistics = Action("PutInstanceStatistics")
RebuildEnvironment = Action("RebuildEnvironment")
RemoveTags = Action("RemoveTags")
RequestEnvironmentInfo = Action("RequestEnvironmentInfo")
RestartAppServer = Action("RestartAppServer")
RetrieveEnvironmentInfo = Action("RetrieveEnvironmentInfo")
SwapEnvironmentCNAMEs = Action("SwapEnvironmentCNAMEs")
TerminateEnvironment = Action("TerminateEnvironment")
UpdateApplication = Action("UpdateApplication")
UpdateApplicationResourceLifecycle = Action("UpdateApplicationResourceLifecycle")
UpdateApplicationVersion = Action("UpdateApplicationVersion")
UpdateConfigurationTemplate = Action("UpdateConfigurationTemplate")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateTagsForResource = Action("UpdateTagsForResource")
ValidateConfigurationSettings = Action("ValidateConfigurationSettings")
