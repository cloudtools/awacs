# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Mechanical Turk'
prefix = 'mechanicalturk'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ApproveAssignment = Action('ApproveAssignment')
ApproveRejectedAssignment = Action('ApproveRejectedAssignment')
AssignQualification = Action('AssignQualification')
BlockWorker = Action('BlockWorker')
ChangeHITTypeOfHIT = Action('ChangeHITTypeOfHIT')
CreateHIT = Action('CreateHIT')
CreateQualificationType = Action('CreateQualificationType')
DisableHIT = Action('DisableHIT')
DisposeHIT = Action('DisposeHIT')
DisposeQualificationType = Action('DisposeQualificationType')
ExtendHIT = Action('ExtendHIT')
ForceExpireHIT = Action('ForceExpireHIT')
GetAccountBalance = Action('GetAccountBalance')
GetAssignment = Action('GetAssignment')
GetAssignmentsForHIT = Action('GetAssignmentsForHIT')
GetBlockedWorkers = Action('GetBlockedWorkers')
GetBonusPayments = Action('GetBonusPayments')
GetFileUploadURL = Action('GetFileUploadURL')
GetHIT = Action('GetHIT')
GetHITsForQualificationType = Action('GetHITsForQualificationType')
GetQualificationRequests = Action('GetQualificationRequests')
GetQualificationScore = Action('GetQualificationScore')
GetQualificationType = Action('GetQualificationType')
GetQualificationsForQualificationType = \
    Action('GetQualificationsForQualificationType')
GetRequesterStatistic = Action('GetRequesterStatistic')
GetRequesterWorkerStatistic = Action('GetRequesterWorkerStatistic')
GetReviewResultsForHIT = Action('GetReviewResultsForHIT')
GetReviewableHITs = Action('GetReviewableHITs')
GrantBonus = Action('GrantBonus')
GrantQualification = Action('GrantQualification')
NotifyWorkers = Action('NotifyWorkers')
RegisterHITType = Action('RegisterHITType')
RejectAssignment = Action('RejectAssignment')
RejectQualificationRequest = Action('RejectQualificationRequest')
RevokeQualification = Action('RevokeQualification')
SearchHITs = Action('SearchHITs')
SearchQualificationTypes = Action('SearchQualificationTypes')
SendTestEventNotification = Action('SendTestEventNotification')
SetHITAsReviewing = Action('SetHITAsReviewing')
SetHITTypeNotification = Action('SetHITTypeNotification')
UnblockWorker = Action('UnblockWorker')
UpdateQualificationScore = Action('UpdateQualificationScore')
UpdateQualificationType = Action('UpdateQualificationType')
