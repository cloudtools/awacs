# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS SimSpace Weaver"
prefix = "simspaceweaver"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSnapshot = Action("CreateSnapshot")
DeleteApp = Action("DeleteApp")
DeleteSimulation = Action("DeleteSimulation")
DescribeApp = Action("DescribeApp")
DescribeSimulation = Action("DescribeSimulation")
ListApps = Action("ListApps")
ListSimulations = Action("ListSimulations")
ListTagsForResource = Action("ListTagsForResource")
StartApp = Action("StartApp")
StartClock = Action("StartClock")
StartSimulation = Action("StartSimulation")
StopApp = Action("StopApp")
StopClock = Action("StopClock")
StopSimulation = Action("StopSimulation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
