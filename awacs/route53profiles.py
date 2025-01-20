# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Profiles"
prefix = "route53profiles"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateProfile = Action("AssociateProfile")
AssociateResourceToProfile = Action("AssociateResourceToProfile")
CreateProfile = Action("CreateProfile")
DeleteProfile = Action("DeleteProfile")
DisassociateProfile = Action("DisassociateProfile")
DisassociateResourceFromProfile = Action("DisassociateResourceFromProfile")
GetProfile = Action("GetProfile")
GetProfileAssociation = Action("GetProfileAssociation")
GetProfilePolicy = Action("GetProfilePolicy")
GetProfileResourceAssociation = Action("GetProfileResourceAssociation")
ListProfileAssociations = Action("ListProfileAssociations")
ListProfileResourceAssociations = Action("ListProfileResourceAssociations")
ListProfiles = Action("ListProfiles")
ListTagsForResource = Action("ListTagsForResource")
PutProfilePolicy = Action("PutProfilePolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateProfileResourceAssociation = Action("UpdateProfileResourceAssociation")
