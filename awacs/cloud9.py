# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Cloud9"
prefix = "cloud9"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateEC2Remote = Action("ActivateEC2Remote")
CreateEnvironmentEC2 = Action("CreateEnvironmentEC2")
CreateEnvironmentMembership = Action("CreateEnvironmentMembership")
CreateEnvironmentSSH = Action("CreateEnvironmentSSH")
CreateEnvironmentToken = Action("CreateEnvironmentToken")
DeleteEnvironment = Action("DeleteEnvironment")
DeleteEnvironmentMembership = Action("DeleteEnvironmentMembership")
DescribeEC2Remote = Action("DescribeEC2Remote")
DescribeEnvironmentMemberships = Action("DescribeEnvironmentMemberships")
DescribeEnvironmentStatus = Action("DescribeEnvironmentStatus")
DescribeEnvironments = Action("DescribeEnvironments")
DescribeSSHRemote = Action("DescribeSSHRemote")
GetEnvironmentConfig = Action("GetEnvironmentConfig")
GetEnvironmentSettings = Action("GetEnvironmentSettings")
GetMembershipSettings = Action("GetMembershipSettings")
GetMigrationExperiences = Action("GetMigrationExperiences")
GetUserPublicKey = Action("GetUserPublicKey")
GetUserSettings = Action("GetUserSettings")
ListEnvironments = Action("ListEnvironments")
ListTagsForResource = Action("ListTagsForResource")
ModifyTemporaryCredentialsOnEnvironmentEC2 = Action(
    "ModifyTemporaryCredentialsOnEnvironmentEC2"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEnvironment = Action("UpdateEnvironment")
UpdateEnvironmentMembership = Action("UpdateEnvironmentMembership")
UpdateEnvironmentSettings = Action("UpdateEnvironmentSettings")
UpdateMembershipSettings = Action("UpdateMembershipSettings")
UpdateSSHRemote = Action("UpdateSSHRemote")
UpdateUserSettings = Action("UpdateUserSettings")
ValidateEnvironmentName = Action("ValidateEnvironmentName")
