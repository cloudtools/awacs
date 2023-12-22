# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudTrail"
prefix = "cloudtrail"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTags = Action("AddTags")
CancelQuery = Action("CancelQuery")
CreateChannel = Action("CreateChannel")
CreateEventDataStore = Action("CreateEventDataStore")
CreateServiceLinkedChannel = Action("CreateServiceLinkedChannel")
CreateTrail = Action("CreateTrail")
DeleteChannel = Action("DeleteChannel")
DeleteEventDataStore = Action("DeleteEventDataStore")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteServiceLinkedChannel = Action("DeleteServiceLinkedChannel")
DeleteTrail = Action("DeleteTrail")
DeregisterOrganizationDelegatedAdmin = Action("DeregisterOrganizationDelegatedAdmin")
DescribeQuery = Action("DescribeQuery")
DescribeTrails = Action("DescribeTrails")
DisableFederation = Action("DisableFederation")
EnableFederation = Action("EnableFederation")
GetChannel = Action("GetChannel")
GetEventDataStore = Action("GetEventDataStore")
GetEventDataStoreData = Action("GetEventDataStoreData")
GetEventSelectors = Action("GetEventSelectors")
GetImport = Action("GetImport")
GetInsightSelectors = Action("GetInsightSelectors")
GetQueryResults = Action("GetQueryResults")
GetResourcePolicy = Action("GetResourcePolicy")
GetServiceLinkedChannel = Action("GetServiceLinkedChannel")
GetTrail = Action("GetTrail")
GetTrailStatus = Action("GetTrailStatus")
ListChannels = Action("ListChannels")
ListEventDataStores = Action("ListEventDataStores")
ListImportFailures = Action("ListImportFailures")
ListImports = Action("ListImports")
ListPublicKeys = Action("ListPublicKeys")
ListQueries = Action("ListQueries")
ListServiceLinkedChannels = Action("ListServiceLinkedChannels")
ListTags = Action("ListTags")
ListTrails = Action("ListTrails")
LookupEvents = Action("LookupEvents")
PutEventSelectors = Action("PutEventSelectors")
PutInsightSelectors = Action("PutInsightSelectors")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterOrganizationDelegatedAdmin = Action("RegisterOrganizationDelegatedAdmin")
RemoveTags = Action("RemoveTags")
RestoreEventDataStore = Action("RestoreEventDataStore")
StartEventDataStoreIngestion = Action("StartEventDataStoreIngestion")
StartImport = Action("StartImport")
StartLogging = Action("StartLogging")
StartQuery = Action("StartQuery")
StopEventDataStoreIngestion = Action("StopEventDataStoreIngestion")
StopImport = Action("StopImport")
StopLogging = Action("StopLogging")
UpdateChannel = Action("UpdateChannel")
UpdateEventDataStore = Action("UpdateEventDataStore")
UpdateServiceLinkedChannel = Action("UpdateServiceLinkedChannel")
UpdateTrail = Action("UpdateTrail")
