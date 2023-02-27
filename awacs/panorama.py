# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Panorama"
prefix = "panorama"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApp = Action("CreateApp")
CreateAppDeployment = Action("CreateAppDeployment")
CreateAppVersion = Action("CreateAppVersion")
CreateApplicationInstance = Action("CreateApplicationInstance")
CreateDataSource = Action("CreateDataSource")
CreateDeploymentConfiguration = Action("CreateDeploymentConfiguration")
CreateDevice = Action("CreateDevice")
CreateDeviceUpdate = Action("CreateDeviceUpdate")
CreateInputs = Action("CreateInputs")
CreateJobForDevices = Action("CreateJobForDevices")
CreateModel = Action("CreateModel")
CreateNodeFromTemplateJob = Action("CreateNodeFromTemplateJob")
CreatePackage = Action("CreatePackage")
CreatePackageImportJob = Action("CreatePackageImportJob")
CreateStreams = Action("CreateStreams")
DeleteApp = Action("DeleteApp")
DeleteAppVersion = Action("DeleteAppVersion")
DeleteDataSource = Action("DeleteDataSource")
DeleteDevice = Action("DeleteDevice")
DeleteModel = Action("DeleteModel")
DeletePackage = Action("DeletePackage")
DeregisterPackageVersion = Action("DeregisterPackageVersion")
DescribeApp = Action("DescribeApp")
DescribeAppDeployment = Action("DescribeAppDeployment")
DescribeAppVersion = Action("DescribeAppVersion")
DescribeApplicationInstance = Action("DescribeApplicationInstance")
DescribeApplicationInstanceDetails = Action("DescribeApplicationInstanceDetails")
DescribeDataSource = Action("DescribeDataSource")
DescribeDevice = Action("DescribeDevice")
DescribeDeviceJob = Action("DescribeDeviceJob")
DescribeDeviceUpdate = Action("DescribeDeviceUpdate")
DescribeModel = Action("DescribeModel")
DescribeNode = Action("DescribeNode")
DescribeNodeFromTemplateJob = Action("DescribeNodeFromTemplateJob")
DescribePackage = Action("DescribePackage")
DescribePackageImportJob = Action("DescribePackageImportJob")
DescribePackageVersion = Action("DescribePackageVersion")
DescribeSoftware = Action("DescribeSoftware")
GetDeploymentConfiguration = Action("GetDeploymentConfiguration")
GetInputs = Action("GetInputs")
GetStreams = Action("GetStreams")
GetWebSocketURL = Action("GetWebSocketURL")
ListAppDeploymentOperations = Action("ListAppDeploymentOperations")
ListAppVersions = Action("ListAppVersions")
ListApplicationInstanceDependencies = Action("ListApplicationInstanceDependencies")
ListApplicationInstanceNodeInstances = Action("ListApplicationInstanceNodeInstances")
ListApplicationInstances = Action("ListApplicationInstances")
ListApps = Action("ListApps")
ListDataSources = Action("ListDataSources")
ListDeploymentConfigurations = Action("ListDeploymentConfigurations")
ListDeviceUpdates = Action("ListDeviceUpdates")
ListDevices = Action("ListDevices")
ListDevicesJobs = Action("ListDevicesJobs")
ListModels = Action("ListModels")
ListNodeFromTemplateJobs = Action("ListNodeFromTemplateJobs")
ListNodes = Action("ListNodes")
ListPackageImportJobs = Action("ListPackageImportJobs")
ListPackages = Action("ListPackages")
ListTagsForResource = Action("ListTagsForResource")
ProvisionDevice = Action("ProvisionDevice")
RegisterPackageVersion = Action("RegisterPackageVersion")
RemoveApplicationInstance = Action("RemoveApplicationInstance")
SignalApplicationInstanceNodeInstances = Action(
    "SignalApplicationInstanceNodeInstances"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApp = Action("UpdateApp")
UpdateAppConfiguration = Action("UpdateAppConfiguration")
UpdateDataSource = Action("UpdateDataSource")
UpdateDevice = Action("UpdateDevice")
UpdateDeviceMetadata = Action("UpdateDeviceMetadata")
