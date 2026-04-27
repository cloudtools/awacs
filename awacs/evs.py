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
CreateEntitlement = Action("CreateEntitlement")
CreateEnvironment = Action("CreateEnvironment")
CreateEnvironmentConnector = Action("CreateEnvironmentConnector")
CreateEnvironmentHost = Action("CreateEnvironmentHost")
DeleteEntitlement = Action("DeleteEntitlement")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteEnvironmentConnector = Action("DeleteEnvironmentConnector")
DeleteEnvironmentHost = Action("DeleteEnvironmentHost")
DisassociateEipFromVlan = Action("DisassociateEipFromVlan")
GetEnvironment = Action("GetEnvironment")
GetVersions = Action("GetVersions")
ListEnvironmentConnectors = Action("ListEnvironmentConnectors")
ListEnvironmentHosts = Action("ListEnvironmentHosts")
ListEnvironmentVlans = Action("ListEnvironmentVlans")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
ListVmEntitlements = Action("ListVmEntitlements")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEnvironmentConnector = Action("UpdateEnvironmentConnector")
