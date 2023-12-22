# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kinesis Data Streams"
prefix = "kinesis"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToStream = Action("AddTagsToStream")
CreateStream = Action("CreateStream")
DecreaseStreamRetentionPeriod = Action("DecreaseStreamRetentionPeriod")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteStream = Action("DeleteStream")
DeregisterStreamConsumer = Action("DeregisterStreamConsumer")
DescribeLimits = Action("DescribeLimits")
DescribeStream = Action("DescribeStream")
DescribeStreamConsumer = Action("DescribeStreamConsumer")
DescribeStreamSummary = Action("DescribeStreamSummary")
DisableEnhancedMonitoring = Action("DisableEnhancedMonitoring")
EnableEnhancedMonitoring = Action("EnableEnhancedMonitoring")
GetRecords = Action("GetRecords")
GetResourcePolicy = Action("GetResourcePolicy")
GetShardIterator = Action("GetShardIterator")
IncreaseStreamRetentionPeriod = Action("IncreaseStreamRetentionPeriod")
ListShards = Action("ListShards")
ListStreamConsumers = Action("ListStreamConsumers")
ListStreams = Action("ListStreams")
ListTagsForStream = Action("ListTagsForStream")
MergeShards = Action("MergeShards")
PutRecord = Action("PutRecord")
PutRecords = Action("PutRecords")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterStreamConsumer = Action("RegisterStreamConsumer")
RemoveTagsFromStream = Action("RemoveTagsFromStream")
SplitShard = Action("SplitShard")
StartStreamEncryption = Action("StartStreamEncryption")
StopStreamEncryption = Action("StopStreamEncryption")
SubscribeToShard = Action("SubscribeToShard")
UpdateShardCount = Action("UpdateShardCount")
UpdateStreamMode = Action("UpdateStreamMode")
