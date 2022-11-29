# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Comprehend Medical"
prefix = "comprehendmedical"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DescribeEntitiesDetectionV2Job = Action("DescribeEntitiesDetectionV2Job")
DescribeICD10CMInferenceJob = Action("DescribeICD10CMInferenceJob")
DescribePHIDetectionJob = Action("DescribePHIDetectionJob")
DescribeRxNormInferenceJob = Action("DescribeRxNormInferenceJob")
DescribeSNOMEDCTInferenceJob = Action("DescribeSNOMEDCTInferenceJob")
DetectEntities = Action("DetectEntities")
DetectEntitiesV2 = Action("DetectEntitiesV2")
DetectPHI = Action("DetectPHI")
InferICD10CM = Action("InferICD10CM")
InferRxNorm = Action("InferRxNorm")
InferSNOMEDCT = Action("InferSNOMEDCT")
ListEntitiesDetectionV2Jobs = Action("ListEntitiesDetectionV2Jobs")
ListICD10CMInferenceJobs = Action("ListICD10CMInferenceJobs")
ListPHIDetectionJobs = Action("ListPHIDetectionJobs")
ListRxNormInferenceJobs = Action("ListRxNormInferenceJobs")
ListSNOMEDCTInferenceJobs = Action("ListSNOMEDCTInferenceJobs")
StartEntitiesDetectionV2Job = Action("StartEntitiesDetectionV2Job")
StartICD10CMInferenceJob = Action("StartICD10CMInferenceJob")
StartPHIDetectionJob = Action("StartPHIDetectionJob")
StartRxNormInferenceJob = Action("StartRxNormInferenceJob")
StartSNOMEDCTInferenceJob = Action("StartSNOMEDCTInferenceJob")
StopEntitiesDetectionV2Job = Action("StopEntitiesDetectionV2Job")
StopICD10CMInferenceJob = Action("StopICD10CMInferenceJob")
StopPHIDetectionJob = Action("StopPHIDetectionJob")
StopRxNormInferenceJob = Action("StopRxNormInferenceJob")
StopSNOMEDCTInferenceJob = Action("StopSNOMEDCTInferenceJob")
