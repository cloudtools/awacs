# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SageMaker Ground Truth Synthetic"
prefix = "sagemaker-groundtruth-synthetic"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateProject = Action("CreateProject")
DeleteProject = Action("DeleteProject")
GetAccountDetails = Action("GetAccountDetails")
GetBatch = Action("GetBatch")
GetProject = Action("GetProject")
ListBatchDataTransfers = Action("ListBatchDataTransfers")
ListBatchSummaries = Action("ListBatchSummaries")
ListProjectDataTransfers = Action("ListProjectDataTransfers")
ListProjectSummaries = Action("ListProjectSummaries")
StartBatchDataTransfer = Action("StartBatchDataTransfer")
StartProjectDataTransfer = Action("StartProjectDataTransfer")
UpdateBatch = Action("UpdateBatch")
