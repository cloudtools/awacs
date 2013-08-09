# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, ARN

service_name = 'Amazon SNS'
prefix = 'sns'

# SNS policy condition key constants.
EndPoint = "sns:EndPoint"
Protocol = "sns:Protocol"

# SNS policy action constants.
AddPermission = Action(prefix, 'AddPermission')
ConfirmSubscription = Action(prefix, 'ConfirmSubscription')
CreateTopic = Action(prefix, 'CreateTopic')
DeleteTopic = Action(prefix, 'DeleteTopic')
GetTopicAttributes = Action(prefix, 'GetTopicAttributes')
ListSubscriptions = Action(prefix, 'ListSubscriptions')
ListSubscriptionsByTopic = Action(prefix, 'ListSubscriptionsByTopic')
ListTopics = Action(prefix, 'ListTopics')
Publish = Action(prefix, 'Publish')
RemovePermission = Action(prefix, 'RemovePermission')
SetTopicAttributes = Action(prefix, 'SetTopicAttributes')
Subscribe = Action(prefix, 'Subscribe')
Unsubscribe = Action(prefix, 'Unsubscribe')


class SNS_ARN(ARN):
    def __init__(self, region, account, resource):
        sup = super(SNS_ARN, self)
        sup.__init__('sns', region=region, account=account, resource=resource)
