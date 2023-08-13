# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SQS"
prefix = "sqs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddPermission = Action("AddPermission")
CancelMessageMoveTask = Action("CancelMessageMoveTask")
ChangeMessageVisibility = Action("ChangeMessageVisibility")
ChangeMessageVisibilityBatch = Action("ChangeMessageVisibilityBatch")
CreateQueue = Action("CreateQueue")
DeleteMessage = Action("DeleteMessage")
DeleteMessageBatch = Action("DeleteMessageBatch")
DeleteQueue = Action("DeleteQueue")
GetQueueAttributes = Action("GetQueueAttributes")
GetQueueUrl = Action("GetQueueUrl")
ListDeadLetterSourceQueues = Action("ListDeadLetterSourceQueues")
ListMessageMoveTasks = Action("ListMessageMoveTasks")
ListQueueTags = Action("ListQueueTags")
ListQueues = Action("ListQueues")
PurgeQueue = Action("PurgeQueue")
ReceiveMessage = Action("ReceiveMessage")
RemovePermission = Action("RemovePermission")
SendMessage = Action("SendMessage")
SendMessageBatch = Action("SendMessageBatch")
SetQueueAttributes = Action("SetQueueAttributes")
StartMessageMoveTask = Action("StartMessageMoveTask")
TagQueue = Action("TagQueue")
UntagQueue = Action("UntagQueue")
