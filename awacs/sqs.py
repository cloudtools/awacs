# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, ARN


# SQS policy action constants.
AddPermission = Action("sqs:AddPermission")
ChangeMessageVisibility = Action("sqs:ChangeMessageVisibility")
ChangeMessageVisibilityBatch = Action("sqs:ChangeMessageVisibilityBatch")
CreateQueue = Action("sqs:CreateQueue")
DeleteMessage = Action("sqs:DeleteMessage")
DeleteMessageBatch = Action("sqs:DeleteMessageBatch")
DeleteQueue = Action("sqs:DeleteQueue")
GetQueueAttributes = Action("sqs:GetQueueAttributes")
GetQueueUrl = Action("sqs:GetQueueUrl")
ListQueues = Action("sqs:ListQueues")
ReceiveMessage = Action("sqs:ReceiveMessage")
RemovePermission = Action("sqs:RemovePermission")
SendMessage = Action("sqs:SendMessage")
SendMessageBatch = Action("sqs:SendMessageBatch")
SetQueueAttributes = Action("sqs:SetQueueAttributes")


class SQS_ARN(ARN):
    def __init__(self, region, account, data):
        sup = super(SQS_ARN, self)
        sup.__init__('sqs', region, account, data)
