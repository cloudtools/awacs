# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Multi-party approval"
prefix = "mpa"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelSession = Action("CancelSession")
CreateApprovalTeam = Action("CreateApprovalTeam")
CreateIdentitySource = Action("CreateIdentitySource")
DeleteIdentitySource = Action("DeleteIdentitySource")
DeleteInactiveApprovalTeamVersion = Action("DeleteInactiveApprovalTeamVersion")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
GetApprovalTeam = Action("GetApprovalTeam")
GetIdentitySource = Action("GetIdentitySource")
GetPolicyVersion = Action("GetPolicyVersion")
GetResourcePolicy = Action("GetResourcePolicy")
GetSession = Action("GetSession")
ListApprovalTeams = Action("ListApprovalTeams")
ListIdentitySources = Action("ListIdentitySources")
ListPolicies = Action("ListPolicies")
ListPolicyVersions = Action("ListPolicyVersions")
ListResourcePolicies = Action("ListResourcePolicies")
ListSessions = Action("ListSessions")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
StartActiveApprovalTeamDeletion = Action("StartActiveApprovalTeamDeletion")
StartSession = Action("StartSession")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApprovalTeam = Action("UpdateApprovalTeam")
