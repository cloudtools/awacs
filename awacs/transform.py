# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Transform"
prefix = "transform"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateConnectorResource = Action("AssociateConnectorResource")
CreateProfile = Action("CreateProfile")
DeleteProfile = Action("DeleteProfile")
GetConnector = Action("GetConnector")
ListProfiles = Action("ListProfiles")
RejectConnector = Action("RejectConnector")
UpdateProfile = Action("UpdateProfile")
