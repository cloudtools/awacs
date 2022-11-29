# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Cognito Sync"
prefix = "cognito-sync"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BulkPublish = Action("BulkPublish")
DeleteDataset = Action("DeleteDataset")
DescribeDataset = Action("DescribeDataset")
DescribeIdentityPoolUsage = Action("DescribeIdentityPoolUsage")
DescribeIdentityUsage = Action("DescribeIdentityUsage")
GetBulkPublishDetails = Action("GetBulkPublishDetails")
GetCognitoEvents = Action("GetCognitoEvents")
GetIdentityPoolConfiguration = Action("GetIdentityPoolConfiguration")
ListDatasets = Action("ListDatasets")
ListIdentityPoolUsage = Action("ListIdentityPoolUsage")
ListRecords = Action("ListRecords")
QueryRecords = Action("QueryRecords")
RegisterDevice = Action("RegisterDevice")
SetCognitoEvents = Action("SetCognitoEvents")
SetDatasetConfiguration = Action("SetDatasetConfiguration")
SetIdentityPoolConfiguration = Action("SetIdentityPoolConfiguration")
SubscribeToDataset = Action("SubscribeToDataset")
UnsubscribeFromDataset = Action("UnsubscribeFromDataset")
UpdateRecords = Action("UpdateRecords")
