# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Data Exchange"
prefix = "dataexchange"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelJob = Action("CancelJob")
CreateAsset = Action("CreateAsset")
CreateDataSet = Action("CreateDataSet")
CreateEventAction = Action("CreateEventAction")
CreateJob = Action("CreateJob")
CreateRevision = Action("CreateRevision")
DeleteAsset = Action("DeleteAsset")
DeleteDataSet = Action("DeleteDataSet")
DeleteEventAction = Action("DeleteEventAction")
DeleteRevision = Action("DeleteRevision")
GetAsset = Action("GetAsset")
GetDataSet = Action("GetDataSet")
GetEventAction = Action("GetEventAction")
GetJob = Action("GetJob")
GetRevision = Action("GetRevision")
ListDataSetRevisions = Action("ListDataSetRevisions")
ListDataSets = Action("ListDataSets")
ListEventActions = Action("ListEventActions")
ListJobs = Action("ListJobs")
ListRevisionAssets = Action("ListRevisionAssets")
ListTagsForResource = Action("ListTagsForResource")
PublishDataSet = Action("PublishDataSet")
SendApiAsset = Action("SendApiAsset")
StartJob = Action("StartJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAsset = Action("UpdateAsset")
UpdateDataSet = Action("UpdateDataSet")
UpdateEventAction = Action("UpdateEventAction")
UpdateRevision = Action("UpdateRevision")
