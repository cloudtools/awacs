# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon DynamoDB"
prefix = "dynamodb"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetItem = Action("BatchGetItem")
BatchWriteItem = Action("BatchWriteItem")
ConditionCheckItem = Action("ConditionCheckItem")
CreateBackup = Action("CreateBackup")
CreateGlobalTable = Action("CreateGlobalTable")
CreateTable = Action("CreateTable")
CreateTableReplica = Action("CreateTableReplica")
DeleteBackup = Action("DeleteBackup")
DeleteItem = Action("DeleteItem")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteTable = Action("DeleteTable")
DeleteTableReplica = Action("DeleteTableReplica")
DescribeBackup = Action("DescribeBackup")
DescribeContinuousBackups = Action("DescribeContinuousBackups")
DescribeContributorInsights = Action("DescribeContributorInsights")
DescribeEndpoints = Action("DescribeEndpoints")
DescribeExport = Action("DescribeExport")
DescribeGlobalTable = Action("DescribeGlobalTable")
DescribeGlobalTableSettings = Action("DescribeGlobalTableSettings")
DescribeImport = Action("DescribeImport")
DescribeKinesisStreamingDestination = Action("DescribeKinesisStreamingDestination")
DescribeLimits = Action("DescribeLimits")
DescribeReservedCapacity = Action("DescribeReservedCapacity")
DescribeReservedCapacityOfferings = Action("DescribeReservedCapacityOfferings")
DescribeStream = Action("DescribeStream")
DescribeTable = Action("DescribeTable")
DescribeTableReplicaAutoScaling = Action("DescribeTableReplicaAutoScaling")
DescribeTimeToLive = Action("DescribeTimeToLive")
DisableKinesisStreamingDestination = Action("DisableKinesisStreamingDestination")
EnableKinesisStreamingDestination = Action("EnableKinesisStreamingDestination")
ExportTableToPointInTime = Action("ExportTableToPointInTime")
GetAbacStatus = Action("GetAbacStatus")
GetItem = Action("GetItem")
GetRecords = Action("GetRecords")
GetResourcePolicy = Action("GetResourcePolicy")
GetShardIterator = Action("GetShardIterator")
ImportTable = Action("ImportTable")
ListBackups = Action("ListBackups")
ListContributorInsights = Action("ListContributorInsights")
ListExports = Action("ListExports")
ListGlobalTables = Action("ListGlobalTables")
ListImports = Action("ListImports")
ListStreams = Action("ListStreams")
ListTables = Action("ListTables")
ListTagsOfResource = Action("ListTagsOfResource")
PartiQLDelete = Action("PartiQLDelete")
PartiQLInsert = Action("PartiQLInsert")
PartiQLSelect = Action("PartiQLSelect")
PartiQLUpdate = Action("PartiQLUpdate")
PurchaseReservedCapacityOfferings = Action("PurchaseReservedCapacityOfferings")
PutItem = Action("PutItem")
PutResourcePolicy = Action("PutResourcePolicy")
Query = Action("Query")
RestoreTableFromAwsBackup = Action("RestoreTableFromAwsBackup")
RestoreTableFromBackup = Action("RestoreTableFromBackup")
RestoreTableToPointInTime = Action("RestoreTableToPointInTime")
Scan = Action("Scan")
StartAwsBackupJob = Action("StartAwsBackupJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAbacStatus = Action("UpdateAbacStatus")
UpdateContinuousBackups = Action("UpdateContinuousBackups")
UpdateContributorInsights = Action("UpdateContributorInsights")
UpdateGlobalTable = Action("UpdateGlobalTable")
UpdateGlobalTableSettings = Action("UpdateGlobalTableSettings")
UpdateGlobalTableVersion = Action("UpdateGlobalTableVersion")
UpdateItem = Action("UpdateItem")
UpdateKinesisStreamingDestination = Action("UpdateKinesisStreamingDestination")
UpdateTable = Action("UpdateTable")
UpdateTableReplicaAutoScaling = Action("UpdateTableReplicaAutoScaling")
UpdateTimeToLive = Action("UpdateTimeToLive")
