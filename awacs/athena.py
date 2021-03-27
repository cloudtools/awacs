# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Athena"
prefix = "athena"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetNamedQuery = Action("BatchGetNamedQuery")
BatchGetQueryExecution = Action("BatchGetQueryExecution")
CancelQueryExecution = Action("CancelQueryExecution")
CreateDataCatalog = Action("CreateDataCatalog")
CreateNamedQuery = Action("CreateNamedQuery")
CreatePreparedStatement = Action("CreatePreparedStatement")
CreateWorkGroup = Action("CreateWorkGroup")
DeleteDataCatalog = Action("DeleteDataCatalog")
DeleteNamedQuery = Action("DeleteNamedQuery")
DeletePreparedStatement = Action("DeletePreparedStatement")
DeleteWorkGroup = Action("DeleteWorkGroup")
GetCatalogs = Action("GetCatalogs")
GetDataCatalog = Action("GetDataCatalog")
GetDatabase = Action("GetDatabase")
GetExecutionEngine = Action("GetExecutionEngine")
GetExecutionEngines = Action("GetExecutionEngines")
GetNamedQuery = Action("GetNamedQuery")
GetNamespace = Action("GetNamespace")
GetNamespaces = Action("GetNamespaces")
GetPreparedStatement = Action("GetPreparedStatement")
GetQueryExecution = Action("GetQueryExecution")
GetQueryExecutions = Action("GetQueryExecutions")
GetQueryResults = Action("GetQueryResults")
GetQueryResultsStream = Action("GetQueryResultsStream")
GetTable = Action("GetTable")
GetTableMetadata = Action("GetTableMetadata")
GetTables = Action("GetTables")
GetWorkGroup = Action("GetWorkGroup")
ListDataCatalogs = Action("ListDataCatalogs")
ListDatabases = Action("ListDatabases")
ListEngineVersions = Action("ListEngineVersions")
ListNamedQueries = Action("ListNamedQueries")
ListPreparedStatements = Action("ListPreparedStatements")
ListQueryExecutions = Action("ListQueryExecutions")
ListTableMetadata = Action("ListTableMetadata")
ListTagsForResource = Action("ListTagsForResource")
ListWorkGroups = Action("ListWorkGroups")
RunQuery = Action("RunQuery")
StartQueryExecution = Action("StartQueryExecution")
StopQueryExecution = Action("StopQueryExecution")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataCatalog = Action("UpdateDataCatalog")
UpdatePreparedStatement = Action("UpdatePreparedStatement")
UpdateWorkGroup = Action("UpdateWorkGroup")
