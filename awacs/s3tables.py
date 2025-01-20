# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon S3 Tables"
prefix = "s3tables"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateNamespace = Action("CreateNamespace")
CreateTable = Action("CreateTable")
CreateTableBucket = Action("CreateTableBucket")
DeleteNamespace = Action("DeleteNamespace")
DeleteTable = Action("DeleteTable")
DeleteTableBucket = Action("DeleteTableBucket")
DeleteTableBucketPolicy = Action("DeleteTableBucketPolicy")
DeleteTablePolicy = Action("DeleteTablePolicy")
GetNamespace = Action("GetNamespace")
GetTable = Action("GetTable")
GetTableBucket = Action("GetTableBucket")
GetTableBucketMaintenanceConfiguration = Action(
    "GetTableBucketMaintenanceConfiguration"
)
GetTableBucketPolicy = Action("GetTableBucketPolicy")
GetTableData = Action("GetTableData")
GetTableMaintenanceConfiguration = Action("GetTableMaintenanceConfiguration")
GetTableMaintenanceJobStatus = Action("GetTableMaintenanceJobStatus")
GetTableMetadataLocation = Action("GetTableMetadataLocation")
GetTablePolicy = Action("GetTablePolicy")
ListNamespaces = Action("ListNamespaces")
ListTableBuckets = Action("ListTableBuckets")
ListTables = Action("ListTables")
PutTableBucketMaintenanceConfiguration = Action(
    "PutTableBucketMaintenanceConfiguration"
)
PutTableBucketPolicy = Action("PutTableBucketPolicy")
PutTableData = Action("PutTableData")
PutTableMaintenanceConfiguration = Action("PutTableMaintenanceConfiguration")
PutTablePolicy = Action("PutTablePolicy")
RenameTable = Action("RenameTable")
UpdateTableMetadataLocation = Action("UpdateTableMetadataLocation")
