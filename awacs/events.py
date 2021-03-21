# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EventBridge"
prefix = "events"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateEventSource = Action("ActivateEventSource")
CancelReplay = Action("CancelReplay")
CreateApiDestination = Action("CreateApiDestination")
CreateArchive = Action("CreateArchive")
CreateConnection = Action("CreateConnection")
CreateEventBus = Action("CreateEventBus")
CreatePartnerEventSource = Action("CreatePartnerEventSource")
DeactivateEventSource = Action("DeactivateEventSource")
DeauthorizeConnection = Action("DeauthorizeConnection")
DeleteApiDestination = Action("DeleteApiDestination")
DeleteArchive = Action("DeleteArchive")
DeleteConnection = Action("DeleteConnection")
DeleteEventBus = Action("DeleteEventBus")
DeletePartnerEventSource = Action("DeletePartnerEventSource")
DeleteRule = Action("DeleteRule")
DescribeApiDestination = Action("DescribeApiDestination")
DescribeArchive = Action("DescribeArchive")
DescribeConnection = Action("DescribeConnection")
DescribeEventBus = Action("DescribeEventBus")
DescribeEventSource = Action("DescribeEventSource")
DescribePartnerEventSource = Action("DescribePartnerEventSource")
DescribeReplay = Action("DescribeReplay")
DescribeRule = Action("DescribeRule")
DisableRule = Action("DisableRule")
EnableRule = Action("EnableRule")
InvokeApiDestination = Action("InvokeApiDestination")
ListApiDestinations = Action("ListApiDestinations")
ListArchives = Action("ListArchives")
ListConnections = Action("ListConnections")
ListEventBuses = Action("ListEventBuses")
ListEventSources = Action("ListEventSources")
ListPartnerEventSourceAccounts = Action("ListPartnerEventSourceAccounts")
ListPartnerEventSources = Action("ListPartnerEventSources")
ListReplays = Action("ListReplays")
ListRuleNamesByTarget = Action("ListRuleNamesByTarget")
ListRules = Action("ListRules")
ListTagsForResource = Action("ListTagsForResource")
ListTargetsByRule = Action("ListTargetsByRule")
PutEvents = Action("PutEvents")
PutPartnerEvents = Action("PutPartnerEvents")
PutPermission = Action("PutPermission")
PutRule = Action("PutRule")
PutTargets = Action("PutTargets")
RemovePermission = Action("RemovePermission")
RemoveTargets = Action("RemoveTargets")
StartReplay = Action("StartReplay")
TagResource = Action("TagResource")
TestEventPattern = Action("TestEventPattern")
UntagResource = Action("UntagResource")
UpdateApiDestination = Action("UpdateApiDestination")
UpdateArchive = Action("UpdateArchive")
UpdateConnection = Action("UpdateConnection")
