# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS App Runner"
prefix = "apprunner"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateCustomDomain = Action("AssociateCustomDomain")
AssociateWebAcl = Action("AssociateWebAcl")
CreateAutoScalingConfiguration = Action("CreateAutoScalingConfiguration")
CreateConnection = Action("CreateConnection")
CreateObservabilityConfiguration = Action("CreateObservabilityConfiguration")
CreateService = Action("CreateService")
CreateVpcConnector = Action("CreateVpcConnector")
CreateVpcIngressConnection = Action("CreateVpcIngressConnection")
DeleteAutoScalingConfiguration = Action("DeleteAutoScalingConfiguration")
DeleteConnection = Action("DeleteConnection")
DeleteObservabilityConfiguration = Action("DeleteObservabilityConfiguration")
DeleteService = Action("DeleteService")
DeleteVpcConnector = Action("DeleteVpcConnector")
DeleteVpcIngressConnection = Action("DeleteVpcIngressConnection")
DescribeAutoScalingConfiguration = Action("DescribeAutoScalingConfiguration")
DescribeCustomDomains = Action("DescribeCustomDomains")
DescribeObservabilityConfiguration = Action("DescribeObservabilityConfiguration")
DescribeOperation = Action("DescribeOperation")
DescribeService = Action("DescribeService")
DescribeVpcConnector = Action("DescribeVpcConnector")
DescribeVpcIngressConnection = Action("DescribeVpcIngressConnection")
DescribeWebAclForService = Action("DescribeWebAclForService")
DisassociateCustomDomain = Action("DisassociateCustomDomain")
DisassociateWebAcl = Action("DisassociateWebAcl")
ListAssociatedServicesForWebAcl = Action("ListAssociatedServicesForWebAcl")
ListAutoScalingConfigurations = Action("ListAutoScalingConfigurations")
ListConnections = Action("ListConnections")
ListObservabilityConfigurations = Action("ListObservabilityConfigurations")
ListOperations = Action("ListOperations")
ListServices = Action("ListServices")
ListServicesForAutoScalingConfiguration = Action(
    "ListServicesForAutoScalingConfiguration"
)
ListTagsForResource = Action("ListTagsForResource")
ListVpcConnectors = Action("ListVpcConnectors")
ListVpcIngressConnections = Action("ListVpcIngressConnections")
PauseService = Action("PauseService")
ResumeService = Action("ResumeService")
StartDeployment = Action("StartDeployment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDefaultAutoScalingConfiguration = Action("UpdateDefaultAutoScalingConfiguration")
UpdateService = Action("UpdateService")
UpdateVpcIngressConnection = Action("UpdateVpcIngressConnection")
