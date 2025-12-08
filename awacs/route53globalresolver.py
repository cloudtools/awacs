# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Route53 Global Resolver"
prefix = "route53globalresolver"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
AssociateHostedZone = Action("AssociateHostedZone")
BatchCreateFirewallRule = Action("BatchCreateFirewallRule")
BatchDeleteFirewallRule = Action("BatchDeleteFirewallRule")
BatchUpdateFirewallRule = Action("BatchUpdateFirewallRule")
CreateAccessSource = Action("CreateAccessSource")
CreateAccessToken = Action("CreateAccessToken")
CreateDNSView = Action("CreateDNSView")
CreateFirewallDomainList = Action("CreateFirewallDomainList")
CreateFirewallRule = Action("CreateFirewallRule")
CreateGlobalResolver = Action("CreateGlobalResolver")
DeleteAccessSource = Action("DeleteAccessSource")
DeleteAccessToken = Action("DeleteAccessToken")
DeleteDNSView = Action("DeleteDNSView")
DeleteFirewallDomainList = Action("DeleteFirewallDomainList")
DeleteFirewallRule = Action("DeleteFirewallRule")
DeleteGlobalResolver = Action("DeleteGlobalResolver")
DisableDNSView = Action("DisableDNSView")
DisassociateHostedZone = Action("DisassociateHostedZone")
EnableDNSView = Action("EnableDNSView")
GetAccessSource = Action("GetAccessSource")
GetAccessToken = Action("GetAccessToken")
GetDNSView = Action("GetDNSView")
GetFirewallDomainList = Action("GetFirewallDomainList")
GetFirewallRule = Action("GetFirewallRule")
GetGlobalResolver = Action("GetGlobalResolver")
GetHostedZoneAssociation = Action("GetHostedZoneAssociation")
GetManagedFirewallDomainList = Action("GetManagedFirewallDomainList")
ImportFirewallDomains = Action("ImportFirewallDomains")
ListAccessSources = Action("ListAccessSources")
ListAccessTokens = Action("ListAccessTokens")
ListDNSViews = Action("ListDNSViews")
ListFirewallDomainLists = Action("ListFirewallDomainLists")
ListFirewallDomains = Action("ListFirewallDomains")
ListFirewallRules = Action("ListFirewallRules")
ListGlobalResolvers = Action("ListGlobalResolvers")
ListHostedZoneAssociations = Action("ListHostedZoneAssociations")
ListManagedFirewallDomainLists = Action("ListManagedFirewallDomainLists")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessSource = Action("UpdateAccessSource")
UpdateAccessToken = Action("UpdateAccessToken")
UpdateDNSView = Action("UpdateDNSView")
UpdateFirewallDomains = Action("UpdateFirewallDomains")
UpdateFirewallRule = Action("UpdateFirewallRule")
UpdateGlobalResolver = Action("UpdateGlobalResolver")
UpdateHostedZoneAssociation = Action("UpdateHostedZoneAssociation")
