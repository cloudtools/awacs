# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Verified Permissions"
prefix = "verifiedpermissions"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateIdentitySource = Action("CreateIdentitySource")
CreatePolicy = Action("CreatePolicy")
CreatePolicyStore = Action("CreatePolicyStore")
CreatePolicyTemplate = Action("CreatePolicyTemplate")
DeleteIdentitySource = Action("DeleteIdentitySource")
DeletePolicy = Action("DeletePolicy")
DeletePolicyStore = Action("DeletePolicyStore")
DeletePolicyTemplate = Action("DeletePolicyTemplate")
GetIdentitySource = Action("GetIdentitySource")
GetPolicy = Action("GetPolicy")
GetPolicyStore = Action("GetPolicyStore")
GetPolicyTemplate = Action("GetPolicyTemplate")
GetSchema = Action("GetSchema")
IsAuthorized = Action("IsAuthorized")
IsAuthorizedWithToken = Action("IsAuthorizedWithToken")
ListIdentitySources = Action("ListIdentitySources")
ListPolicies = Action("ListPolicies")
ListPolicyStores = Action("ListPolicyStores")
ListPolicyTemplates = Action("ListPolicyTemplates")
PutSchema = Action("PutSchema")
UpdateIdentitySource = Action("UpdateIdentitySource")
UpdatePolicy = Action("UpdatePolicy")
UpdatePolicyStore = Action("UpdatePolicyStore")
UpdatePolicyTemplate = Action("UpdatePolicyTemplate")
