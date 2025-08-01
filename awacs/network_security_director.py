# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Shield network security director"
prefix = "network-security-director"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetFinding = Action("GetFinding")
GetNetworkSecurityScan = Action("GetNetworkSecurityScan")
GetResource = Action("GetResource")
ListFindings = Action("ListFindings")
ListInsights = Action("ListInsights")
ListRemediations = Action("ListRemediations")
ListResources = Action("ListResources")
StartNetworkSecurityScan = Action("StartNetworkSecurityScan")
UpdateFinding = Action("UpdateFinding")
