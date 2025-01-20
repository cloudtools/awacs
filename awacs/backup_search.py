# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Backup Search"
prefix = "backup-search"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


GetSearchJob = Action("GetSearchJob")
GetSearchResultExportJob = Action("GetSearchResultExportJob")
ListSearchJobBackups = Action("ListSearchJobBackups")
ListSearchJobResults = Action("ListSearchJobResults")
ListSearchJobs = Action("ListSearchJobs")
ListSearchResultExportJobs = Action("ListSearchResultExportJobs")
ListTagsForResource = Action("ListTagsForResource")
StartSearchJob = Action("StartSearchJob")
StartSearchResultExportJob = Action("StartSearchResultExportJob")
StopSearchJob = Action("StopSearchJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
