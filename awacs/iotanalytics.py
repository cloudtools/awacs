# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Analytics"
prefix = "iotanalytics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchPutMessage = Action("BatchPutMessage")
CancelPipelineReprocessing = Action("CancelPipelineReprocessing")
CreateChannel = Action("CreateChannel")
CreateDataset = Action("CreateDataset")
CreateDatasetContent = Action("CreateDatasetContent")
CreateDatastore = Action("CreateDatastore")
CreatePipeline = Action("CreatePipeline")
DeleteChannel = Action("DeleteChannel")
DeleteDataset = Action("DeleteDataset")
DeleteDatasetContent = Action("DeleteDatasetContent")
DeleteDatastore = Action("DeleteDatastore")
DeletePipeline = Action("DeletePipeline")
DescribeChannel = Action("DescribeChannel")
DescribeDataset = Action("DescribeDataset")
DescribeDatastore = Action("DescribeDatastore")
DescribeLoggingOptions = Action("DescribeLoggingOptions")
DescribePipeline = Action("DescribePipeline")
GetDatasetContent = Action("GetDatasetContent")
ListChannels = Action("ListChannels")
ListDatasetContents = Action("ListDatasetContents")
ListDatasets = Action("ListDatasets")
ListDatastores = Action("ListDatastores")
ListPipelines = Action("ListPipelines")
ListTagsForResource = Action("ListTagsForResource")
PutLoggingOptions = Action("PutLoggingOptions")
RunPipelineActivity = Action("RunPipelineActivity")
SampleChannelData = Action("SampleChannelData")
StartPipelineReprocessing = Action("StartPipelineReprocessing")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateChannel = Action("UpdateChannel")
UpdateDataset = Action("UpdateDataset")
UpdateDatastore = Action("UpdateDatastore")
UpdatePipeline = Action("UpdatePipeline")
