# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Lake Formation"
prefix = "lakeformation"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddLFTagsToResource = Action("AddLFTagsToResource")
BatchGrantPermissions = Action("BatchGrantPermissions")
BatchRevokePermissions = Action("BatchRevokePermissions")
CancelTransaction = Action("CancelTransaction")
CommitTransaction = Action("CommitTransaction")
CreateDataCellsFilter = Action("CreateDataCellsFilter")
CreateLFTag = Action("CreateLFTag")
CreateLakeFormationOptIn = Action("CreateLakeFormationOptIn")
DeleteDataCellsFilter = Action("DeleteDataCellsFilter")
DeleteLFTag = Action("DeleteLFTag")
DeleteLakeFormationOptIn = Action("DeleteLakeFormationOptIn")
DeleteObjectsOnCancel = Action("DeleteObjectsOnCancel")
DeregisterResource = Action("DeregisterResource")
DescribeResource = Action("DescribeResource")
DescribeTransaction = Action("DescribeTransaction")
ExtendTransaction = Action("ExtendTransaction")
GetDataAccess = Action("GetDataAccess")
GetDataCellsFilter = Action("GetDataCellsFilter")
GetDataLakeSettings = Action("GetDataLakeSettings")
GetEffectivePermissionsForPath = Action("GetEffectivePermissionsForPath")
GetLFTag = Action("GetLFTag")
GetQueryState = Action("GetQueryState")
GetQueryStatistics = Action("GetQueryStatistics")
GetResourceLFTags = Action("GetResourceLFTags")
GetTableObjects = Action("GetTableObjects")
GetWorkUnitResults = Action("GetWorkUnitResults")
GetWorkUnits = Action("GetWorkUnits")
GrantPermissions = Action("GrantPermissions")
ListDataCellsFilter = Action("ListDataCellsFilter")
ListLFTags = Action("ListLFTags")
ListLakeFormationOptIns = Action("ListLakeFormationOptIns")
ListPermissions = Action("ListPermissions")
ListResources = Action("ListResources")
ListTableStorageOptimizers = Action("ListTableStorageOptimizers")
ListTransactions = Action("ListTransactions")
PutDataLakeSettings = Action("PutDataLakeSettings")
RegisterResource = Action("RegisterResource")
RemoveLFTagsFromResource = Action("RemoveLFTagsFromResource")
RevokePermissions = Action("RevokePermissions")
SearchDatabasesByLFTags = Action("SearchDatabasesByLFTags")
SearchTablesByLFTags = Action("SearchTablesByLFTags")
StartQueryPlanning = Action("StartQueryPlanning")
StartTransaction = Action("StartTransaction")
UpdateDataCellsFilter = Action("UpdateDataCellsFilter")
UpdateLFTag = Action("UpdateLFTag")
UpdateResource = Action("UpdateResource")
UpdateTableObjects = Action("UpdateTableObjects")
UpdateTableStorageOptimizer = Action("UpdateTableStorageOptimizer")
