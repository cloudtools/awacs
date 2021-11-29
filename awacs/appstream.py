# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AppStream 2.0"
prefix = "appstream"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateApplicationFleet = Action("AssociateApplicationFleet")
AssociateFleet = Action("AssociateFleet")
BatchAssociateUserStack = Action("BatchAssociateUserStack")
BatchDisassociateUserStack = Action("BatchDisassociateUserStack")
CopyImage = Action("CopyImage")
CreateAppBlock = Action("CreateAppBlock")
CreateApplication = Action("CreateApplication")
CreateDirectoryConfig = Action("CreateDirectoryConfig")
CreateFleet = Action("CreateFleet")
CreateImageBuilder = Action("CreateImageBuilder")
CreateImageBuilderStreamingURL = Action("CreateImageBuilderStreamingURL")
CreateStack = Action("CreateStack")
CreateStreamingURL = Action("CreateStreamingURL")
CreateUpdatedImage = Action("CreateUpdatedImage")
CreateUsageReportSubscription = Action("CreateUsageReportSubscription")
CreateUser = Action("CreateUser")
DeleteAppBlock = Action("DeleteAppBlock")
DeleteApplication = Action("DeleteApplication")
DeleteDirectoryConfig = Action("DeleteDirectoryConfig")
DeleteFleet = Action("DeleteFleet")
DeleteImage = Action("DeleteImage")
DeleteImageBuilder = Action("DeleteImageBuilder")
DeleteImagePermissions = Action("DeleteImagePermissions")
DeleteStack = Action("DeleteStack")
DeleteUsageReportSubscription = Action("DeleteUsageReportSubscription")
DeleteUser = Action("DeleteUser")
DescribeAppBlocks = Action("DescribeAppBlocks")
DescribeApplicationFleetAssociations = Action("DescribeApplicationFleetAssociations")
DescribeApplications = Action("DescribeApplications")
DescribeDirectoryConfigs = Action("DescribeDirectoryConfigs")
DescribeFleets = Action("DescribeFleets")
DescribeImageBuilders = Action("DescribeImageBuilders")
DescribeImagePermissions = Action("DescribeImagePermissions")
DescribeImages = Action("DescribeImages")
DescribeSessions = Action("DescribeSessions")
DescribeStacks = Action("DescribeStacks")
DescribeUsageReportSubscriptions = Action("DescribeUsageReportSubscriptions")
DescribeUserStackAssociations = Action("DescribeUserStackAssociations")
DescribeUsers = Action("DescribeUsers")
DisableUser = Action("DisableUser")
DisassociateApplicationFleet = Action("DisassociateApplicationFleet")
DisassociateFleet = Action("DisassociateFleet")
EnableUser = Action("EnableUser")
ExpireSession = Action("ExpireSession")
GetImageBuilders = Action("GetImageBuilders")
GetParametersForThemeAssetUpload = Action("GetParametersForThemeAssetUpload")
ListAssociatedFleets = Action("ListAssociatedFleets")
ListAssociatedStacks = Action("ListAssociatedStacks")
ListTagsForResource = Action("ListTagsForResource")
StartFleet = Action("StartFleet")
StartImageBuilder = Action("StartImageBuilder")
StopFleet = Action("StopFleet")
StopImageBuilder = Action("StopImageBuilder")
Stream = Action("Stream")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateDirectoryConfig = Action("UpdateDirectoryConfig")
UpdateFleet = Action("UpdateFleet")
UpdateImagePermissions = Action("UpdateImagePermissions")
UpdateStack = Action("UpdateStack")
