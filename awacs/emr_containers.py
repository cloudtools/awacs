# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EMR on EKS (EMR Containers)"
prefix = "emr-containers"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelJobRun = Action("CancelJobRun")
CreateJobTemplate = Action("CreateJobTemplate")
CreateManagedEndpoint = Action("CreateManagedEndpoint")
CreateSecurityConfiguration = Action("CreateSecurityConfiguration")
CreateVirtualCluster = Action("CreateVirtualCluster")
DeleteJobTemplate = Action("DeleteJobTemplate")
DeleteManagedEndpoint = Action("DeleteManagedEndpoint")
DeleteVirtualCluster = Action("DeleteVirtualCluster")
DescribeJobRun = Action("DescribeJobRun")
DescribeJobTemplate = Action("DescribeJobTemplate")
DescribeManagedEndpoint = Action("DescribeManagedEndpoint")
DescribeSecurityConfiguration = Action("DescribeSecurityConfiguration")
DescribeVirtualCluster = Action("DescribeVirtualCluster")
GetManagedEndpointSessionCredentials = Action("GetManagedEndpointSessionCredentials")
ListJobRuns = Action("ListJobRuns")
ListJobTemplates = Action("ListJobTemplates")
ListManagedEndpoints = Action("ListManagedEndpoints")
ListSecurityConfigurations = Action("ListSecurityConfigurations")
ListTagsForResource = Action("ListTagsForResource")
ListVirtualClusters = Action("ListVirtualClusters")
StartJobRun = Action("StartJobRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
