# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Secrets Manager"
prefix = "secretsmanager"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetSecretValue = Action("BatchGetSecretValue")
CancelRotateSecret = Action("CancelRotateSecret")
CreateSecret = Action("CreateSecret")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteSecret = Action("DeleteSecret")
DescribeSecret = Action("DescribeSecret")
GetRandomPassword = Action("GetRandomPassword")
GetResourcePolicy = Action("GetResourcePolicy")
GetSecretValue = Action("GetSecretValue")
ListSecretVersionIds = Action("ListSecretVersionIds")
ListSecrets = Action("ListSecrets")
PutResourcePolicy = Action("PutResourcePolicy")
PutSecretValue = Action("PutSecretValue")
RemoveRegionsFromReplication = Action("RemoveRegionsFromReplication")
ReplicateSecretToRegions = Action("ReplicateSecretToRegions")
RestoreSecret = Action("RestoreSecret")
RotateSecret = Action("RotateSecret")
StopReplicationToReplica = Action("StopReplicationToReplica")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateSecret = Action("UpdateSecret")
UpdateSecretVersionStage = Action("UpdateSecretVersionStage")
ValidateResourcePolicy = Action("ValidateResourcePolicy")
