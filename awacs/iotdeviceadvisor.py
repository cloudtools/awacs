# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT Core Device Advisor"
prefix = "iotdeviceadvisor"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSuiteDefinition = Action("CreateSuiteDefinition")
DeleteSuiteDefinition = Action("DeleteSuiteDefinition")
GetEndpoint = Action("GetEndpoint")
GetSuiteDefinition = Action("GetSuiteDefinition")
GetSuiteRun = Action("GetSuiteRun")
GetSuiteRunReport = Action("GetSuiteRunReport")
ListSuiteDefinitions = Action("ListSuiteDefinitions")
ListSuiteRuns = Action("ListSuiteRuns")
ListTagsForResource = Action("ListTagsForResource")
ListTestCases = Action("ListTestCases")
StartSuiteRun = Action("StartSuiteRun")
StopSuiteRun = Action("StopSuiteRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateSuiteDefinition = Action("UpdateSuiteDefinition")
