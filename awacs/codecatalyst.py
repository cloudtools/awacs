# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CodeCatalyst"
prefix = "codecatalyst"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptConnection = Action("AcceptConnection")
AssociateIamRoleToConnection = Action("AssociateIamRoleToConnection")
AssociateIdentityCenterApplicationToSpace = Action(
    "AssociateIdentityCenterApplicationToSpace"
)
AssociateIdentityToIdentityCenterApplication = Action(
    "AssociateIdentityToIdentityCenterApplication"
)
BatchAssociateIdentitiesToIdentityCenterApplication = Action(
    "BatchAssociateIdentitiesToIdentityCenterApplication"
)
BatchDisassociateIdentitiesFromIdentityCenterApplication = Action(
    "BatchDisassociateIdentitiesFromIdentityCenterApplication"
)
CreateIdentityCenterApplication = Action("CreateIdentityCenterApplication")
CreateSpace = Action("CreateSpace")
CreateSpaceAdminRoleAssignment = Action("CreateSpaceAdminRoleAssignment")
DeleteConnection = Action("DeleteConnection")
DeleteIdentityCenterApplication = Action("DeleteIdentityCenterApplication")
DisassociateIamRoleFromConnection = Action("DisassociateIamRoleFromConnection")
DisassociateIdentityCenterApplicationFromSpace = Action(
    "DisassociateIdentityCenterApplicationFromSpace"
)
DisassociateIdentityFromIdentityCenterApplication = Action(
    "DisassociateIdentityFromIdentityCenterApplication"
)
GetBillingAuthorization = Action("GetBillingAuthorization")
GetConnection = Action("GetConnection")
GetIdentityCenterApplication = Action("GetIdentityCenterApplication")
GetPendingConnection = Action("GetPendingConnection")
ListConnections = Action("ListConnections")
ListIamRolesForConnection = Action("ListIamRolesForConnection")
ListIdentityCenterApplications = Action("ListIdentityCenterApplications")
ListIdentityCenterApplicationsForSpace = Action(
    "ListIdentityCenterApplicationsForSpace"
)
ListSpacesForIdentityCenterApplication = Action(
    "ListSpacesForIdentityCenterApplication"
)
ListTagsForResource = Action("ListTagsForResource")
PutBillingAuthorization = Action("PutBillingAuthorization")
RejectConnection = Action("RejectConnection")
SynchronizeIdentityCenterApplication = Action("SynchronizeIdentityCenterApplication")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateIdentityCenterApplication = Action("UpdateIdentityCenterApplication")
