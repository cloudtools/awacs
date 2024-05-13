# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Systems Manager for SAP"
prefix = "ssm-sap"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BackupDatabase = Action("BackupDatabase")
DeleteResourcePermission = Action("DeleteResourcePermission")
DeregisterApplication = Action("DeregisterApplication")
GetApplication = Action("GetApplication")
GetComponent = Action("GetComponent")
GetDatabase = Action("GetDatabase")
GetOperation = Action("GetOperation")
GetResourcePermission = Action("GetResourcePermission")
ListApplications = Action("ListApplications")
ListComponents = Action("ListComponents")
ListDatabases = Action("ListDatabases")
ListOperationEvents = Action("ListOperationEvents")
ListOperations = Action("ListOperations")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePermission = Action("PutResourcePermission")
RegisterApplication = Action("RegisterApplication")
RestoreDatabase = Action("RestoreDatabase")
StartApplication = Action("StartApplication")
StartApplicationRefresh = Action("StartApplicationRefresh")
StopApplication = Action("StopApplication")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplicationSettings = Action("UpdateApplicationSettings")
UpdateHANABackupSettings = Action("UpdateHANABackupSettings")
