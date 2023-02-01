# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Observability Access Manager"
prefix = "oam"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateLink = Action("CreateLink")
CreateSink = Action("CreateSink")
DeleteLink = Action("DeleteLink")
DeleteSink = Action("DeleteSink")
GetLink = Action("GetLink")
GetSink = Action("GetSink")
GetSinkPolicy = Action("GetSinkPolicy")
ListAttachedLinks = Action("ListAttachedLinks")
ListLinks = Action("ListLinks")
ListSinks = Action("ListSinks")
ListTagsForResource = Action("ListTagsForResource")
PutSinkPolicy = Action("PutSinkPolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLink = Action("UpdateLink")
