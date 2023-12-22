# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Network Manager Chat"
prefix = "networkmanager-chat"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelMessageResponse = Action("CancelMessageResponse")
CreateConversation = Action("CreateConversation")
DeleteConversation = Action("DeleteConversation")
ListConversationMessages = Action("ListConversationMessages")
ListConversations = Action("ListConversations")
NotifyConversationIsActive = Action("NotifyConversationIsActive")
SendConversationMessage = Action("SendConversationMessage")
