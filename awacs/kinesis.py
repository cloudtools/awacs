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
AssociateStreamsWithChannel = Action("AssociateStreamsWithChannel")
CreateChannel = Action("CreateChannel")
CreateStream = Action("CreateStream")
DecreaseStreamRetentionPeriod = Action("DecreaseStreamRetentionPeriod")
DeleteChannel = Action("DeleteChannel")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteStream = Action("DeleteStream")
DeregisterStreamConsumer = Action("DeregisterStreamConsumer")
DescribeAccountSettings = Action("DescribeAccountSettings")
DescribeChannel = Action("DescribeChannel")
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
InjectApiError = Action("InjectApiError")
ListChannels = Action("ListChannels")
ListShards = Action("ListShards")
ListStreamConsumers = Action("ListStreamConsumers")
ListStreams = Action("ListStreams")
ListTagsForResource = Action("ListTagsForResource")
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
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateChannel = Action("UpdateChannel")
UpdateMaxRecordSize = Action("UpdateMaxRecordSize")
UpdateShardCount = Action("UpdateShardCount")
UpdateStreamMode = Action("UpdateStreamMode")
UpdateStreamRecordDistributionStrategy = Action(
    "UpdateStreamRecordDistributionStrategy"
)
UpdateStreamWarmThroughput = Action("UpdateStreamWarmThroughput")
