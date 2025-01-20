# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS HealthLake"
prefix = "healthlake"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelFHIRExportJobWithDelete = Action("CancelFHIRExportJobWithDelete")
CreateFHIRDatastore = Action("CreateFHIRDatastore")
CreateResource = Action("CreateResource")
DeleteFHIRDatastore = Action("DeleteFHIRDatastore")
DeleteResource = Action("DeleteResource")
DescribeFHIRDatastore = Action("DescribeFHIRDatastore")
DescribeFHIRExportJob = Action("DescribeFHIRExportJob")
DescribeFHIRExportJobWithGet = Action("DescribeFHIRExportJobWithGet")
DescribeFHIRImportJob = Action("DescribeFHIRImportJob")
GetCapabilities = Action("GetCapabilities")
ListFHIRDatastores = Action("ListFHIRDatastores")
ListFHIRExportJobs = Action("ListFHIRExportJobs")
ListFHIRImportJobs = Action("ListFHIRImportJobs")
ListTagsForResource = Action("ListTagsForResource")
ReadResource = Action("ReadResource")
SearchEverything = Action("SearchEverything")
SearchWithGet = Action("SearchWithGet")
SearchWithPost = Action("SearchWithPost")
StartFHIRExportJob = Action("StartFHIRExportJob")
StartFHIRExportJobWithPost = Action("StartFHIRExportJobWithPost")
StartFHIRImportJob = Action("StartFHIRImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateResource = Action("UpdateResource")
