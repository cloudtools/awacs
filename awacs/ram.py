# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Resource Access Manager (RAM)"
prefix = "ram"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptResourceShareInvitation = Action("AcceptResourceShareInvitation")
AssociateResourceShare = Action("AssociateResourceShare")
AssociateResourceSharePermission = Action("AssociateResourceSharePermission")
CreatePermission = Action("CreatePermission")
CreatePermissionVersion = Action("CreatePermissionVersion")
CreateResourceShare = Action("CreateResourceShare")
DeletePermission = Action("DeletePermission")
DeletePermissionVersion = Action("DeletePermissionVersion")
DeleteResourceShare = Action("DeleteResourceShare")
DisassociateResourceShare = Action("DisassociateResourceShare")
DisassociateResourceSharePermission = Action("DisassociateResourceSharePermission")
EnableSharingWithAwsOrganization = Action("EnableSharingWithAwsOrganization")
GetPermission = Action("GetPermission")
GetResourcePolicies = Action("GetResourcePolicies")
GetResourceShareAssociations = Action("GetResourceShareAssociations")
GetResourceShareInvitations = Action("GetResourceShareInvitations")
GetResourceShares = Action("GetResourceShares")
ListPendingInvitationResources = Action("ListPendingInvitationResources")
ListPermissionAssociations = Action("ListPermissionAssociations")
ListPermissionVersions = Action("ListPermissionVersions")
ListPermissions = Action("ListPermissions")
ListPrincipals = Action("ListPrincipals")
ListReplacePermissionAssociationsWork = Action("ListReplacePermissionAssociationsWork")
ListResourceSharePermissions = Action("ListResourceSharePermissions")
ListResourceTypes = Action("ListResourceTypes")
ListResources = Action("ListResources")
PromotePermissionCreatedFromPolicy = Action("PromotePermissionCreatedFromPolicy")
PromoteResourceShareCreatedFromPolicy = Action("PromoteResourceShareCreatedFromPolicy")
RejectResourceShareInvitation = Action("RejectResourceShareInvitation")
ReplacePermissionAssociations = Action("ReplacePermissionAssociations")
SetDefaultPermissionVersion = Action("SetDefaultPermissionVersion")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateResourceShare = Action("UpdateResourceShare")
