# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, ARN


service_name = 'Amazon SQS'
prefix = 'sqs'

AddPermission = Action(prefix, 'AddPermission')
ChangeMessageVisibility = Action(prefix, 'ChangeMessageVisibility')
ChangeMessageVisibilityBatch = \
    Action(prefix, 'ChangeMessageVisibilityBatch')
CreateQueue = Action(prefix, 'CreateQueue')
DeleteMessage = Action(prefix, 'DeleteMessage')
DeleteMessageBatch = Action(prefix, 'DeleteMessageBatch')
DeleteQueue = Action(prefix, 'DeleteQueue')
GetQueueAttributes = Action(prefix, 'GetQueueAttributes')
GetQueueUrl = Action(prefix, 'GetQueueUrl')
ListQueues = Action(prefix, 'ListQueues')
ReceiveMessage = Action(prefix, 'ReceiveMessage')
RemovePermission = Action(prefix, 'RemovePermission')
SendMessage = Action(prefix, 'SendMessage')
SendMessageBatch = Action(prefix, 'SendMessageBatch')
SetQueueAttributes = Action(prefix, 'SetQueueAttributes')


class SQS_ARN(ARN):
    def __init__(self, region, account, resource):
        sup = super(SQS_ARN, self)
        sup.__init__('sqs', region=region, account=account, resource=resource)
