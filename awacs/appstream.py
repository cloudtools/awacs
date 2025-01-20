# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AppStream 2.0"
prefix = "appstream"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAppBlockBuilderAppBlock = Action("AssociateAppBlockBuilderAppBlock")
AssociateApplicationFleet = Action("AssociateApplicationFleet")
AssociateApplicationToEntitlement = Action("AssociateApplicationToEntitlement")
AssociateApplicatonToEntitlement = Action("AssociateApplicatonToEntitlement")
AssociateFleet = Action("AssociateFleet")
BatchAssociateUserStack = Action("BatchAssociateUserStack")
BatchDisassociateUserStack = Action("BatchDisassociateUserStack")
CopyImage = Action("CopyImage")
CreateAppBlock = Action("CreateAppBlock")
CreateAppBlockBuilder = Action("CreateAppBlockBuilder")
CreateAppBlockBuilderStreamingURL = Action("CreateAppBlockBuilderStreamingURL")
CreateApplication = Action("CreateApplication")
CreateDirectoryConfig = Action("CreateDirectoryConfig")
CreateEntitlement = Action("CreateEntitlement")
CreateFleet = Action("CreateFleet")
CreateImageBuilder = Action("CreateImageBuilder")
CreateImageBuilderStreamingURL = Action("CreateImageBuilderStreamingURL")
CreateStack = Action("CreateStack")
CreateStreamingURL = Action("CreateStreamingURL")
CreateThemeForStack = Action("CreateThemeForStack")
CreateUpdatedImage = Action("CreateUpdatedImage")
CreateUsageReportSubscription = Action("CreateUsageReportSubscription")
CreateUser = Action("CreateUser")
DeleteAppBlock = Action("DeleteAppBlock")
DeleteAppBlockBuilder = Action("DeleteAppBlockBuilder")
DeleteApplication = Action("DeleteApplication")
DeleteDirectoryConfig = Action("DeleteDirectoryConfig")
DeleteEntitlement = Action("DeleteEntitlement")
DeleteFleet = Action("DeleteFleet")
DeleteImage = Action("DeleteImage")
DeleteImageBuilder = Action("DeleteImageBuilder")
DeleteImagePermissions = Action("DeleteImagePermissions")
DeleteStack = Action("DeleteStack")
DeleteThemeForStack = Action("DeleteThemeForStack")
DeleteUsageReportSubscription = Action("DeleteUsageReportSubscription")
DeleteUser = Action("DeleteUser")
DescribeAppBlockBuilderAppBlockAssociations = Action(
    "DescribeAppBlockBuilderAppBlockAssociations"
)
DescribeAppBlockBuilders = Action("DescribeAppBlockBuilders")
DescribeAppBlocks = Action("DescribeAppBlocks")
DescribeApplicationFleetAssociations = Action("DescribeApplicationFleetAssociations")
DescribeApplications = Action("DescribeApplications")
DescribeDirectoryConfigs = Action("DescribeDirectoryConfigs")
DescribeEntitlements = Action("DescribeEntitlements")
DescribeFleets = Action("DescribeFleets")
DescribeImageBuilders = Action("DescribeImageBuilders")
DescribeImagePermissions = Action("DescribeImagePermissions")
DescribeImages = Action("DescribeImages")
DescribeSessions = Action("DescribeSessions")
DescribeStacks = Action("DescribeStacks")
DescribeThemeForStack = Action("DescribeThemeForStack")
DescribeUsageReportSubscriptions = Action("DescribeUsageReportSubscriptions")
DescribeUserStackAssociations = Action("DescribeUserStackAssociations")
DescribeUsers = Action("DescribeUsers")
DisableUser = Action("DisableUser")
DisassociateAppBlockBuilderAppBlock = Action("DisassociateAppBlockBuilderAppBlock")
DisassociateApplicationFleet = Action("DisassociateApplicationFleet")
DisassociateApplicationFromEntitlement = Action(
    "DisassociateApplicationFromEntitlement"
)
DisassociateApplicatonFromEntitlement = Action("DisassociateApplicatonFromEntitlement")
DisassociateFleet = Action("DisassociateFleet")
EnableUser = Action("EnableUser")
ExpireSession = Action("ExpireSession")
GetImageBuilders = Action("GetImageBuilders")
GetParametersForThemeAssetUpload = Action("GetParametersForThemeAssetUpload")
ListAssociatedFleets = Action("ListAssociatedFleets")
ListAssociatedStacks = Action("ListAssociatedStacks")
ListEntitledApplications = Action("ListEntitledApplications")
ListTagsForResource = Action("ListTagsForResource")
StartAppBlockBuilder = Action("StartAppBlockBuilder")
StartFleet = Action("StartFleet")
StartImageBuilder = Action("StartImageBuilder")
StopAppBlockBuilder = Action("StopAppBlockBuilder")
StopFleet = Action("StopFleet")
StopImageBuilder = Action("StopImageBuilder")
Stream = Action("Stream")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAppBlockBuilder = Action("UpdateAppBlockBuilder")
UpdateApplication = Action("UpdateApplication")
UpdateDirectoryConfig = Action("UpdateDirectoryConfig")
UpdateEntitlement = Action("UpdateEntitlement")
UpdateFleet = Action("UpdateFleet")
UpdateImagePermissions = Action("UpdateImagePermissions")
UpdateStack = Action("UpdateStack")
UpdateThemeForStack = Action("UpdateThemeForStack")
