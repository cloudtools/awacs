# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodePipeline"
prefix = "codepipeline"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcknowledgeJob = Action("AcknowledgeJob")
AcknowledgeThirdPartyJob = Action("AcknowledgeThirdPartyJob")
CreateCustomActionType = Action("CreateCustomActionType")
CreatePipeline = Action("CreatePipeline")
DeleteCustomActionType = Action("DeleteCustomActionType")
DeletePipeline = Action("DeletePipeline")
DeleteWebhook = Action("DeleteWebhook")
DeregisterWebhookWithThirdParty = Action("DeregisterWebhookWithThirdParty")
DisableStageTransition = Action("DisableStageTransition")
EnableStageTransition = Action("EnableStageTransition")
GetActionType = Action("GetActionType")
GetJobDetails = Action("GetJobDetails")
GetPipeline = Action("GetPipeline")
GetPipelineExecution = Action("GetPipelineExecution")
GetPipelineState = Action("GetPipelineState")
GetThirdPartyJobDetails = Action("GetThirdPartyJobDetails")
ListActionExecutions = Action("ListActionExecutions")
ListActionTypes = Action("ListActionTypes")
ListPipelineExecutions = Action("ListPipelineExecutions")
ListPipelines = Action("ListPipelines")
ListRuleExecutions = Action("ListRuleExecutions")
ListRuleTypes = Action("ListRuleTypes")
ListTagsForResource = Action("ListTagsForResource")
ListWebhooks = Action("ListWebhooks")
OverrideStageCondition = Action("OverrideStageCondition")
PollForJobs = Action("PollForJobs")
PollForThirdPartyJobs = Action("PollForThirdPartyJobs")
PutActionRevision = Action("PutActionRevision")
PutApprovalResult = Action("PutApprovalResult")
PutJobFailureResult = Action("PutJobFailureResult")
PutJobSuccessResult = Action("PutJobSuccessResult")
PutThirdPartyJobFailureResult = Action("PutThirdPartyJobFailureResult")
PutThirdPartyJobSuccessResult = Action("PutThirdPartyJobSuccessResult")
PutWebhook = Action("PutWebhook")
RegisterWebhookWithThirdParty = Action("RegisterWebhookWithThirdParty")
RetryStageExecution = Action("RetryStageExecution")
RollbackStage = Action("RollbackStage")
StartPipelineExecution = Action("StartPipelineExecution")
StopPipelineExecution = Action("StopPipelineExecution")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateActionType = Action("UpdateActionType")
UpdatePipeline = Action("UpdatePipeline")
