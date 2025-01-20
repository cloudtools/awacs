# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaConvert"
prefix = "mediaconvert"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateCertificate = Action("AssociateCertificate")
CancelJob = Action("CancelJob")
CreateJob = Action("CreateJob")
CreateJobTemplate = Action("CreateJobTemplate")
CreatePreset = Action("CreatePreset")
CreateQueue = Action("CreateQueue")
DeleteJobTemplate = Action("DeleteJobTemplate")
DeletePolicy = Action("DeletePolicy")
DeletePreset = Action("DeletePreset")
DeleteQueue = Action("DeleteQueue")
DescribeEndpoint = Action("DescribeEndpoint")
DescribeEndpoints = Action("DescribeEndpoints")
DisassociateCertificate = Action("DisassociateCertificate")
GetJob = Action("GetJob")
GetJobTemplate = Action("GetJobTemplate")
GetPolicy = Action("GetPolicy")
GetPreset = Action("GetPreset")
GetQueue = Action("GetQueue")
ListJobTemplates = Action("ListJobTemplates")
ListJobs = Action("ListJobs")
ListPresets = Action("ListPresets")
ListQueues = Action("ListQueues")
ListTagsForResource = Action("ListTagsForResource")
ListVersions = Action("ListVersions")
PutPolicy = Action("PutPolicy")
SearchJobs = Action("SearchJobs")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateJobTemplate = Action("UpdateJobTemplate")
UpdatePreset = Action("UpdatePreset")
UpdateQueue = Action("UpdateQueue")
