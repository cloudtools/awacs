# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudTrail"
prefix = "cloudtrail"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTags = Action("AddTags")
CancelQuery = Action("CancelQuery")
CreateEventDataStore = Action("CreateEventDataStore")
CreateServiceLinkedChannel = Action("CreateServiceLinkedChannel")
CreateTrail = Action("CreateTrail")
DeleteEventDataStore = Action("DeleteEventDataStore")
DeleteServiceLinkedChannel = Action("DeleteServiceLinkedChannel")
DeleteTrail = Action("DeleteTrail")
DescribeQuery = Action("DescribeQuery")
DescribeTrails = Action("DescribeTrails")
GetEventDataStore = Action("GetEventDataStore")
GetEventSelectors = Action("GetEventSelectors")
GetInsightSelectors = Action("GetInsightSelectors")
GetQueryResults = Action("GetQueryResults")
GetServiceLinkedChannel = Action("GetServiceLinkedChannel")
GetTrail = Action("GetTrail")
GetTrailStatus = Action("GetTrailStatus")
ListEventDataStores = Action("ListEventDataStores")
ListPublicKeys = Action("ListPublicKeys")
ListQueries = Action("ListQueries")
ListServiceLinkedChannels = Action("ListServiceLinkedChannels")
ListTags = Action("ListTags")
ListTrails = Action("ListTrails")
LookupEvents = Action("LookupEvents")
PutEventSelectors = Action("PutEventSelectors")
PutInsightSelectors = Action("PutInsightSelectors")
RemoveTags = Action("RemoveTags")
RestoreEventDataStore = Action("RestoreEventDataStore")
StartLogging = Action("StartLogging")
StartQuery = Action("StartQuery")
StopLogging = Action("StopLogging")
UpdateEventDataStore = Action("UpdateEventDataStore")
UpdateServiceLinkedChannel = Action("UpdateServiceLinkedChannel")
UpdateTrail = Action("UpdateTrail")
