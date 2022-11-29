# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS OpsWorks Configuration Management"
prefix = "opsworks-cm"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateNode = Action("AssociateNode")
CreateBackup = Action("CreateBackup")
CreateServer = Action("CreateServer")
DeleteBackup = Action("DeleteBackup")
DeleteServer = Action("DeleteServer")
DescribeAccountAttributes = Action("DescribeAccountAttributes")
DescribeBackups = Action("DescribeBackups")
DescribeEvents = Action("DescribeEvents")
DescribeNodeAssociationStatus = Action("DescribeNodeAssociationStatus")
DescribeServers = Action("DescribeServers")
DisassociateNode = Action("DisassociateNode")
ExportServerEngineAttribute = Action("ExportServerEngineAttribute")
ListTagsForResource = Action("ListTagsForResource")
RestoreServer = Action("RestoreServer")
StartMaintenance = Action("StartMaintenance")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateServer = Action("UpdateServer")
UpdateServerEngineAttributes = Action("UpdateServerEngineAttributes")
