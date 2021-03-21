# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lookout for Vision"
prefix = "lookoutvision"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDataset = Action("CreateDataset")
CreateModel = Action("CreateModel")
CreateProject = Action("CreateProject")
DeleteDataset = Action("DeleteDataset")
DeleteModel = Action("DeleteModel")
DeleteProject = Action("DeleteProject")
DescribeDataset = Action("DescribeDataset")
DescribeModel = Action("DescribeModel")
DescribeProject = Action("DescribeProject")
DescribeTrialDetection = Action("DescribeTrialDetection")
DetectAnomalies = Action("DetectAnomalies")
ListDatasetEntries = Action("ListDatasetEntries")
ListModels = Action("ListModels")
ListProjects = Action("ListProjects")
ListTagsForResource = Action("ListTagsForResource")
ListTrialDetections = Action("ListTrialDetections")
StartModel = Action("StartModel")
StartTrialDetection = Action("StartTrialDetection")
StopModel = Action("StopModel")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDatasetEntries = Action("UpdateDatasetEntries")
