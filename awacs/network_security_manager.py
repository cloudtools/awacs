# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Network Security Manager"
prefix = "network-security-manager"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDeployment = Action("CreateDeployment")
CreateDeploymentSnapshot = Action("CreateDeploymentSnapshot")
CreatePolicy = Action("CreatePolicy")
CreatePolicySnapshot = Action("CreatePolicySnapshot")
CreateRule = Action("CreateRule")
CreateRuleSnapshot = Action("CreateRuleSnapshot")
CreateScope = Action("CreateScope")
CreateScopeSnapshot = Action("CreateScopeSnapshot")
CreateTemplate = Action("CreateTemplate")
CreateTemplateSnapshot = Action("CreateTemplateSnapshot")
DeleteAdminAccount = Action("DeleteAdminAccount")
DeleteDeployment = Action("DeleteDeployment")
DeletePolicy = Action("DeletePolicy")
DeleteRule = Action("DeleteRule")
DeleteScope = Action("DeleteScope")
DeleteTemplate = Action("DeleteTemplate")
GenerateRuleConfiguration = Action("GenerateRuleConfiguration")
GetAdminAccount = Action("GetAdminAccount")
GetDeployment = Action("GetDeployment")
GetPolicy = Action("GetPolicy")
GetRule = Action("GetRule")
GetScope = Action("GetScope")
GetTemplate = Action("GetTemplate")
ListAdminAccounts = Action("ListAdminAccounts")
ListAggregateResourceSynchronizationStatuses = Action(
    "ListAggregateResourceSynchronizationStatuses"
)
ListDeploymentSnapshots = Action("ListDeploymentSnapshots")
ListDeployments = Action("ListDeployments")
ListPolicies = Action("ListPolicies")
ListPolicySnapshots = Action("ListPolicySnapshots")
ListResourceAssociations = Action("ListResourceAssociations")
ListResourceSynchronizationStatuses = Action("ListResourceSynchronizationStatuses")
ListRuleSnapshots = Action("ListRuleSnapshots")
ListRules = Action("ListRules")
ListScopeSnapshots = Action("ListScopeSnapshots")
ListScopes = Action("ListScopes")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateSnapshots = Action("ListTemplateSnapshots")
ListTemplates = Action("ListTemplates")
PutAdminAccount = Action("PutAdminAccount")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDeployment = Action("UpdateDeployment")
UpdatePolicy = Action("UpdatePolicy")
UpdateRule = Action("UpdateRule")
UpdateScope = Action("UpdateScope")
UpdateTemplate = Action("UpdateTemplate")
