# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Kinesis Firehose"
prefix = "firehose"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDeliveryStream = Action("CreateDeliveryStream")
DeleteDeliveryStream = Action("DeleteDeliveryStream")
DescribeDeliveryStream = Action("DescribeDeliveryStream")
ListDeliveryStreams = Action("ListDeliveryStreams")
ListTagsForDeliveryStream = Action("ListTagsForDeliveryStream")
PutRecord = Action("PutRecord")
PutRecordBatch = Action("PutRecordBatch")
StartDeliveryStreamEncryption = Action("StartDeliveryStreamEncryption")
StopDeliveryStreamEncryption = Action("StopDeliveryStreamEncryption")
TagDeliveryStream = Action("TagDeliveryStream")
UntagDeliveryStream = Action("UntagDeliveryStream")
UpdateDestination = Action("UpdateDestination")
