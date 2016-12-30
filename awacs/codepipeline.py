# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodePipeline'
prefix = 'codepipeline'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcknowledgeJob = Action('AcknowledgeJob')
AcknowledgeThirdPartyJob = Action('AcknowledgeThirdPartyJob')
CreateCustomActionType = Action('CreateCustomActionType')
CreatePipeline = Action('CreatePipeline')
DeleteCustomActionType = Action('DeleteCustomActionType')
DeletePipeline = Action('DeletePipeline')
DisableStageTransition = Action('DisableStageTransition')
EnableStageTransition = Action('EnableStageTransition')
GetJobDetails = Action('GetJobDetails')
GetPipeline = Action('GetPipeline')
GetPipelineState = Action('GetPipelineState')
GetThirdPartyJobDetails = Action('GetThirdPartyJobDetails')
ListActionTypes = Action('ListActionTypes')
ListPipelines = Action('ListPipelines')
PollForJobs = Action('PollForJobs')
PollForThirdPartyJobs = Action('PollForThirdPartyJobs')
PutActionRevision = Action('PutActionRevision')
PutApprovalResult = Action('PutApprovalResult')
PutJobFailureResult = Action('PutJobFailureResult')
PutJobSuccessResult = Action('PutJobSuccessResult')
PutThirdPartyJobFailureResult = Action('PutThirdPartyJobFailureResult')
PutThirdPartyJobSuccessResult = Action('PutThirdPartyJobSuccessResult')
RetryStageExecution = Action('RetryStageExecution')
StartPipelineExecution = Action('StartPipelineExecution')
UpdatePipeline = Action('UpdatePipeline')
