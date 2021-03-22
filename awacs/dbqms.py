# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Database Query Metadata Service"
prefix = "dbqms"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateFavoriteQuery = Action("CreateFavoriteQuery")
CreateQueryHistory = Action("CreateQueryHistory")
DeleteFavoriteQueries = Action("DeleteFavoriteQueries")
DeleteQueryHistory = Action("DeleteQueryHistory")
DescribeFavoriteQueries = Action("DescribeFavoriteQueries")
DescribeQueryHistory = Action("DescribeQueryHistory")
GetQueryString = Action("GetQueryString")
UpdateFavoriteQuery = Action("UpdateFavoriteQuery")
UpdateQueryHistory = Action("UpdateQueryHistory")
