# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Translate"
prefix = "translate"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateParallelData = Action("CreateParallelData")
DeleteParallelData = Action("DeleteParallelData")
DeleteTerminology = Action("DeleteTerminology")
DescribeTextTranslationJob = Action("DescribeTextTranslationJob")
GetParallelData = Action("GetParallelData")
GetTerminology = Action("GetTerminology")
ImportTerminology = Action("ImportTerminology")
ListParallelData = Action("ListParallelData")
ListTerminologies = Action("ListTerminologies")
ListTextTranslationJobs = Action("ListTextTranslationJobs")
StartTextTranslationJob = Action("StartTextTranslationJob")
StopTextTranslationJob = Action("StopTextTranslationJob")
TranslateText = Action("TranslateText")
UpdateParallelData = Action("UpdateParallelData")
