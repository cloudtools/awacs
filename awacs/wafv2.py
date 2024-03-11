# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS WAF V2"
prefix = "wafv2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateWebACL = Action("AssociateWebACL")
CheckCapacity = Action("CheckCapacity")
CreateAPIKey = Action("CreateAPIKey")
CreateIPSet = Action("CreateIPSet")
CreateRegexPatternSet = Action("CreateRegexPatternSet")
CreateRuleGroup = Action("CreateRuleGroup")
CreateWebACL = Action("CreateWebACL")
DeleteAPIKey = Action("DeleteAPIKey")
DeleteFirewallManagerRuleGroups = Action("DeleteFirewallManagerRuleGroups")
DeleteIPSet = Action("DeleteIPSet")
DeleteLoggingConfiguration = Action("DeleteLoggingConfiguration")
DeletePermissionPolicy = Action("DeletePermissionPolicy")
DeleteRegexPatternSet = Action("DeleteRegexPatternSet")
DeleteRuleGroup = Action("DeleteRuleGroup")
DeleteWebACL = Action("DeleteWebACL")
DescribeAllManagedProducts = Action("DescribeAllManagedProducts")
DescribeManagedProductsByVendor = Action("DescribeManagedProductsByVendor")
DescribeManagedRuleGroup = Action("DescribeManagedRuleGroup")
DisassociateFirewallManager = Action("DisassociateFirewallManager")
DisassociateWebACL = Action("DisassociateWebACL")
GenerateMobileSdkReleaseUrl = Action("GenerateMobileSdkReleaseUrl")
GetDecryptedAPIKey = Action("GetDecryptedAPIKey")
GetIPSet = Action("GetIPSet")
GetLoggingConfiguration = Action("GetLoggingConfiguration")
GetManagedRuleSet = Action("GetManagedRuleSet")
GetMobileSdkRelease = Action("GetMobileSdkRelease")
GetPermissionPolicy = Action("GetPermissionPolicy")
GetRateBasedStatementManagedKeys = Action("GetRateBasedStatementManagedKeys")
GetRegexPatternSet = Action("GetRegexPatternSet")
GetRuleGroup = Action("GetRuleGroup")
GetSampledRequests = Action("GetSampledRequests")
GetWebACL = Action("GetWebACL")
GetWebACLForResource = Action("GetWebACLForResource")
ListAPIKeys = Action("ListAPIKeys")
ListAvailableManagedRuleGroupVersions = Action("ListAvailableManagedRuleGroupVersions")
ListAvailableManagedRuleGroups = Action("ListAvailableManagedRuleGroups")
ListIPSets = Action("ListIPSets")
ListLoggingConfigurations = Action("ListLoggingConfigurations")
ListManagedRuleSets = Action("ListManagedRuleSets")
ListMobileSdkReleases = Action("ListMobileSdkReleases")
ListRegexPatternSets = Action("ListRegexPatternSets")
ListResourcesForWebACL = Action("ListResourcesForWebACL")
ListRuleGroups = Action("ListRuleGroups")
ListTagsForResource = Action("ListTagsForResource")
ListWebACLs = Action("ListWebACLs")
PutFirewallManagerRuleGroups = Action("PutFirewallManagerRuleGroups")
PutLoggingConfiguration = Action("PutLoggingConfiguration")
PutManagedRuleSetVersions = Action("PutManagedRuleSetVersions")
PutPermissionPolicy = Action("PutPermissionPolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateIPSet = Action("UpdateIPSet")
UpdateManagedRuleSetVersionExpiryDate = Action("UpdateManagedRuleSetVersionExpiryDate")
UpdateRegexPatternSet = Action("UpdateRegexPatternSet")
UpdateRuleGroup = Action("UpdateRuleGroup")
UpdateWebACL = Action("UpdateWebACL")
