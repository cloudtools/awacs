# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS rePost Private"
prefix = "repostspace"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchAddRole = Action("BatchAddRole")
BatchRemoveRole = Action("BatchRemoveRole")
CreateSpace = Action("CreateSpace")
DeleteSpace = Action("DeleteSpace")
DeregisterAdmin = Action("DeregisterAdmin")
GetSpace = Action("GetSpace")
ListSpaces = Action("ListSpaces")
ListTagsForResource = Action("ListTagsForResource")
RegisterAdmin = Action("RegisterAdmin")
SendInvites = Action("SendInvites")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateSpace = Action("UpdateSpace")
