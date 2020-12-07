# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon DevOps Guru'
prefix = 'devops-guru'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddNotificationChannel = Action('AddNotificationChannel')
DescribeAccountHealth = Action('DescribeAccountHealth')
DescribeAccountOverview = Action('DescribeAccountOverview')
DescribeAnomaly = Action('DescribeAnomaly')
DescribeInsight = Action('DescribeInsight')
DescribeResourceCollectionHealth = \
    Action('DescribeResourceCollectionHealth')
DescribeServiceIntegration = Action('DescribeServiceIntegration')
GetResourceCollection = Action('GetResourceCollection')
ListAnomaliesForInsight = Action('ListAnomaliesForInsight')
ListEvents = Action('ListEvents')
ListInsights = Action('ListInsights')
ListNotificationChannels = Action('ListNotificationChannels')
ListRecommendations = Action('ListRecommendations')
PutFeedback = Action('PutFeedback')
RemoveNotificationChannel = Action('RemoveNotificationChannel')
SearchInsights = Action('SearchInsights')
UpdateResourceCollection = Action('UpdateResourceCollection')
UpdateServiceIntegration = Action('UpdateServiceIntegration')
