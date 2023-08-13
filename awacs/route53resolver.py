# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Resolver"
prefix = "route53resolver"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFirewallRuleGroup = Action("AssociateFirewallRuleGroup")
AssociateResolverEndpointIpAddress = Action("AssociateResolverEndpointIpAddress")
AssociateResolverQueryLogConfig = Action("AssociateResolverQueryLogConfig")
AssociateResolverRule = Action("AssociateResolverRule")
CreateFirewallDomainList = Action("CreateFirewallDomainList")
CreateFirewallRule = Action("CreateFirewallRule")
CreateFirewallRuleGroup = Action("CreateFirewallRuleGroup")
CreateOutpostResolver = Action("CreateOutpostResolver")
CreateResolverEndpoint = Action("CreateResolverEndpoint")
CreateResolverQueryLogConfig = Action("CreateResolverQueryLogConfig")
CreateResolverRule = Action("CreateResolverRule")
DeleteFirewallDomainList = Action("DeleteFirewallDomainList")
DeleteFirewallRule = Action("DeleteFirewallRule")
DeleteFirewallRuleGroup = Action("DeleteFirewallRuleGroup")
DeleteOutpostResolver = Action("DeleteOutpostResolver")
DeleteResolverEndpoint = Action("DeleteResolverEndpoint")
DeleteResolverQueryLogConfig = Action("DeleteResolverQueryLogConfig")
DeleteResolverRule = Action("DeleteResolverRule")
DisassociateFirewallRuleGroup = Action("DisassociateFirewallRuleGroup")
DisassociateResolverEndpointIpAddress = Action("DisassociateResolverEndpointIpAddress")
DisassociateResolverQueryLogConfig = Action("DisassociateResolverQueryLogConfig")
DisassociateResolverRule = Action("DisassociateResolverRule")
GetFirewallConfig = Action("GetFirewallConfig")
GetFirewallDomainList = Action("GetFirewallDomainList")
GetFirewallRuleGroup = Action("GetFirewallRuleGroup")
GetFirewallRuleGroupAssociation = Action("GetFirewallRuleGroupAssociation")
GetFirewallRuleGroupPolicy = Action("GetFirewallRuleGroupPolicy")
GetOutpostResolver = Action("GetOutpostResolver")
GetResolverConfig = Action("GetResolverConfig")
GetResolverDnssecConfig = Action("GetResolverDnssecConfig")
GetResolverEndpoint = Action("GetResolverEndpoint")
GetResolverQueryLogConfig = Action("GetResolverQueryLogConfig")
GetResolverQueryLogConfigAssociation = Action("GetResolverQueryLogConfigAssociation")
GetResolverQueryLogConfigPolicy = Action("GetResolverQueryLogConfigPolicy")
GetResolverRule = Action("GetResolverRule")
GetResolverRuleAssociation = Action("GetResolverRuleAssociation")
GetResolverRulePolicy = Action("GetResolverRulePolicy")
ImportFirewallDomains = Action("ImportFirewallDomains")
ListFirewallConfigs = Action("ListFirewallConfigs")
ListFirewallDomainLists = Action("ListFirewallDomainLists")
ListFirewallDomains = Action("ListFirewallDomains")
ListFirewallRuleGroupAssociations = Action("ListFirewallRuleGroupAssociations")
ListFirewallRuleGroups = Action("ListFirewallRuleGroups")
ListFirewallRules = Action("ListFirewallRules")
ListOutpostResolvers = Action("ListOutpostResolvers")
ListResolverConfigs = Action("ListResolverConfigs")
ListResolverDnssecConfigs = Action("ListResolverDnssecConfigs")
ListResolverEndpointIpAddresses = Action("ListResolverEndpointIpAddresses")
ListResolverEndpoints = Action("ListResolverEndpoints")
ListResolverQueryLogConfigAssociations = Action(
    "ListResolverQueryLogConfigAssociations"
)
ListResolverQueryLogConfigs = Action("ListResolverQueryLogConfigs")
ListResolverRuleAssociations = Action("ListResolverRuleAssociations")
ListResolverRules = Action("ListResolverRules")
ListTagsForResource = Action("ListTagsForResource")
PutFirewallRuleGroupPolicy = Action("PutFirewallRuleGroupPolicy")
PutResolverQueryLogConfigPolicy = Action("PutResolverQueryLogConfigPolicy")
PutResolverRulePolicy = Action("PutResolverRulePolicy")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFirewallConfig = Action("UpdateFirewallConfig")
UpdateFirewallDomains = Action("UpdateFirewallDomains")
UpdateFirewallRule = Action("UpdateFirewallRule")
UpdateFirewallRuleGroupAssociation = Action("UpdateFirewallRuleGroupAssociation")
UpdateOutpostResolver = Action("UpdateOutpostResolver")
UpdateResolverConfig = Action("UpdateResolverConfig")
UpdateResolverDnssecConfig = Action("UpdateResolverDnssecConfig")
UpdateResolverEndpoint = Action("UpdateResolverEndpoint")
UpdateResolverRule = Action("UpdateResolverRule")
