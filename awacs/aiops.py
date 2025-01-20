# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AI Operations"
prefix = "aiops"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateInvestigation = Action("CreateInvestigation")
CreateInvestigationEvent = Action("CreateInvestigationEvent")
CreateInvestigationGroup = Action("CreateInvestigationGroup")
CreateInvestigationResource = Action("CreateInvestigationResource")
DeleteInvestigation = Action("DeleteInvestigation")
DeleteInvestigationGroup = Action("DeleteInvestigationGroup")
DeleteInvestigationGroupPolicy = Action("DeleteInvestigationGroupPolicy")
GetInvestigation = Action("GetInvestigation")
GetInvestigationEvent = Action("GetInvestigationEvent")
GetInvestigationGroup = Action("GetInvestigationGroup")
GetInvestigationGroupPolicy = Action("GetInvestigationGroupPolicy")
GetInvestigationResource = Action("GetInvestigationResource")
ListInvestigationEvents = Action("ListInvestigationEvents")
ListInvestigationGroups = Action("ListInvestigationGroups")
ListInvestigations = Action("ListInvestigations")
ListTagsForResource = Action("ListTagsForResource")
PutInvestigationGroupPolicy = Action("PutInvestigationGroupPolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateInvestigation = Action("UpdateInvestigation")
UpdateInvestigationEvent = Action("UpdateInvestigationEvent")
UpdateInvestigationGroup = Action("UpdateInvestigationGroup")
