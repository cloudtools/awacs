# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Redshift Serverless"
prefix = "redshift-serverless"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ConvertRecoveryPointToSnapshot = Action("ConvertRecoveryPointToSnapshot")
CreateEndpointAccess = Action("CreateEndpointAccess")
CreateNamespace = Action("CreateNamespace")
CreateSnapshot = Action("CreateSnapshot")
CreateUsageLimit = Action("CreateUsageLimit")
CreateWorkgroup = Action("CreateWorkgroup")
DeleteEndpointAccess = Action("DeleteEndpointAccess")
DeleteNamespace = Action("DeleteNamespace")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteUsageLimit = Action("DeleteUsageLimit")
DeleteWorkgroup = Action("DeleteWorkgroup")
GetCredentials = Action("GetCredentials")
GetEndpointAccess = Action("GetEndpointAccess")
GetNamespace = Action("GetNamespace")
GetRecoveryPoint = Action("GetRecoveryPoint")
GetResourcePolicy = Action("GetResourcePolicy")
GetSnapshot = Action("GetSnapshot")
GetTableRestoreStatus = Action("GetTableRestoreStatus")
GetUsageLimit = Action("GetUsageLimit")
GetWorkgroup = Action("GetWorkgroup")
ListEndpointAccess = Action("ListEndpointAccess")
ListNamespaces = Action("ListNamespaces")
ListRecoveryPoints = Action("ListRecoveryPoints")
ListSnapshots = Action("ListSnapshots")
ListTableRestoreStatus = Action("ListTableRestoreStatus")
ListTagsForResource = Action("ListTagsForResource")
ListUsageLimits = Action("ListUsageLimits")
ListWorkgroups = Action("ListWorkgroups")
PutResourcePolicy = Action("PutResourcePolicy")
RestoreFromRecoveryPoint = Action("RestoreFromRecoveryPoint")
RestoreFromSnapshot = Action("RestoreFromSnapshot")
RestoreTableFromSnapshot = Action("RestoreTableFromSnapshot")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEndpointAccess = Action("UpdateEndpointAccess")
UpdateNamespace = Action("UpdateNamespace")
UpdateSnapshot = Action("UpdateSnapshot")
UpdateUsageLimit = Action("UpdateUsageLimit")
UpdateWorkgroup = Action("UpdateWorkgroup")
