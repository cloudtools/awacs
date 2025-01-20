# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS SQL Workbench"
prefix = "sqlworkbench"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConnectionWithChart = Action("AssociateConnectionWithChart")
AssociateConnectionWithTab = Action("AssociateConnectionWithTab")
AssociateNotebookWithTab = Action("AssociateNotebookWithTab")
AssociateQueryWithTab = Action("AssociateQueryWithTab")
BatchDeleteFolder = Action("BatchDeleteFolder")
BatchGetNotebookCell = Action("BatchGetNotebookCell")
CreateAccount = Action("CreateAccount")
CreateChart = Action("CreateChart")
CreateConnection = Action("CreateConnection")
CreateFolder = Action("CreateFolder")
CreateNotebook = Action("CreateNotebook")
CreateNotebookCell = Action("CreateNotebookCell")
CreateNotebookFromVersion = Action("CreateNotebookFromVersion")
CreateNotebookVersion = Action("CreateNotebookVersion")
CreateSavedQuery = Action("CreateSavedQuery")
DeleteChart = Action("DeleteChart")
DeleteConnection = Action("DeleteConnection")
DeleteNotebook = Action("DeleteNotebook")
DeleteNotebookCell = Action("DeleteNotebookCell")
DeleteNotebookVersion = Action("DeleteNotebookVersion")
DeleteQCustomContext = Action("DeleteQCustomContext")
DeleteSavedQuery = Action("DeleteSavedQuery")
DeleteSqlGenerationContext = Action("DeleteSqlGenerationContext")
DeleteTab = Action("DeleteTab")
DriverExecute = Action("DriverExecute")
DuplicateNotebook = Action("DuplicateNotebook")
ExportNotebook = Action("ExportNotebook")
GenerateSession = Action("GenerateSession")
GetAccountInfo = Action("GetAccountInfo")
GetAccountSettings = Action("GetAccountSettings")
GetAutocompletionMetadata = Action("GetAutocompletionMetadata")
GetAutocompletionResource = Action("GetAutocompletionResource")
GetChart = Action("GetChart")
GetConnection = Action("GetConnection")
GetKMSKey = Action("GetKMSKey")
GetNotebook = Action("GetNotebook")
GetNotebookVersion = Action("GetNotebookVersion")
GetQCustomContext = Action("GetQCustomContext")
GetQSqlPromptQuotas = Action("GetQSqlPromptQuotas")
GetQSqlRecommendations = Action("GetQSqlRecommendations")
GetQueryExecutionHistory = Action("GetQueryExecutionHistory")
GetSavedQuery = Action("GetSavedQuery")
GetSchemaInference = Action("GetSchemaInference")
GetSqlGenerationContext = Action("GetSqlGenerationContext")
GetSqlRecommendations = Action("GetSqlRecommendations")
GetUserInfo = Action("GetUserInfo")
GetUserWorkspaceSettings = Action("GetUserWorkspaceSettings")
ImportNotebook = Action("ImportNotebook")
ListBuckets = Action("ListBuckets")
ListConnections = Action("ListConnections")
ListDatabases = Action("ListDatabases")
ListFiles = Action("ListFiles")
ListKMSKeyAliases = Action("ListKMSKeyAliases")
ListKMSKeys = Action("ListKMSKeys")
ListNotebookVersions = Action("ListNotebookVersions")
ListNotebooks = Action("ListNotebooks")
ListQueryExecutionHistory = Action("ListQueryExecutionHistory")
ListRedshiftClusters = Action("ListRedshiftClusters")
ListSampleDatabases = Action("ListSampleDatabases")
ListSavedQueryVersions = Action("ListSavedQueryVersions")
ListTabs = Action("ListTabs")
ListTaggedResources = Action("ListTaggedResources")
ListTagsForResource = Action("ListTagsForResource")
PassAccountSettings = Action("PassAccountSettings")
PutQCustomContext = Action("PutQCustomContext")
PutSqlGenerationContext = Action("PutSqlGenerationContext")
PutTab = Action("PutTab")
PutUserWorkspaceSettings = Action("PutUserWorkspaceSettings")
RestoreNotebookVersion = Action("RestoreNotebookVersion")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountConnectionSettings = Action("UpdateAccountConnectionSettings")
UpdateAccountExportSettings = Action("UpdateAccountExportSettings")
UpdateAccountGeneralSettings = Action("UpdateAccountGeneralSettings")
UpdateAccountQSqlSettings = Action("UpdateAccountQSqlSettings")
UpdateChart = Action("UpdateChart")
UpdateConnection = Action("UpdateConnection")
UpdateFileFolder = Action("UpdateFileFolder")
UpdateFolder = Action("UpdateFolder")
UpdateNotebook = Action("UpdateNotebook")
UpdateNotebookCellContent = Action("UpdateNotebookCellContent")
UpdateNotebookCellLayout = Action("UpdateNotebookCellLayout")
UpdateSavedQuery = Action("UpdateSavedQuery")
