# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Billing And Cost Management Data Exports"
prefix = "bcm-data-exports"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateExport = Action("CreateExport")
DeleteExport = Action("DeleteExport")
GetExecution = Action("GetExecution")
GetExport = Action("GetExport")
GetTable = Action("GetTable")
ListExecutions = Action("ListExecutions")
ListExports = Action("ListExports")
ListTables = Action("ListTables")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateExport = Action("UpdateExport")
