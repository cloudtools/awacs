# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Snow Device Management"
prefix = "snow-device-management"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelTask = Action("CancelTask")
CreateTask = Action("CreateTask")
DescribeDevice = Action("DescribeDevice")
DescribeDeviceEc2Instances = Action("DescribeDeviceEc2Instances")
DescribeExecution = Action("DescribeExecution")
DescribeTask = Action("DescribeTask")
ListDeviceResources = Action("ListDeviceResources")
ListDevices = Action("ListDevices")
ListExecutions = Action("ListExecutions")
ListTagsForResource = Action("ListTagsForResource")
ListTasks = Action("ListTasks")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
