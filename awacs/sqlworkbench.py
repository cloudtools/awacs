# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS SQL Workbench"
prefix = "sqlworkbench"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConnectionWithChart = Action("AssociateConnectionWithChart")
AssociateConnectionWithTab = Action("AssociateConnectionWithTab")
AssociateQueryWithTab = Action("AssociateQueryWithTab")
BatchDeleteFolder = Action("BatchDeleteFolder")
CreateAccount = Action("CreateAccount")
CreateChart = Action("CreateChart")
CreateConnection = Action("CreateConnection")
CreateFolder = Action("CreateFolder")
CreateSavedQuery = Action("CreateSavedQuery")
DeleteChart = Action("DeleteChart")
DeleteConnection = Action("DeleteConnection")
DeleteSavedQuery = Action("DeleteSavedQuery")
DeleteTab = Action("DeleteTab")
DriverExecute = Action("DriverExecute")
GenerateSession = Action("GenerateSession")
GetAccountInfo = Action("GetAccountInfo")
GetChart = Action("GetChart")
GetConnection = Action("GetConnection")
GetKMSKey = Action("GetKMSKey")
GetSavedQuery = Action("GetSavedQuery")
GetUserInfo = Action("GetUserInfo")
GetUserWorkspaceSettings = Action("GetUserWorkspaceSettings")
ListBuckets = Action("ListBuckets")
ListConnections = Action("ListConnections")
ListDatabases = Action("ListDatabases")
ListFiles = Action("ListFiles")
ListKMSKeyAliases = Action("ListKMSKeyAliases")
ListKMSKeys = Action("ListKMSKeys")
ListRedshiftClusters = Action("ListRedshiftClusters")
ListSampleDatabases = Action("ListSampleDatabases")
ListSavedQueryVersions = Action("ListSavedQueryVersions")
ListTabs = Action("ListTabs")
ListTaggedResources = Action("ListTaggedResources")
ListTagsForResource = Action("ListTagsForResource")
PutTab = Action("PutTab")
PutUserWorkspaceSettings = Action("PutUserWorkspaceSettings")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChart = Action("UpdateChart")
UpdateConnection = Action("UpdateConnection")
UpdateFileFolder = Action("UpdateFileFolder")
UpdateFolder = Action("UpdateFolder")
UpdateSavedQuery = Action("UpdateSavedQuery")
