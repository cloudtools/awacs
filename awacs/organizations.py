# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Organizations"
prefix = "organizations"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptHandshake = Action("AcceptHandshake")
AttachPolicy = Action("AttachPolicy")
CancelHandshake = Action("CancelHandshake")
CloseAccount = Action("CloseAccount")
CreateAccount = Action("CreateAccount")
CreateGovCloudAccount = Action("CreateGovCloudAccount")
CreateOrganization = Action("CreateOrganization")
CreateOrganizationalUnit = Action("CreateOrganizationalUnit")
CreatePolicy = Action("CreatePolicy")
DeclineHandshake = Action("DeclineHandshake")
DeleteOrganization = Action("DeleteOrganization")
DeleteOrganizationalUnit = Action("DeleteOrganizationalUnit")
DeletePolicy = Action("DeletePolicy")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeregisterDelegatedAdministrator = Action("DeregisterDelegatedAdministrator")
DescribeAccount = Action("DescribeAccount")
DescribeCreateAccountStatus = Action("DescribeCreateAccountStatus")
DescribeEffectivePolicy = Action("DescribeEffectivePolicy")
DescribeHandshake = Action("DescribeHandshake")
DescribeOrganization = Action("DescribeOrganization")
DescribeOrganizationalUnit = Action("DescribeOrganizationalUnit")
DescribePolicy = Action("DescribePolicy")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DetachPolicy = Action("DetachPolicy")
DisableAWSServiceAccess = Action("DisableAWSServiceAccess")
DisablePolicyType = Action("DisablePolicyType")
EnableAWSServiceAccess = Action("EnableAWSServiceAccess")
EnableAllFeatures = Action("EnableAllFeatures")
EnablePolicyType = Action("EnablePolicyType")
InviteAccountToOrganization = Action("InviteAccountToOrganization")
LeaveOrganization = Action("LeaveOrganization")
ListAWSServiceAccessForOrganization = Action("ListAWSServiceAccessForOrganization")
ListAccounts = Action("ListAccounts")
ListAccountsForParent = Action("ListAccountsForParent")
ListChildren = Action("ListChildren")
ListCreateAccountStatus = Action("ListCreateAccountStatus")
ListDelegatedAdministrators = Action("ListDelegatedAdministrators")
ListDelegatedServicesForAccount = Action("ListDelegatedServicesForAccount")
ListHandshakesForAccount = Action("ListHandshakesForAccount")
ListHandshakesForOrganization = Action("ListHandshakesForOrganization")
ListOrganizationalUnitsForParent = Action("ListOrganizationalUnitsForParent")
ListParents = Action("ListParents")
ListPolicies = Action("ListPolicies")
ListPoliciesForTarget = Action("ListPoliciesForTarget")
ListRoots = Action("ListRoots")
ListTagsForResource = Action("ListTagsForResource")
ListTargetsForPolicy = Action("ListTargetsForPolicy")
MoveAccount = Action("MoveAccount")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterDelegatedAdministrator = Action("RegisterDelegatedAdministrator")
RemoveAccountFromOrganization = Action("RemoveAccountFromOrganization")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateOrganizationalUnit = Action("UpdateOrganizationalUnit")
UpdatePolicy = Action("UpdatePolicy")
