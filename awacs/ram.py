# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Resource Access Manager"
prefix = "ram"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptResourceShareInvitation = Action("AcceptResourceShareInvitation")
AssociateResourceShare = Action("AssociateResourceShare")
AssociateResourceSharePermission = Action("AssociateResourceSharePermission")
CreateResourceShare = Action("CreateResourceShare")
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
ListPermissions = Action("ListPermissions")
ListPrincipals = Action("ListPrincipals")
ListResourceSharePermissions = Action("ListResourceSharePermissions")
ListResourceTypes = Action("ListResourceTypes")
ListResources = Action("ListResources")
PromoteResourceShareCreatedFromPolicy = Action("PromoteResourceShareCreatedFromPolicy")
RejectResourceShareInvitation = Action("RejectResourceShareInvitation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateResourceShare = Action("UpdateResourceShare")
