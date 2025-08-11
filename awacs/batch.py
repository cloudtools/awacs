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
CreateConsumableResource = Action("CreateConsumableResource")
CreateJobQueue = Action("CreateJobQueue")
CreateSchedulingPolicy = Action("CreateSchedulingPolicy")
CreateServiceEnvironment = Action("CreateServiceEnvironment")
DeleteComputeEnvironment = Action("DeleteComputeEnvironment")
DeleteConsumableResource = Action("DeleteConsumableResource")
DeleteJobQueue = Action("DeleteJobQueue")
DeleteSchedulingPolicy = Action("DeleteSchedulingPolicy")
DeleteServiceEnvironment = Action("DeleteServiceEnvironment")
DeregisterJobDefinition = Action("DeregisterJobDefinition")
DescribeComputeEnvironments = Action("DescribeComputeEnvironments")
DescribeConsumableResource = Action("DescribeConsumableResource")
DescribeJobDefinitions = Action("DescribeJobDefinitions")
DescribeJobQueues = Action("DescribeJobQueues")
DescribeJobs = Action("DescribeJobs")
DescribeSchedulingPolicies = Action("DescribeSchedulingPolicies")
DescribeServiceEnvironments = Action("DescribeServiceEnvironments")
DescribeServiceJob = Action("DescribeServiceJob")
GetJobQueueSnapshot = Action("GetJobQueueSnapshot")
ListConsumableResources = Action("ListConsumableResources")
ListJobs = Action("ListJobs")
ListJobsByConsumableResource = Action("ListJobsByConsumableResource")
ListSchedulingPolicies = Action("ListSchedulingPolicies")
ListServiceJobs = Action("ListServiceJobs")
ListTagsForResource = Action("ListTagsForResource")
RegisterJobDefinition = Action("RegisterJobDefinition")
SubmitJob = Action("SubmitJob")
SubmitServiceJob = Action("SubmitServiceJob")
TagResource = Action("TagResource")
TerminateJob = Action("TerminateJob")
TerminateServiceJob = Action("TerminateServiceJob")
UntagResource = Action("UntagResource")
UpdateComputeEnvironment = Action("UpdateComputeEnvironment")
UpdateConsumableResource = Action("UpdateConsumableResource")
UpdateJobQueue = Action("UpdateJobQueue")
UpdateSchedulingPolicy = Action("UpdateSchedulingPolicy")
UpdateServiceEnvironment = Action("UpdateServiceEnvironment")
