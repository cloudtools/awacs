# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Data Pipeline"
prefix = "datapipeline"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivatePipeline = Action("ActivatePipeline")
AddTags = Action("AddTags")
CreatePipeline = Action("CreatePipeline")
DeactivatePipeline = Action("DeactivatePipeline")
DeletePipeline = Action("DeletePipeline")
DescribeObjects = Action("DescribeObjects")
DescribePipelines = Action("DescribePipelines")
EvaluateExpression = Action("EvaluateExpression")
GetAccountLimits = Action("GetAccountLimits")
GetPipelineDefinition = Action("GetPipelineDefinition")
ListPipelines = Action("ListPipelines")
PollForTask = Action("PollForTask")
PutAccountLimits = Action("PutAccountLimits")
PutPipelineDefinition = Action("PutPipelineDefinition")
QueryObjects = Action("QueryObjects")
RemoveTags = Action("RemoveTags")
ReportTaskProgress = Action("ReportTaskProgress")
ReportTaskRunnerHeartbeat = Action("ReportTaskRunnerHeartbeat")
SetStatus = Action("SetStatus")
SetTaskStatus = Action("SetTaskStatus")
ValidatePipelineDefinition = Action("ValidatePipelineDefinition")
