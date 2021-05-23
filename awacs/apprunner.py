# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS App Runner"
prefix = "apprunner"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateCustomDomain = Action("AssociateCustomDomain")
CreateAutoScalingConfiguration = Action("CreateAutoScalingConfiguration")
CreateConnection = Action("CreateConnection")
CreateService = Action("CreateService")
DeleteAutoScalingConfiguration = Action("DeleteAutoScalingConfiguration")
DeleteConnection = Action("DeleteConnection")
DeleteService = Action("DeleteService")
DescribeAutoScalingConfiguration = Action("DescribeAutoScalingConfiguration")
DescribeCustomDomains = Action("DescribeCustomDomains")
DescribeOperation = Action("DescribeOperation")
DescribeService = Action("DescribeService")
DisassociateCustomDomain = Action("DisassociateCustomDomain")
ListAutoScalingConfigurations = Action("ListAutoScalingConfigurations")
ListConnections = Action("ListConnections")
ListOperations = Action("ListOperations")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
PauseService = Action("PauseService")
ResumeService = Action("ResumeService")
StartDeployment = Action("StartDeployment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateService = Action("UpdateService")
