# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kinesis Analytics"
prefix = "kinesisanalytics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddApplicationCloudWatchLoggingOption = Action("AddApplicationCloudWatchLoggingOption")
AddApplicationInput = Action("AddApplicationInput")
AddApplicationInputProcessingConfiguration = Action(
    "AddApplicationInputProcessingConfiguration"
)
AddApplicationOutput = Action("AddApplicationOutput")
AddApplicationReferenceDataSource = Action("AddApplicationReferenceDataSource")
AddApplicationVpcConfiguration = Action("AddApplicationVpcConfiguration")
CreateApplication = Action("CreateApplication")
CreateApplicationPresignedUrl = Action("CreateApplicationPresignedUrl")
CreateApplicationSnapshot = Action("CreateApplicationSnapshot")
DeleteApplication = Action("DeleteApplication")
DeleteApplicationCloudWatchLoggingOption = Action(
    "DeleteApplicationCloudWatchLoggingOption"
)
DeleteApplicationInputProcessingConfiguration = Action(
    "DeleteApplicationInputProcessingConfiguration"
)
DeleteApplicationOutput = Action("DeleteApplicationOutput")
DeleteApplicationReferenceDataSource = Action("DeleteApplicationReferenceDataSource")
DeleteApplicationSnapshot = Action("DeleteApplicationSnapshot")
DeleteApplicationVpcConfiguration = Action("DeleteApplicationVpcConfiguration")
DescribeApplication = Action("DescribeApplication")
DescribeApplicationOperation = Action("DescribeApplicationOperation")
DescribeApplicationSnapshot = Action("DescribeApplicationSnapshot")
DescribeApplicationVersion = Action("DescribeApplicationVersion")
DiscoverInputSchema = Action("DiscoverInputSchema")
GetApplicationState = Action("GetApplicationState")
ListApplicationOperations = Action("ListApplicationOperations")
ListApplicationSnapshots = Action("ListApplicationSnapshots")
ListApplicationVersions = Action("ListApplicationVersions")
ListApplications = Action("ListApplications")
ListTagsForResource = Action("ListTagsForResource")
RollbackApplication = Action("RollbackApplication")
StartApplication = Action("StartApplication")
StopApplication = Action("StopApplication")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateApplicationMaintenanceConfiguration = Action(
    "UpdateApplicationMaintenanceConfiguration"
)
