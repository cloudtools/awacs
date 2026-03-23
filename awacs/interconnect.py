# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Interconnect"
prefix = "interconnect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptConnectionProposal = Action("AcceptConnectionProposal")
CreateConnection = Action("CreateConnection")
DeleteConnection = Action("DeleteConnection")
DescribeConnectionProposal = Action("DescribeConnectionProposal")
GetConnection = Action("GetConnection")
GetEnvironment = Action("GetEnvironment")
ListAttachPoints = Action("ListAttachPoints")
ListConnections = Action("ListConnections")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnection = Action("UpdateConnection")
