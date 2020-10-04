# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CodeGuru Reviewer'
prefix = 'codeguru-reviewer'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateRepository = Action('AssociateRepository')
CreateConnectionToken = Action('CreateConnectionToken')
DescribeCodeReview = Action('DescribeCodeReview')
DescribeRecommendationFeedback = Action('DescribeRecommendationFeedback')
DescribeRepositoryAssociation = Action('DescribeRepositoryAssociation')
DisassociateRepository = Action('DisassociateRepository')
GetMetricsData = Action('GetMetricsData')
ListCodeReviews = Action('ListCodeReviews')
ListRecommendationFeedback = Action('ListRecommendationFeedback')
ListRecommendations = Action('ListRecommendations')
ListRepositoryAssociations = Action('ListRepositoryAssociations')
ListThirdPartyRepositories = Action('ListThirdPartyRepositories')
PutRecommendationFeedback = Action('PutRecommendationFeedback')
