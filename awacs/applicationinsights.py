# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'CloudWatch Application Insights'
prefix = 'applicationinsights'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApplication = Action('CreateApplication')
CreateComponent = Action('CreateComponent')
CreateLogPattern = Action('CreateLogPattern')
DeleteApplication = Action('DeleteApplication')
DeleteComponent = Action('DeleteComponent')
DeleteLogPattern = Action('DeleteLogPattern')
DescribeApplication = Action('DescribeApplication')
DescribeComponent = Action('DescribeComponent')
DescribeComponentConfiguration = Action('DescribeComponentConfiguration')
DescribeComponentConfigurationRecommendation = \
    Action('DescribeComponentConfigurationRecommendation')
DescribeLogPattern = Action('DescribeLogPattern')
DescribeObservation = Action('DescribeObservation')
DescribeProblem = Action('DescribeProblem')
DescribeProblemObservations = Action('DescribeProblemObservations')
ListApplications = Action('ListApplications')
ListComponents = Action('ListComponents')
ListConfigurationHistory = Action('ListConfigurationHistory')
ListLogPatternSets = Action('ListLogPatternSets')
ListLogPatterns = Action('ListLogPatterns')
ListProblems = Action('ListProblems')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
UpdateComponent = Action('UpdateComponent')
UpdateComponentConfiguration = Action('UpdateComponentConfiguration')
UpdateLogPattern = Action('UpdateLogPattern')
