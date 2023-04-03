# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon DataZone Control"
prefix = "datazonecontrol"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAccountAssociationInvitation = Action("CreateAccountAssociationInvitation")
CreateDataSource = Action("CreateDataSource")
CreateEnvironment = Action("CreateEnvironment")
DeleteDataSource = Action("DeleteDataSource")
DeleteEnvironment = Action("DeleteEnvironment")
DissociateAccount = Action("DissociateAccount")
GetAssociatedDomain = Action("GetAssociatedDomain")
GetDataSourceByEnvironment = Action("GetDataSourceByEnvironment")
GetDomain = Action("GetDomain")
GetEnvironment = Action("GetEnvironment")
GetMetadataCollector = Action("GetMetadataCollector")
GetUserPortalLoginAuthCode = Action("GetUserPortalLoginAuthCode")
ListAccountAssociationInvitations = Action("ListAccountAssociationInvitations")
ListAllAssociatedAccountsForEnvironment = Action(
    "ListAllAssociatedAccountsForEnvironment"
)
ListAssociatedEnvironments = Action("ListAssociatedEnvironments")
ListDataSources = Action("ListDataSources")
ListDataSourcesByEnvironment = Action("ListDataSourcesByEnvironment")
ListDomains = Action("ListDomains")
ListEnvironment = Action("ListEnvironment")
ListMetadataCollectorRuns = Action("ListMetadataCollectorRuns")
ListMetadataCollectors = Action("ListMetadataCollectors")
ListProjects = Action("ListProjects")
ListTagsForResource = Action("ListTagsForResource")
ReviewAccountAssociationInvitation = Action("ReviewAccountAssociationInvitation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountAssociationDescription = Action("UpdateAccountAssociationDescription")
UpdateDataSource = Action("UpdateDataSource")
UpdateEnvironment = Action("UpdateEnvironment")
