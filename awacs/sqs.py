import warnings
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SQS'
prefix = 'sqs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class SQS_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(SQS_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use sqs.ARN instead.",
                      FutureWarning)


AddPermission = Action('AddPermission')
ChangeMessageVisibility = Action('ChangeMessageVisibility')
ChangeMessageVisibilityBatch = Action('ChangeMessageVisibilityBatch')
CreateQueue = Action('CreateQueue')
DeleteMessage = Action('DeleteMessage')
DeleteMessageBatch = Action('DeleteMessageBatch')
DeleteQueue = Action('DeleteQueue')
GetQueueAttributes = Action('GetQueueAttributes')
GetQueueUrl = Action('GetQueueUrl')
ListDeadLetterSourceQueues = Action('ListDeadLetterSourceQueues')
ListQueues = Action('ListQueues')
PurgeQueue = Action('PurgeQueue')
ReceiveMessage = Action('ReceiveMessage')
RemovePermission = Action('RemovePermission')
SendMessage = Action('SendMessage')
SendMessageBatch = Action('SendMessageBatch')
SetQueueAttributes = Action('SetQueueAttributes')
