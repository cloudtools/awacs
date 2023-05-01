# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Firewall Manager"
prefix = "fms"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAdminAccount = Action("AssociateAdminAccount")
AssociateThirdPartyFirewall = Action("AssociateThirdPartyFirewall")
BatchAssociateResource = Action("BatchAssociateResource")
BatchDisassociateResource = Action("BatchDisassociateResource")
DeleteAppsList = Action("DeleteAppsList")
DeleteNotificationChannel = Action("DeleteNotificationChannel")
DeletePolicy = Action("DeletePolicy")
DeleteProtocolsList = Action("DeleteProtocolsList")
DeleteResourceSet = Action("DeleteResourceSet")
DisassociateAdminAccount = Action("DisassociateAdminAccount")
DisassociateThirdPartyFirewall = Action("DisassociateThirdPartyFirewall")
GetAdminAccount = Action("GetAdminAccount")
GetAdminScope = Action("GetAdminScope")
GetAppsList = Action("GetAppsList")
GetComplianceDetail = Action("GetComplianceDetail")
GetNotificationChannel = Action("GetNotificationChannel")
GetPolicy = Action("GetPolicy")
GetProtectionStatus = Action("GetProtectionStatus")
GetProtocolsList = Action("GetProtocolsList")
GetResourceSet = Action("GetResourceSet")
GetThirdPartyFirewallAssociationStatus = Action(
    "GetThirdPartyFirewallAssociationStatus"
)
GetViolationDetails = Action("GetViolationDetails")
ListAdminAccountsForOrganization = Action("ListAdminAccountsForOrganization")
ListAdminsManagingAccount = Action("ListAdminsManagingAccount")
ListAppsLists = Action("ListAppsLists")
ListComplianceStatus = Action("ListComplianceStatus")
ListDiscoveredResources = Action("ListDiscoveredResources")
ListMemberAccounts = Action("ListMemberAccounts")
ListPolicies = Action("ListPolicies")
ListProtocolsLists = Action("ListProtocolsLists")
ListResourceSetResources = Action("ListResourceSetResources")
ListResourceSets = Action("ListResourceSets")
ListTagsForResource = Action("ListTagsForResource")
ListThirdPartyFirewallFirewallPolicies = Action(
    "ListThirdPartyFirewallFirewallPolicies"
)
PutAdminAccount = Action("PutAdminAccount")
PutAppsList = Action("PutAppsList")
PutNotificationChannel = Action("PutNotificationChannel")
PutPolicy = Action("PutPolicy")
PutProtocolsList = Action("PutProtocolsList")
PutResourceSet = Action("PutResourceSet")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
