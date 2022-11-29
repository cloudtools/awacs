# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Events"
prefix = "iotevents"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchAcknowledgeAlarm = Action("BatchAcknowledgeAlarm")
BatchDeleteDetector = Action("BatchDeleteDetector")
BatchDisableAlarm = Action("BatchDisableAlarm")
BatchEnableAlarm = Action("BatchEnableAlarm")
BatchPutMessage = Action("BatchPutMessage")
BatchResetAlarm = Action("BatchResetAlarm")
BatchSnoozeAlarm = Action("BatchSnoozeAlarm")
BatchUpdateDetector = Action("BatchUpdateDetector")
CreateAlarmModel = Action("CreateAlarmModel")
CreateDetectorModel = Action("CreateDetectorModel")
CreateInput = Action("CreateInput")
DeleteAlarmModel = Action("DeleteAlarmModel")
DeleteDetectorModel = Action("DeleteDetectorModel")
DeleteInput = Action("DeleteInput")
DescribeAlarm = Action("DescribeAlarm")
DescribeAlarmModel = Action("DescribeAlarmModel")
DescribeDetector = Action("DescribeDetector")
DescribeDetectorModel = Action("DescribeDetectorModel")
DescribeDetectorModelAnalysis = Action("DescribeDetectorModelAnalysis")
DescribeInput = Action("DescribeInput")
DescribeLoggingOptions = Action("DescribeLoggingOptions")
GetDetectorModelAnalysisResults = Action("GetDetectorModelAnalysisResults")
ListAlarmModelVersions = Action("ListAlarmModelVersions")
ListAlarmModels = Action("ListAlarmModels")
ListAlarms = Action("ListAlarms")
ListDetectorModelVersions = Action("ListDetectorModelVersions")
ListDetectorModels = Action("ListDetectorModels")
ListDetectors = Action("ListDetectors")
ListInputRoutings = Action("ListInputRoutings")
ListInputs = Action("ListInputs")
ListTagsForResource = Action("ListTagsForResource")
PutLoggingOptions = Action("PutLoggingOptions")
StartDetectorModelAnalysis = Action("StartDetectorModelAnalysis")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAlarmModel = Action("UpdateAlarmModel")
UpdateDetectorModel = Action("UpdateDetectorModel")
UpdateInput = Action("UpdateInput")
UpdateInputRouting = Action("UpdateInputRouting")
