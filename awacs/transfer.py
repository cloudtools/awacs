# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Transfer for SFTP"
prefix = "transfer"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateServer = Action("CreateServer")
CreateUser = Action("CreateUser")
DeleteServer = Action("DeleteServer")
DeleteSshPublicKey = Action("DeleteSshPublicKey")
DeleteUser = Action("DeleteUser")
DescribeSecurityPolicy = Action("DescribeSecurityPolicy")
DescribeServer = Action("DescribeServer")
DescribeUser = Action("DescribeUser")
ImportSshPublicKey = Action("ImportSshPublicKey")
ListSecurityPolicies = Action("ListSecurityPolicies")
ListServers = Action("ListServers")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
StartServer = Action("StartServer")
StopServer = Action("StopServer")
TagResource = Action("TagResource")
TestIdentityProvider = Action("TestIdentityProvider")
UntagResource = Action("UntagResource")
UpdateServer = Action("UpdateServer")
UpdateUser = Action("UpdateUser")
