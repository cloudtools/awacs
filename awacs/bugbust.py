# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS BugBust"
prefix = "bugbust"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateEvent = Action("CreateEvent")
EvaluateProfilingGroups = Action("EvaluateProfilingGroups")
GetEvent = Action("GetEvent")
GetJoinEventStatus = Action("GetJoinEventStatus")
JoinEvent = Action("JoinEvent")
ListBugs = Action("ListBugs")
ListEventParticipants = Action("ListEventParticipants")
ListEventScores = Action("ListEventScores")
ListEvents = Action("ListEvents")
ListProfilingGroups = Action("ListProfilingGroups")
ListPullRequests = Action("ListPullRequests")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEvent = Action("UpdateEvent")
UpdateWorkItem = Action("UpdateWorkItem")
UpdateWorkItemAdmin = Action("UpdateWorkItemAdmin")
