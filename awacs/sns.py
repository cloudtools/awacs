import warnings
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SNS'
prefix = 'sns'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class SNS_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(SNS_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use sns.ARN instead.",
                      FutureWarning)


AddPermission = Action('AddPermission')
ConfirmSubscription = Action('ConfirmSubscription')
CreatePlatformApplication = Action('CreatePlatformApplication')
CreatePlatformEndpoint = Action('CreatePlatformEndpoint')
CreateTopic = Action('CreateTopic')
DeleteEndpoint = Action('DeleteEndpoint')
DeletePlatformApplication = Action('DeletePlatformApplication')
DeleteTopic = Action('DeleteTopic')
GetEndpointAttributes = Action('GetEndpointAttributes')
GetPlatformApplicationAttributes = \
    Action('GetPlatformApplicationAttributes')
GetSubscriptionAttributes = Action('GetSubscriptionAttributes')
GetTopicAttributes = Action('GetTopicAttributes')
ListEndpointsByPlatformApplication = \
    Action('ListEndpointsByPlatformApplication')
ListPlatformApplications = Action('ListPlatformApplications')
ListSubscriptions = Action('ListSubscriptions')
ListSubscriptionsByTopic = Action('ListSubscriptionsByTopic')
ListTopics = Action('ListTopics')
Publish = Action('Publish')
RemovePermission = Action('RemovePermission')
SetEndpointAttributes = Action('SetEndpointAttributes')
SetPlatformApplicationAttributes = \
    Action('SetPlatformApplicationAttributes')
SetSubscriptionAttributes = Action('SetSubscriptionAttributes')
SetTopicAttributes = Action('SetTopicAttributes')
Subscribe = Action('Subscribe')
Unsubscribe = Action('Unsubscribe')
