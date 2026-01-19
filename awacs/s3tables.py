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
DeleteTableBucketEncryption = Action("DeleteTableBucketEncryption")
DeleteTableBucketMetricsConfiguration = Action("DeleteTableBucketMetricsConfiguration")
DeleteTableBucketPolicy = Action("DeleteTableBucketPolicy")
DeleteTableBucketReplication = Action("DeleteTableBucketReplication")
DeleteTablePolicy = Action("DeleteTablePolicy")
DeleteTableReplication = Action("DeleteTableReplication")
GetNamespace = Action("GetNamespace")
GetTable = Action("GetTable")
GetTableBucket = Action("GetTableBucket")
GetTableBucketEncryption = Action("GetTableBucketEncryption")
GetTableBucketMaintenanceConfiguration = Action(
    "GetTableBucketMaintenanceConfiguration"
)
GetTableBucketMetricsConfiguration = Action("GetTableBucketMetricsConfiguration")
GetTableBucketPolicy = Action("GetTableBucketPolicy")
GetTableBucketReplication = Action("GetTableBucketReplication")
GetTableBucketStorageClass = Action("GetTableBucketStorageClass")
GetTableData = Action("GetTableData")
GetTableEncryption = Action("GetTableEncryption")
GetTableMaintenanceConfiguration = Action("GetTableMaintenanceConfiguration")
GetTableMaintenanceJobStatus = Action("GetTableMaintenanceJobStatus")
GetTableMetadataLocation = Action("GetTableMetadataLocation")
GetTablePolicy = Action("GetTablePolicy")
GetTableRecordExpirationConfiguration = Action("GetTableRecordExpirationConfiguration")
GetTableRecordExpirationJobStatus = Action("GetTableRecordExpirationJobStatus")
GetTableReplication = Action("GetTableReplication")
GetTableReplicationStatus = Action("GetTableReplicationStatus")
GetTableStorageClass = Action("GetTableStorageClass")
ListNamespaces = Action("ListNamespaces")
ListTableBuckets = Action("ListTableBuckets")
ListTables = Action("ListTables")
ListTagsForResource = Action("ListTagsForResource")
PutTableBucketEncryption = Action("PutTableBucketEncryption")
PutTableBucketMaintenanceConfiguration = Action(
    "PutTableBucketMaintenanceConfiguration"
)
PutTableBucketMetricsConfiguration = Action("PutTableBucketMetricsConfiguration")
PutTableBucketPolicy = Action("PutTableBucketPolicy")
PutTableBucketReplication = Action("PutTableBucketReplication")
PutTableBucketStorageClass = Action("PutTableBucketStorageClass")
PutTableData = Action("PutTableData")
PutTableEncryption = Action("PutTableEncryption")
PutTableMaintenanceConfiguration = Action("PutTableMaintenanceConfiguration")
PutTablePolicy = Action("PutTablePolicy")
PutTableRecordExpirationConfiguration = Action("PutTableRecordExpirationConfiguration")
PutTableReplication = Action("PutTableReplication")
PutTableStorageClass = Action("PutTableStorageClass")
RenameTable = Action("RenameTable")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTableMetadataLocation = Action("UpdateTableMetadataLocation")
