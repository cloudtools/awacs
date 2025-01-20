# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Batch"
prefix = "batch"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelJob = Action("CancelJob")
CreateComputeEnvironment = Action("CreateComputeEnvironment")
CreateJobQueue = Action("CreateJobQueue")
CreateSchedulingPolicy = Action("CreateSchedulingPolicy")
DeleteComputeEnvironment = Action("DeleteComputeEnvironment")
DeleteJobQueue = Action("DeleteJobQueue")
DeleteSchedulingPolicy = Action("DeleteSchedulingPolicy")
DeregisterJobDefinition = Action("DeregisterJobDefinition")
DescribeComputeEnvironments = Action("DescribeComputeEnvironments")
DescribeJobDefinitions = Action("DescribeJobDefinitions")
DescribeJobQueues = Action("DescribeJobQueues")
DescribeJobs = Action("DescribeJobs")
DescribeSchedulingPolicies = Action("DescribeSchedulingPolicies")
GetJobQueueSnapshot = Action("GetJobQueueSnapshot")
ListJobs = Action("ListJobs")
ListSchedulingPolicies = Action("ListSchedulingPolicies")
ListTagsForResource = Action("ListTagsForResource")
RegisterJobDefinition = Action("RegisterJobDefinition")
SubmitJob = Action("SubmitJob")
TagResource = Action("TagResource")
TerminateJob = Action("TerminateJob")
UntagResource = Action("UntagResource")
UpdateComputeEnvironment = Action("UpdateComputeEnvironment")
UpdateJobQueue = Action("UpdateJobQueue")
UpdateSchedulingPolicy = Action("UpdateSchedulingPolicy")
