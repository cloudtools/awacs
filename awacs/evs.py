# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic VMware Service"
prefix = "evs"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateEipToVlan = Action("AssociateEipToVlan")
CreateEnvironment = Action("CreateEnvironment")
CreateEnvironmentHost = Action("CreateEnvironmentHost")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteEnvironmentHost = Action("DeleteEnvironmentHost")
DisassociateEipFromVlan = Action("DisassociateEipFromVlan")
GetEnvironment = Action("GetEnvironment")
GetVersions = Action("GetVersions")
ListEnvironmentHosts = Action("ListEnvironmentHosts")
ListEnvironmentVlans = Action("ListEnvironmentVlans")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
