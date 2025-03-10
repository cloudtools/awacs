# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon GameLift Streams"
prefix = "gameliftstreams"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddStreamGroupLocations = Action("AddStreamGroupLocations")
AssociateApplications = Action("AssociateApplications")
CreateApplication = Action("CreateApplication")
CreateStreamGroup = Action("CreateStreamGroup")
CreateStreamSessionConnection = Action("CreateStreamSessionConnection")
DeleteApplication = Action("DeleteApplication")
DeleteStreamGroup = Action("DeleteStreamGroup")
DisassociateApplications = Action("DisassociateApplications")
ExportStreamSessionFiles = Action("ExportStreamSessionFiles")
GetApplication = Action("GetApplication")
GetStreamGroup = Action("GetStreamGroup")
GetStreamSession = Action("GetStreamSession")
ListApplications = Action("ListApplications")
ListStreamGroups = Action("ListStreamGroups")
ListStreamSessions = Action("ListStreamSessions")
ListStreamSessionsByAccount = Action("ListStreamSessionsByAccount")
ListTagsForResource = Action("ListTagsForResource")
RemoveStreamGroupLocations = Action("RemoveStreamGroupLocations")
StartStreamSession = Action("StartStreamSession")
TagResource = Action("TagResource")
TerminateStreamSession = Action("TerminateStreamSession")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateStreamGroup = Action("UpdateStreamGroup")
