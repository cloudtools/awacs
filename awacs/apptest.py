# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Mainframe Modernization Application Testing"
prefix = "apptest"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateTestCase = Action("CreateTestCase")
CreateTestConfiguration = Action("CreateTestConfiguration")
CreateTestSuite = Action("CreateTestSuite")
DeleteTestCase = Action("DeleteTestCase")
DeleteTestConfiguration = Action("DeleteTestConfiguration")
DeleteTestRun = Action("DeleteTestRun")
DeleteTestSuite = Action("DeleteTestSuite")
GetTestCase = Action("GetTestCase")
GetTestConfiguration = Action("GetTestConfiguration")
GetTestRunStep = Action("GetTestRunStep")
GetTestSuite = Action("GetTestSuite")
ListTagsForResource = Action("ListTagsForResource")
ListTestCases = Action("ListTestCases")
ListTestConfigurations = Action("ListTestConfigurations")
ListTestRunSteps = Action("ListTestRunSteps")
ListTestRunTestCases = Action("ListTestRunTestCases")
ListTestRuns = Action("ListTestRuns")
ListTestSuites = Action("ListTestSuites")
StartTestRun = Action("StartTestRun")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTestCase = Action("UpdateTestCase")
UpdateTestConfiguration = Action("UpdateTestConfiguration")
UpdateTestSuite = Action("UpdateTestSuite")
