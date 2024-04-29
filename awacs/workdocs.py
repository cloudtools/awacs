# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkDocs"
prefix = "workdocs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortDocumentVersionUpload = Action("AbortDocumentVersionUpload")
ActivateUser = Action("ActivateUser")
AddNotificationPermissions = Action("AddNotificationPermissions")
AddResourcePermissions = Action("AddResourcePermissions")
AddUserToGroup = Action("AddUserToGroup")
CheckAlias = Action("CheckAlias")
CreateComment = Action("CreateComment")
CreateCustomMetadata = Action("CreateCustomMetadata")
CreateFolder = Action("CreateFolder")
CreateInstance = Action("CreateInstance")
CreateLabels = Action("CreateLabels")
CreateNotificationSubscription = Action("CreateNotificationSubscription")
CreateUser = Action("CreateUser")
DeactivateUser = Action("DeactivateUser")
DeleteComment = Action("DeleteComment")
DeleteCustomMetadata = Action("DeleteCustomMetadata")
DeleteDocument = Action("DeleteDocument")
DeleteDocumentVersion = Action("DeleteDocumentVersion")
DeleteFolder = Action("DeleteFolder")
DeleteFolderContents = Action("DeleteFolderContents")
DeleteInstance = Action("DeleteInstance")
DeleteLabels = Action("DeleteLabels")
DeleteNotificationPermissions = Action("DeleteNotificationPermissions")
DeleteNotificationSubscription = Action("DeleteNotificationSubscription")
DeleteUser = Action("DeleteUser")
DeregisterDirectory = Action("DeregisterDirectory")
DescribeActivities = Action("DescribeActivities")
DescribeAvailableDirectories = Action("DescribeAvailableDirectories")
DescribeComments = Action("DescribeComments")
DescribeDocumentVersions = Action("DescribeDocumentVersions")
DescribeFolderContents = Action("DescribeFolderContents")
DescribeGroups = Action("DescribeGroups")
DescribeInstanceExports = Action("DescribeInstanceExports")
DescribeInstances = Action("DescribeInstances")
DescribeNotificationPermissions = Action("DescribeNotificationPermissions")
DescribeNotificationSubscriptions = Action("DescribeNotificationSubscriptions")
DescribeResourcePermissions = Action("DescribeResourcePermissions")
DescribeRootFolders = Action("DescribeRootFolders")
DescribeUsers = Action("DescribeUsers")
DownloadDocumentVersion = Action("DownloadDocumentVersion")
GetCurrentUser = Action("GetCurrentUser")
GetDocument = Action("GetDocument")
GetDocumentPath = Action("GetDocumentPath")
GetDocumentVersion = Action("GetDocumentVersion")
GetFolder = Action("GetFolder")
GetFolderPath = Action("GetFolderPath")
GetGroup = Action("GetGroup")
GetResources = Action("GetResources")
InitiateDocumentVersionUpload = Action("InitiateDocumentVersionUpload")
RegisterDirectory = Action("RegisterDirectory")
RemoveAllResourcePermissions = Action("RemoveAllResourcePermissions")
RemoveResourcePermission = Action("RemoveResourcePermission")
RemoveUserFromGroup = Action("RemoveUserFromGroup")
RestoreDocumentVersions = Action("RestoreDocumentVersions")
SearchResources = Action("SearchResources")
StartInstanceExport = Action("StartInstanceExport")
UpdateDocument = Action("UpdateDocument")
UpdateDocumentVersion = Action("UpdateDocumentVersion")
UpdateFolder = Action("UpdateFolder")
UpdateInstanceAlias = Action("UpdateInstanceAlias")
UpdateUser = Action("UpdateUser")
UpdateUserAdministrativeSettings = Action("UpdateUserAdministrativeSettings")
