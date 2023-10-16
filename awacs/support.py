# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support"
prefix = "support"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddAttachmentsToSet = Action("AddAttachmentsToSet")
AddCommunicationToCase = Action("AddCommunicationToCase")
CreateCase = Action("CreateCase")
DescribeAttachment = Action("DescribeAttachment")
DescribeCaseAttributes = Action("DescribeCaseAttributes")
DescribeCases = Action("DescribeCases")
DescribeCommunication = Action("DescribeCommunication")
DescribeCommunications = Action("DescribeCommunications")
DescribeCreateCaseOptions = Action("DescribeCreateCaseOptions")
DescribeIssueTypes = Action("DescribeIssueTypes")
DescribeServices = Action("DescribeServices")
DescribeSeverityLevels = Action("DescribeSeverityLevels")
DescribeSupportLevel = Action("DescribeSupportLevel")
DescribeSupportedLanguages = Action("DescribeSupportedLanguages")
DescribeTrustedAdvisorCheckRefreshStatuses = Action(
    "DescribeTrustedAdvisorCheckRefreshStatuses"
)
DescribeTrustedAdvisorCheckResult = Action("DescribeTrustedAdvisorCheckResult")
DescribeTrustedAdvisorCheckSummaries = Action("DescribeTrustedAdvisorCheckSummaries")
DescribeTrustedAdvisorChecks = Action("DescribeTrustedAdvisorChecks")
InitiateCallForCase = Action("InitiateCallForCase")
InitiateChatForCase = Action("InitiateChatForCase")
PutCaseAttributes = Action("PutCaseAttributes")
RateCaseCommunication = Action("RateCaseCommunication")
RefreshTrustedAdvisorCheck = Action("RefreshTrustedAdvisorCheck")
ResolveCase = Action("ResolveCase")
SearchForCases = Action("SearchForCases")
