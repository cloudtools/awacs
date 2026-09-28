# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EventBridge"
prefix = "events"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateEventSource = Action("ActivateEventSource")
AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
CancelReplay = Action("CancelReplay")
CreateApiDestination = Action("CreateApiDestination")
CreateArchive = Action("CreateArchive")
CreateConnection = Action("CreateConnection")
CreateEndpoint = Action("CreateEndpoint")
CreateEventBus = Action("CreateEventBus")
CreateEventSource = Action("CreateEventSource")
CreatePartnerEventSource = Action("CreatePartnerEventSource")
CreateSubscriber = Action("CreateSubscriber")
DeactivateEventSource = Action("DeactivateEventSource")
DeauthorizeConnection = Action("DeauthorizeConnection")
DeleteApiDestination = Action("DeleteApiDestination")
DeleteArchive = Action("DeleteArchive")
DeleteConnection = Action("DeleteConnection")
DeleteEndpoint = Action("DeleteEndpoint")
DeleteEventBus = Action("DeleteEventBus")
DeleteEventSource = Action("DeleteEventSource")
DeletePartnerEventSource = Action("DeletePartnerEventSource")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRule = Action("DeleteRule")
DeleteSubscriber = Action("DeleteSubscriber")
DescribeApiDestination = Action("DescribeApiDestination")
DescribeArchive = Action("DescribeArchive")
DescribeConnection = Action("DescribeConnection")
DescribeEndpoint = Action("DescribeEndpoint")
DescribeEventBus = Action("DescribeEventBus")
DescribeEventSource = Action("DescribeEventSource")
DescribePartnerEventSource = Action("DescribePartnerEventSource")
DescribeReplay = Action("DescribeReplay")
DescribeRule = Action("DescribeRule")
DescribeSubscriber = Action("DescribeSubscriber")
DisableRule = Action("DisableRule")
EnableRule = Action("EnableRule")
GetResourcePolicy = Action("GetResourcePolicy")
InvokeApiDestination = Action("InvokeApiDestination")
ListApiDestinations = Action("ListApiDestinations")
ListArchives = Action("ListArchives")
ListConnections = Action("ListConnections")
ListEndpoints = Action("ListEndpoints")
ListEventBuses = Action("ListEventBuses")
ListEventSources = Action("ListEventSources")
ListPartnerEventSourceAccounts = Action("ListPartnerEventSourceAccounts")
ListPartnerEventSources = Action("ListPartnerEventSources")
ListReplays = Action("ListReplays")
ListResourcePolicies = Action("ListResourcePolicies")
ListRuleNamesByTarget = Action("ListRuleNamesByTarget")
ListRules = Action("ListRules")
ListSubscribers = Action("ListSubscribers")
ListTagsForResource = Action("ListTagsForResource")
ListTargetsByRule = Action("ListTargetsByRule")
PutEvents = Action("PutEvents")
PutPartnerEvents = Action("PutPartnerEvents")
PutPermission = Action("PutPermission")
PutRawEvents = Action("PutRawEvents")
PutResourcePolicy = Action("PutResourcePolicy")
PutRule = Action("PutRule")
PutTargets = Action("PutTargets")
RemovePermission = Action("RemovePermission")
RemoveTargets = Action("RemoveTargets")
RetrieveConnectionCredentials = Action("RetrieveConnectionCredentials")
RevokeResource = Action("RevokeResource")
StartReplay = Action("StartReplay")
TagResource = Action("TagResource")
TestEventPattern = Action("TestEventPattern")
UntagResource = Action("UntagResource")
UpdateApiDestination = Action("UpdateApiDestination")
UpdateArchive = Action("UpdateArchive")
UpdateConnection = Action("UpdateConnection")
UpdateEndpoint = Action("UpdateEndpoint")
UpdateEventBus = Action("UpdateEventBus")
UpdateEventSource = Action("UpdateEventSource")
UpdateSubscriber = Action("UpdateSubscriber")
