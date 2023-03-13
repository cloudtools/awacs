# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Fraud Detector"
prefix = "frauddetector"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreateVariable = Action("BatchCreateVariable")
BatchGetVariable = Action("BatchGetVariable")
CancelBatchImportJob = Action("CancelBatchImportJob")
CancelBatchPredictionJob = Action("CancelBatchPredictionJob")
CreateBatchImportJob = Action("CreateBatchImportJob")
CreateBatchPredictionJob = Action("CreateBatchPredictionJob")
CreateDetectorVersion = Action("CreateDetectorVersion")
CreateList = Action("CreateList")
CreateModel = Action("CreateModel")
CreateModelVersion = Action("CreateModelVersion")
CreateRule = Action("CreateRule")
CreateVariable = Action("CreateVariable")
DeleteBatchImportJob = Action("DeleteBatchImportJob")
DeleteBatchPredictionJob = Action("DeleteBatchPredictionJob")
DeleteDetector = Action("DeleteDetector")
DeleteDetectorVersion = Action("DeleteDetectorVersion")
DeleteEntityType = Action("DeleteEntityType")
DeleteEvent = Action("DeleteEvent")
DeleteEventType = Action("DeleteEventType")
DeleteEventsByEventType = Action("DeleteEventsByEventType")
DeleteExternalModel = Action("DeleteExternalModel")
DeleteLabel = Action("DeleteLabel")
DeleteList = Action("DeleteList")
DeleteModel = Action("DeleteModel")
DeleteModelVersion = Action("DeleteModelVersion")
DeleteOutcome = Action("DeleteOutcome")
DeleteRule = Action("DeleteRule")
DeleteVariable = Action("DeleteVariable")
DescribeDetector = Action("DescribeDetector")
DescribeModelVersions = Action("DescribeModelVersions")
GetBatchImportJobValidationReport = Action("GetBatchImportJobValidationReport")
GetBatchImportJobs = Action("GetBatchImportJobs")
GetBatchPredictionJobs = Action("GetBatchPredictionJobs")
GetDeleteEventsByEventTypeStatus = Action("GetDeleteEventsByEventTypeStatus")
GetDetectorVersion = Action("GetDetectorVersion")
GetDetectors = Action("GetDetectors")
GetEntityTypes = Action("GetEntityTypes")
GetEvent = Action("GetEvent")
GetEventPrediction = Action("GetEventPrediction")
GetEventPredictionMetadata = Action("GetEventPredictionMetadata")
GetEventTypes = Action("GetEventTypes")
GetExternalModels = Action("GetExternalModels")
GetKMSEncryptionKey = Action("GetKMSEncryptionKey")
GetLabels = Action("GetLabels")
GetListElements = Action("GetListElements")
GetListsMetadata = Action("GetListsMetadata")
GetModelVersion = Action("GetModelVersion")
GetModels = Action("GetModels")
GetOutcomes = Action("GetOutcomes")
GetRules = Action("GetRules")
GetVariables = Action("GetVariables")
ListEventPredictions = Action("ListEventPredictions")
ListTagsForResource = Action("ListTagsForResource")
PutDetector = Action("PutDetector")
PutEntityType = Action("PutEntityType")
PutEventType = Action("PutEventType")
PutExternalModel = Action("PutExternalModel")
PutKMSEncryptionKey = Action("PutKMSEncryptionKey")
PutLabel = Action("PutLabel")
PutOutcome = Action("PutOutcome")
SendEvent = Action("SendEvent")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDetectorVersion = Action("UpdateDetectorVersion")
UpdateDetectorVersionMetadata = Action("UpdateDetectorVersionMetadata")
UpdateDetectorVersionStatus = Action("UpdateDetectorVersionStatus")
UpdateEventLabel = Action("UpdateEventLabel")
UpdateList = Action("UpdateList")
UpdateModel = Action("UpdateModel")
UpdateModelVersion = Action("UpdateModelVersion")
UpdateModelVersionStatus = Action("UpdateModelVersionStatus")
UpdateRuleMetadata = Action("UpdateRuleMetadata")
UpdateRuleVersion = Action("UpdateRuleVersion")
UpdateVariable = Action("UpdateVariable")
