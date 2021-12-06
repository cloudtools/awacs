# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Timestream"
prefix = "timestream"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelQuery = Action("CancelQuery")
CreateDatabase = Action("CreateDatabase")
CreateScheduledQuery = Action("CreateScheduledQuery")
CreateTable = Action("CreateTable")
DeleteDatabase = Action("DeleteDatabase")
DeleteScheduledQuery = Action("DeleteScheduledQuery")
DeleteTable = Action("DeleteTable")
DescribeDatabase = Action("DescribeDatabase")
DescribeEndpoints = Action("DescribeEndpoints")
DescribeScheduledQuery = Action("DescribeScheduledQuery")
DescribeTable = Action("DescribeTable")
ExecuteScheduledQuery = Action("ExecuteScheduledQuery")
ListDatabases = Action("ListDatabases")
ListMeasures = Action("ListMeasures")
ListScheduledQueries = Action("ListScheduledQueries")
ListTables = Action("ListTables")
ListTagsForResource = Action("ListTagsForResource")
Select = Action("Select")
SelectValues = Action("SelectValues")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDatabase = Action("UpdateDatabase")
UpdateScheduledQuery = Action("UpdateScheduledQuery")
UpdateTable = Action("UpdateTable")
WriteRecords = Action("WriteRecords")
