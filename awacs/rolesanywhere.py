# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Identity and Access Management Roles Anywhere"
prefix = "rolesanywhere"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateProfile = Action("CreateProfile")
CreateTrustAnchor = Action("CreateTrustAnchor")
DeleteAttributeMapping = Action("DeleteAttributeMapping")
DeleteCrl = Action("DeleteCrl")
DeleteProfile = Action("DeleteProfile")
DeleteTrustAnchor = Action("DeleteTrustAnchor")
DisableCrl = Action("DisableCrl")
DisableProfile = Action("DisableProfile")
DisableTrustAnchor = Action("DisableTrustAnchor")
EnableCrl = Action("EnableCrl")
EnableProfile = Action("EnableProfile")
EnableTrustAnchor = Action("EnableTrustAnchor")
GetCrl = Action("GetCrl")
GetProfile = Action("GetProfile")
GetSubject = Action("GetSubject")
GetTrustAnchor = Action("GetTrustAnchor")
ImportCrl = Action("ImportCrl")
ListCrls = Action("ListCrls")
ListProfiles = Action("ListProfiles")
ListSubjects = Action("ListSubjects")
ListTagsForResource = Action("ListTagsForResource")
ListTrustAnchors = Action("ListTrustAnchors")
PutAttributeMapping = Action("PutAttributeMapping")
PutNotificationSettings = Action("PutNotificationSettings")
ResetNotificationSettings = Action("ResetNotificationSettings")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCrl = Action("UpdateCrl")
UpdateProfile = Action("UpdateProfile")
UpdateTrustAnchor = Action("UpdateTrustAnchor")
