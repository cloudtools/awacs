# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Lookout for Equipment"
prefix = "lookoutequipment"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateDataset = Action("CreateDataset")
CreateInferenceScheduler = Action("CreateInferenceScheduler")
CreateLabel = Action("CreateLabel")
CreateLabelGroup = Action("CreateLabelGroup")
CreateModel = Action("CreateModel")
CreateRetrainingScheduler = Action("CreateRetrainingScheduler")
DeleteDataset = Action("DeleteDataset")
DeleteInferenceScheduler = Action("DeleteInferenceScheduler")
DeleteLabel = Action("DeleteLabel")
DeleteLabelGroup = Action("DeleteLabelGroup")
DeleteModel = Action("DeleteModel")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteRetrainingScheduler = Action("DeleteRetrainingScheduler")
DescribeDataIngestionJob = Action("DescribeDataIngestionJob")
DescribeDataset = Action("DescribeDataset")
DescribeInferenceScheduler = Action("DescribeInferenceScheduler")
DescribeLabelGroup = Action("DescribeLabelGroup")
DescribeModel = Action("DescribeModel")
DescribeModelVersion = Action("DescribeModelVersion")
DescribeResourcePolicy = Action("DescribeResourcePolicy")
DescribeRetrainingScheduler = Action("DescribeRetrainingScheduler")
Describelabel = Action("Describelabel")
ImportDataset = Action("ImportDataset")
ImportModelVersion = Action("ImportModelVersion")
ListDataIngestionJobs = Action("ListDataIngestionJobs")
ListDatasets = Action("ListDatasets")
ListInferenceEvents = Action("ListInferenceEvents")
ListInferenceExecutions = Action("ListInferenceExecutions")
ListInferenceSchedulers = Action("ListInferenceSchedulers")
ListLabelGroups = Action("ListLabelGroups")
ListLabels = Action("ListLabels")
ListModelVersions = Action("ListModelVersions")
ListModels = Action("ListModels")
ListRetrainingSchedulers = Action("ListRetrainingSchedulers")
ListSensorStatistics = Action("ListSensorStatistics")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
StartDataIngestionJob = Action("StartDataIngestionJob")
StartInferenceScheduler = Action("StartInferenceScheduler")
StartRetrainingScheduler = Action("StartRetrainingScheduler")
StopInferenceScheduler = Action("StopInferenceScheduler")
StopRetrainingScheduler = Action("StopRetrainingScheduler")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateActiveModelVersion = Action("UpdateActiveModelVersion")
UpdateInferenceScheduler = Action("UpdateInferenceScheduler")
UpdateLabelGroup = Action("UpdateLabelGroup")
UpdateModel = Action("UpdateModel")
UpdateRetrainingScheduler = Action("UpdateRetrainingScheduler")
