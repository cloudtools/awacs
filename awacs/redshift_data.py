# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Redshift Data API"
prefix = "redshift-data"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchExecuteStatement = Action("BatchExecuteStatement")
CancelStatement = Action("CancelStatement")
DescribeStatement = Action("DescribeStatement")
DescribeTable = Action("DescribeTable")
ExecuteStatement = Action("ExecuteStatement")
GetStagingBucketLocation = Action("GetStagingBucketLocation")
GetStatementResult = Action("GetStatementResult")
ListDatabases = Action("ListDatabases")
ListSchemas = Action("ListSchemas")
ListStatements = Action("ListStatements")
ListTables = Action("ListTables")
