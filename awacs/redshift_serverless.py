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
CreateCustomDomainAssociation = Action("CreateCustomDomainAssociation")
CreateEndpointAccess = Action("CreateEndpointAccess")
CreateNamespace = Action("CreateNamespace")
CreateScheduledAction = Action("CreateScheduledAction")
CreateSnapshot = Action("CreateSnapshot")
CreateSnapshotCopyConfiguration = Action("CreateSnapshotCopyConfiguration")
CreateUsageLimit = Action("CreateUsageLimit")
CreateWorkgroup = Action("CreateWorkgroup")
DeleteCustomDomainAssociation = Action("DeleteCustomDomainAssociation")
DeleteEndpointAccess = Action("DeleteEndpointAccess")
DeleteNamespace = Action("DeleteNamespace")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteScheduledAction = Action("DeleteScheduledAction")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteSnapshotCopyConfiguration = Action("DeleteSnapshotCopyConfiguration")
DeleteUsageLimit = Action("DeleteUsageLimit")
DeleteWorkgroup = Action("DeleteWorkgroup")
DescribeOneTimeCredit = Action("DescribeOneTimeCredit")
GetCredentials = Action("GetCredentials")
GetCustomDomainAssociation = Action("GetCustomDomainAssociation")
GetEndpointAccess = Action("GetEndpointAccess")
GetManagedWorkgroup = Action("GetManagedWorkgroup")
GetNamespace = Action("GetNamespace")
GetRecoveryPoint = Action("GetRecoveryPoint")
GetResourcePolicy = Action("GetResourcePolicy")
GetScheduledAction = Action("GetScheduledAction")
GetSnapshot = Action("GetSnapshot")
GetTableRestoreStatus = Action("GetTableRestoreStatus")
GetUsageLimit = Action("GetUsageLimit")
GetWorkgroup = Action("GetWorkgroup")
ListCustomDomainAssociations = Action("ListCustomDomainAssociations")
ListEndpointAccess = Action("ListEndpointAccess")
ListManagedWorkgroups = Action("ListManagedWorkgroups")
ListNamespaces = Action("ListNamespaces")
ListRecoveryPoints = Action("ListRecoveryPoints")
ListScheduledActions = Action("ListScheduledActions")
ListSnapshotCopyConfigurations = Action("ListSnapshotCopyConfigurations")
ListSnapshots = Action("ListSnapshots")
ListTableRestoreStatus = Action("ListTableRestoreStatus")
ListTagsForResource = Action("ListTagsForResource")
ListUsageLimits = Action("ListUsageLimits")
ListWorkgroups = Action("ListWorkgroups")
PutResourcePolicy = Action("PutResourcePolicy")
RestoreFromRecoveryPoint = Action("RestoreFromRecoveryPoint")
RestoreFromSnapshot = Action("RestoreFromSnapshot")
RestoreTableFromRecoveryPoint = Action("RestoreTableFromRecoveryPoint")
RestoreTableFromSnapshot = Action("RestoreTableFromSnapshot")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCustomDomainAssociation = Action("UpdateCustomDomainAssociation")
UpdateEndpointAccess = Action("UpdateEndpointAccess")
UpdateNamespace = Action("UpdateNamespace")
UpdateScheduledAction = Action("UpdateScheduledAction")
UpdateSnapshot = Action("UpdateSnapshot")
UpdateSnapshotCopyConfiguration = Action("UpdateSnapshotCopyConfiguration")
UpdateUsageLimit = Action("UpdateUsageLimit")
UpdateWorkgroup = Action("UpdateWorkgroup")
