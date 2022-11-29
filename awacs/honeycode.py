# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Honeycode"
prefix = "honeycode"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ApproveTeamAssociation = Action("ApproveTeamAssociation")
BatchCreateTableRows = Action("BatchCreateTableRows")
BatchDeleteTableRows = Action("BatchDeleteTableRows")
BatchUpdateTableRows = Action("BatchUpdateTableRows")
BatchUpsertTableRows = Action("BatchUpsertTableRows")
CreateTeam = Action("CreateTeam")
CreateTenant = Action("CreateTenant")
DeleteDomains = Action("DeleteDomains")
DeregisterGroups = Action("DeregisterGroups")
DescribeTableDataImportJob = Action("DescribeTableDataImportJob")
DescribeTeam = Action("DescribeTeam")
GetScreenData = Action("GetScreenData")
InvokeScreenAutomation = Action("InvokeScreenAutomation")
ListDomains = Action("ListDomains")
ListGroups = Action("ListGroups")
ListTableColumns = Action("ListTableColumns")
ListTableRows = Action("ListTableRows")
ListTables = Action("ListTables")
ListTagsForResource = Action("ListTagsForResource")
ListTeamAssociations = Action("ListTeamAssociations")
ListTenants = Action("ListTenants")
QueryTableRows = Action("QueryTableRows")
RegisterDomainForVerification = Action("RegisterDomainForVerification")
RegisterGroups = Action("RegisterGroups")
RejectTeamAssociation = Action("RejectTeamAssociation")
RestartDomainVerification = Action("RestartDomainVerification")
StartTableDataImportJob = Action("StartTableDataImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTeam = Action("UpdateTeam")
