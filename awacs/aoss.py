# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon OpenSearch Serverless"
prefix = "aoss"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


APIAccessAll = Action("APIAccessAll")
BatchGetCollection = Action("BatchGetCollection")
BatchGetEffectiveLifecyclePolicy = Action("BatchGetEffectiveLifecyclePolicy")
BatchGetLifecyclePolicy = Action("BatchGetLifecyclePolicy")
BatchGetVpcEndpoint = Action("BatchGetVpcEndpoint")
CreateAccessPolicy = Action("CreateAccessPolicy")
CreateCollection = Action("CreateCollection")
CreateLifecyclePolicy = Action("CreateLifecyclePolicy")
CreateSecurityConfig = Action("CreateSecurityConfig")
CreateSecurityPolicy = Action("CreateSecurityPolicy")
CreateVpcEndpoint = Action("CreateVpcEndpoint")
DashboardsAccessAll = Action("DashboardsAccessAll")
DeleteAccessPolicy = Action("DeleteAccessPolicy")
DeleteCollection = Action("DeleteCollection")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
DeleteSecurityConfig = Action("DeleteSecurityConfig")
DeleteSecurityPolicy = Action("DeleteSecurityPolicy")
DeleteVpcEndpoint = Action("DeleteVpcEndpoint")
GetAccessPolicy = Action("GetAccessPolicy")
GetAccountSettings = Action("GetAccountSettings")
GetPoliciesStats = Action("GetPoliciesStats")
GetSecurityConfig = Action("GetSecurityConfig")
GetSecurityPolicy = Action("GetSecurityPolicy")
ListAccessPolicies = Action("ListAccessPolicies")
ListCollections = Action("ListCollections")
ListLifecyclePolicies = Action("ListLifecyclePolicies")
ListSecurityConfigs = Action("ListSecurityConfigs")
ListSecurityPolicies = Action("ListSecurityPolicies")
ListTagsForResource = Action("ListTagsForResource")
ListVpcEndpoints = Action("ListVpcEndpoints")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessPolicy = Action("UpdateAccessPolicy")
UpdateAccountSettings = Action("UpdateAccountSettings")
UpdateCollection = Action("UpdateCollection")
UpdateLifecyclePolicy = Action("UpdateLifecyclePolicy")
UpdateSecurityConfig = Action("UpdateSecurityConfig")
UpdateSecurityPolicy = Action("UpdateSecurityPolicy")
UpdateVpcEndpoint = Action("UpdateVpcEndpoint")
