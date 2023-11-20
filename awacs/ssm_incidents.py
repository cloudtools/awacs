# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Systems Manager Incident Manager"
prefix = "ssm-incidents"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetIncidentFindings = Action("BatchGetIncidentFindings")
CreateReplicationSet = Action("CreateReplicationSet")
CreateResponsePlan = Action("CreateResponsePlan")
CreateTimelineEvent = Action("CreateTimelineEvent")
DeleteIncidentRecord = Action("DeleteIncidentRecord")
DeleteReplicationSet = Action("DeleteReplicationSet")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteResponsePlan = Action("DeleteResponsePlan")
DeleteTimelineEvent = Action("DeleteTimelineEvent")
GetIncidentRecord = Action("GetIncidentRecord")
GetReplicationSet = Action("GetReplicationSet")
GetResourcePolicies = Action("GetResourcePolicies")
GetResponsePlan = Action("GetResponsePlan")
GetTimelineEvent = Action("GetTimelineEvent")
ListIncidentFindings = Action("ListIncidentFindings")
ListIncidentRecords = Action("ListIncidentRecords")
ListRelatedItems = Action("ListRelatedItems")
ListReplicationSets = Action("ListReplicationSets")
ListResponsePlans = Action("ListResponsePlans")
ListTagsForResource = Action("ListTagsForResource")
ListTimelineEvents = Action("ListTimelineEvents")
PutResourcePolicy = Action("PutResourcePolicy")
StartIncident = Action("StartIncident")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDeletionProtection = Action("UpdateDeletionProtection")
UpdateIncidentRecord = Action("UpdateIncidentRecord")
UpdateRelatedItems = Action("UpdateRelatedItems")
UpdateReplicationSet = Action("UpdateReplicationSet")
UpdateResponsePlan = Action("UpdateResponsePlan")
UpdateTimelineEvent = Action("UpdateTimelineEvent")
