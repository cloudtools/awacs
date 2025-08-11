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


BatchAddChannelRoleToAccessors = Action("BatchAddChannelRoleToAccessors")
BatchAddRole = Action("BatchAddRole")
BatchRemoveChannelRoleFromAccessors = Action("BatchRemoveChannelRoleFromAccessors")
BatchRemoveRole = Action("BatchRemoveRole")
CreateChannel = Action("CreateChannel")
CreateSpace = Action("CreateSpace")
DeleteSpace = Action("DeleteSpace")
DeregisterAdmin = Action("DeregisterAdmin")
GetChannel = Action("GetChannel")
GetSpace = Action("GetSpace")
ListChannels = Action("ListChannels")
ListSpaces = Action("ListSpaces")
ListTagsForResource = Action("ListTagsForResource")
RegisterAdmin = Action("RegisterAdmin")
SendInvites = Action("SendInvites")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateSpace = Action("UpdateSpace")
