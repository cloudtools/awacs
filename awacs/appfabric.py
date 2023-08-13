# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS AppFabric"
prefix = "appfabric"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetUserAccessTasks = Action("BatchGetUserAccessTasks")
ConnectAppAuthorization = Action("ConnectAppAuthorization")
CreateAppAuthorization = Action("CreateAppAuthorization")
CreateAppBundle = Action("CreateAppBundle")
CreateIngestion = Action("CreateIngestion")
CreateIngestionDestination = Action("CreateIngestionDestination")
DeleteAppAuthorization = Action("DeleteAppAuthorization")
DeleteAppBundle = Action("DeleteAppBundle")
DeleteIngestion = Action("DeleteIngestion")
DeleteIngestionDestination = Action("DeleteIngestionDestination")
GetAppAuthorization = Action("GetAppAuthorization")
GetAppBundle = Action("GetAppBundle")
GetIngestion = Action("GetIngestion")
GetIngestionDestination = Action("GetIngestionDestination")
ListAppAuthorizations = Action("ListAppAuthorizations")
ListAppBundles = Action("ListAppBundles")
ListIngestionDestinations = Action("ListIngestionDestinations")
ListIngestions = Action("ListIngestions")
ListTagsForResource = Action("ListTagsForResource")
StartIngestion = Action("StartIngestion")
StartUserAccessTasks = Action("StartUserAccessTasks")
StopIngestion = Action("StopIngestion")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAppAuthorization = Action("UpdateAppAuthorization")
UpdateIngestionDestination = Action("UpdateIngestionDestination")
