# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces AgentAccess MCP Server"
prefix = "agentaccess-mcp"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DoubleClick = Action("DoubleClick")
GetScreenshot = Action("GetScreenshot")
HoldKey = Action("HoldKey")
InvokeMcp = Action("InvokeMcp")
KeyPress = Action("KeyPress")
LeftClick = Action("LeftClick")
LeftClickDrag = Action("LeftClickDrag")
LeftMouseDown = Action("LeftMouseDown")
LeftMouseUp = Action("LeftMouseUp")
MiddleClick = Action("MiddleClick")
MovePointer = Action("MovePointer")
RightClick = Action("RightClick")
Scroll = Action("Scroll")
TripleClick = Action("TripleClick")
TypeText = Action("TypeText")
