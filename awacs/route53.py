# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, BaseARN

service_name = 'Amazon Route 53'
prefix = 'route53'


class ARN(BaseARN):
    def __init__(self, resource="*"):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource)


class Route53Action(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


AssociateVPCWithHostedZone = Route53Action("AssociateVPCWithHostedZone")
ChangeResourceRecordSets = Route53Action("ChangeResourceRecordSets")
ChangeTagsForResource = Route53Action("ChangeTagsForResource")
CreateHealthCheck = Route53Action("CreateHealthCheck")
CreateHostedZone = Route53Action("CreateHostedZone")
CreateReusableDelegationSet = Route53Action("CreateReusableDelegationSet")
DeleteHealthCheck = Route53Action("DeleteHealthCheck")
DeleteHostedZone = Route53Action("DeleteHostedZone")
DeleteReusableDelegationSet = Route53Action("DeleteReusableDelegationSet")
DisassociateVPCFromHostedZone = Route53Action("DisassociateVPCFromHostedZone")
GetChange = Route53Action("GetChange")
GetCheckerIpRanges = Route53Action("GetCheckerIpRanges")
GetGeoLocation = Route53Action("GetGeoLocation")
GetHealthCheck = Route53Action("GetHealthCheck")
GetHealthCheckCount = Route53Action("GetHealthCheckCount")
GetHealthCheckLastFailureReason = \
    Route53Action("GetHealthCheckLastFailureReason")
GetHealthCheckStatus = Route53Action("GetHealthCheckStatus")
GetHostedZone = Route53Action("GetHostedZone")
GetHostedZoneCount = Route53Action("GetHostedZoneCount")
GetReusableDelegationSet = Route53Action("GetReusableDelegationSet")
ListGeoLocations = Route53Action("ListGeoLocations")
ListHealthChecks = Route53Action("ListHealthChecks")
ListHostedZones = Route53Action("ListHostedZones")
ListHostedZonesByName = Route53Action("ListHostedZonesByName")
ListOperations = Route53Action("ListOperations")
ListResourceRecordSets = Route53Action("ListResourceRecordSets")
ListReusableDelegationSets = Route53Action("ListReusableDelegationSets")
ListTagsForResource = Route53Action("ListTagsForResource")
ListTagsForResources = Route53Action("ListTagsForResources")
UpdateHealthCheck = Route53Action("UpdateHealthCheck")
UpdateHostedZoneComment = Route53Action("UpdateHostedZoneComment")
