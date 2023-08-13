# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IQ Permissions"
prefix = "iq-permission"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApproveAccessGrant = Action("ApproveAccessGrant")
ApprovePermissionRequest = Action("ApprovePermissionRequest")
AssumePermissionRole = Action("AssumePermissionRole")
CreatePermissionRequest = Action("CreatePermissionRequest")
GetPermissionRequest = Action("GetPermissionRequest")
ListPermissionRequests = Action("ListPermissionRequests")
RejectPermissionRequest = Action("RejectPermissionRequest")
RevokePermissionRequest = Action("RevokePermissionRequest")
WithdrawPermissionRequest = Action("WithdrawPermissionRequest")
