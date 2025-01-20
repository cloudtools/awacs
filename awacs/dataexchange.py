# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Data Exchange"
prefix = "dataexchange"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptDataGrant = Action("AcceptDataGrant")
CancelJob = Action("CancelJob")
CreateAsset = Action("CreateAsset")
CreateDataGrant = Action("CreateDataGrant")
CreateDataSet = Action("CreateDataSet")
CreateEventAction = Action("CreateEventAction")
CreateJob = Action("CreateJob")
CreateRevision = Action("CreateRevision")
DeleteAsset = Action("DeleteAsset")
DeleteDataGrant = Action("DeleteDataGrant")
DeleteDataSet = Action("DeleteDataSet")
DeleteEventAction = Action("DeleteEventAction")
DeleteRevision = Action("DeleteRevision")
GetAsset = Action("GetAsset")
GetDataGrant = Action("GetDataGrant")
GetDataSet = Action("GetDataSet")
GetEventAction = Action("GetEventAction")
GetJob = Action("GetJob")
GetReceivedDataGrant = Action("GetReceivedDataGrant")
GetRevision = Action("GetRevision")
ListDataGrants = Action("ListDataGrants")
ListDataSetRevisions = Action("ListDataSetRevisions")
ListDataSets = Action("ListDataSets")
ListEventActions = Action("ListEventActions")
ListJobs = Action("ListJobs")
ListReceivedDataGrants = Action("ListReceivedDataGrants")
ListRevisionAssets = Action("ListRevisionAssets")
ListTagsForResource = Action("ListTagsForResource")
PublishDataSet = Action("PublishDataSet")
PublishToDataGrant = Action("PublishToDataGrant")
RevokeRevision = Action("RevokeRevision")
SendApiAsset = Action("SendApiAsset")
SendDataSetNotification = Action("SendDataSetNotification")
StartJob = Action("StartJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAsset = Action("UpdateAsset")
UpdateDataSet = Action("UpdateDataSet")
UpdateEventAction = Action("UpdateEventAction")
UpdateRevision = Action("UpdateRevision")
