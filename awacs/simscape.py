# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS SimScape"
prefix = "simscape"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeleteAgent = Action("DeleteAgent")
DeleteSimulation = Action("DeleteSimulation")
DescribeAgent = Action("DescribeAgent")
DescribeSimulation = Action("DescribeSimulation")
ListAgents = Action("ListAgents")
ListSimulations = Action("ListSimulations")
ListTagsForResource = Action("ListTagsForResource")
StartAgent = Action("StartAgent")
StartClock = Action("StartClock")
StartSimulation = Action("StartSimulation")
StopAgent = Action("StopAgent")
StopClock = Action("StopClock")
StopSimulation = Action("StopSimulation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
