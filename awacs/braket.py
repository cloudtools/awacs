# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Braket"
prefix = "braket"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptUserAgreement = Action("AcceptUserAgreement")
AccessBraketFeature = Action("AccessBraketFeature")
CancelJob = Action("CancelJob")
CancelQuantumTask = Action("CancelQuantumTask")
CreateJob = Action("CreateJob")
CreateQuantumTask = Action("CreateQuantumTask")
GetDevice = Action("GetDevice")
GetJob = Action("GetJob")
GetQuantumTask = Action("GetQuantumTask")
GetServiceLinkedRoleStatus = Action("GetServiceLinkedRoleStatus")
GetUserAgreementStatus = Action("GetUserAgreementStatus")
ListTagsForResource = Action("ListTagsForResource")
SearchDevices = Action("SearchDevices")
SearchJobs = Action("SearchJobs")
SearchQuantumTasks = Action("SearchQuantumTasks")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
