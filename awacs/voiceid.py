# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Voice ID"
prefix = "voiceid"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFraudster = Action("AssociateFraudster")
CreateDomain = Action("CreateDomain")
CreateWatchlist = Action("CreateWatchlist")
DeleteDomain = Action("DeleteDomain")
DeleteFraudster = Action("DeleteFraudster")
DeleteSpeaker = Action("DeleteSpeaker")
DeleteWatchlist = Action("DeleteWatchlist")
DescribeComplianceConsent = Action("DescribeComplianceConsent")
DescribeDomain = Action("DescribeDomain")
DescribeFraudster = Action("DescribeFraudster")
DescribeFraudsterRegistrationJob = Action("DescribeFraudsterRegistrationJob")
DescribeSpeaker = Action("DescribeSpeaker")
DescribeSpeakerEnrollmentJob = Action("DescribeSpeakerEnrollmentJob")
DescribeWatchlist = Action("DescribeWatchlist")
DisassociateFraudster = Action("DisassociateFraudster")
EvaluateSession = Action("EvaluateSession")
ListDomains = Action("ListDomains")
ListFraudsterRegistrationJobs = Action("ListFraudsterRegistrationJobs")
ListFraudsters = Action("ListFraudsters")
ListSpeakerEnrollmentJobs = Action("ListSpeakerEnrollmentJobs")
ListSpeakers = Action("ListSpeakers")
ListTagsForResource = Action("ListTagsForResource")
ListWatchlists = Action("ListWatchlists")
OptOutSpeaker = Action("OptOutSpeaker")
RegisterComplianceConsent = Action("RegisterComplianceConsent")
StartFraudsterRegistrationJob = Action("StartFraudsterRegistrationJob")
StartSpeakerEnrollmentJob = Action("StartSpeakerEnrollmentJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDomain = Action("UpdateDomain")
UpdateWatchlist = Action("UpdateWatchlist")
