# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Signin"
prefix = "signin"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


Authenticate = Action("Authenticate")
AuthorizeOAuth2Access = Action("AuthorizeOAuth2Access")
CreateAccount = Action("CreateAccount")
CreateOAuth2Token = Action("CreateOAuth2Token")
CreateTrustedIdentityPropagationApplicationForConsole = Action(
    "CreateTrustedIdentityPropagationApplicationForConsole"
)
DeleteConsoleAuthorizationConfiguration = Action(
    "DeleteConsoleAuthorizationConfiguration"
)
DeleteResourcePermissionStatement = Action("DeleteResourcePermissionStatement")
GetConsoleAuthorizationConfiguration = Action("GetConsoleAuthorizationConfiguration")
GetResourcePolicy = Action("GetResourcePolicy")
ListResourcePermissionStatements = Action("ListResourcePermissionStatements")
ListTrustedIdentityPropagationApplicationsForConsole = Action(
    "ListTrustedIdentityPropagationApplicationsForConsole"
)
PutConsoleAuthorizationConfiguration = Action("PutConsoleAuthorizationConfiguration")
PutResourcePermissionStatement = Action("PutResourcePermissionStatement")
