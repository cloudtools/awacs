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
DeleteApplication = Action('DeleteApplication')
DeleteComponent = Action('DeleteComponent')
DescribeApplication = Action('DescribeApplication')
DescribeComponent = Action('DescribeComponent')
DescribeComponentConfiguration = Action('DescribeComponentConfiguration')
DescribeComponentConfigurationRecommendation = \
    Action('DescribeComponentConfigurationRecommendation')
DescribeObservation = Action('DescribeObservation')
DescribeProblem = Action('DescribeProblem')
DescribeProblemObservations = Action('DescribeProblemObservations')
ListApplications = Action('ListApplications')
ListComponents = Action('ListComponents')
ListProblems = Action('ListProblems')
UpdateApplication = Action('UpdateApplication')
UpdateComponent = Action('UpdateComponent')
UpdateComponentConfiguration = Action('UpdateComponentConfiguration')
