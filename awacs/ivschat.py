# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Interactive Video Service Chat"
prefix = "ivschat"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateChatToken = Action("CreateChatToken")
CreateRoom = Action("CreateRoom")
DeleteMessage = Action("DeleteMessage")
DeleteRoom = Action("DeleteRoom")
DisconnectUser = Action("DisconnectUser")
GetRoom = Action("GetRoom")
ListRooms = Action("ListRooms")
ListTagsForResource = Action("ListTagsForResource")
SendEvent = Action("SendEvent")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateRoom = Action("UpdateRoom")
