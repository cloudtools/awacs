# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Keyspaces (for Apache Cassandra)"
prefix = "cassandra"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


Alter = Action("Alter")
AlterMultiRegionResource = Action("AlterMultiRegionResource")
Create = Action("Create")
CreateMultiRegionResource = Action("CreateMultiRegionResource")
Drop = Action("Drop")
DropMultiRegionResource = Action("DropMultiRegionResource")
Modify = Action("Modify")
ModifyMultiRegionResource = Action("ModifyMultiRegionResource")
Restore = Action("Restore")
RestoreMultiRegionTable = Action("RestoreMultiRegionTable")
Select = Action("Select")
SelectMultiRegionResource = Action("SelectMultiRegionResource")
TagMultiRegionResource = Action("TagMultiRegionResource")
TagResource = Action("TagResource")
UnTagMultiRegionResource = Action("UnTagMultiRegionResource")
UntagResource = Action("UntagResource")
UpdatePartitioner = Action("UpdatePartitioner")
