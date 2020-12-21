# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Well-Architected Tool'
prefix = 'wellarchitected'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateLenses = Action('AssociateLenses')
CreateMilestone = Action('CreateMilestone')
CreateWorkload = Action('CreateWorkload')
CreateWorkloadShare = Action('CreateWorkloadShare')
DeleteWorkload = Action('DeleteWorkload')
DeleteWorkloadShare = Action('DeleteWorkloadShare')
DisassociateLenses = Action('DisassociateLenses')
GetAnswer = Action('GetAnswer')
GetLensReview = Action('GetLensReview')
GetLensReviewReport = Action('GetLensReviewReport')
GetLensVersionDifference = Action('GetLensVersionDifference')
GetMilestone = Action('GetMilestone')
GetWorkload = Action('GetWorkload')
ListAnswers = Action('ListAnswers')
ListLensReviewImprovements = Action('ListLensReviewImprovements')
ListLensReviews = Action('ListLensReviews')
ListLenses = Action('ListLenses')
ListMilestones = Action('ListMilestones')
ListNotifications = Action('ListNotifications')
ListShareInvitations = Action('ListShareInvitations')
ListWorkloadShares = Action('ListWorkloadShares')
ListWorkloads = Action('ListWorkloads')
UpdateAnswer = Action('UpdateAnswer')
UpdateLensReview = Action('UpdateLensReview')
UpdateShareInvitation = Action('UpdateShareInvitation')
UpdateWorkload = Action('UpdateWorkload')
UpdateWorkloadShare = Action('UpdateWorkloadShare')
UpgradeLensReview = Action('UpgradeLensReview')
