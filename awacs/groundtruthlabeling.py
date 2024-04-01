# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon GroundTruth Labeling"
prefix = "groundtruthlabeling"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociatePatchToManifestJob = Action("AssociatePatchToManifestJob")
CreateBatch = Action("CreateBatch")
CreateIntakeForm = Action("CreateIntakeForm")
CreateProject = Action("CreateProject")
CreateWorkflowDefinition = Action("CreateWorkflowDefinition")
DescribeConsoleJob = Action("DescribeConsoleJob")
GenerateLIDARPreviewTaskConfigJob = Action("GenerateLIDARPreviewTaskConfigJob")
GetBatch = Action("GetBatch")
GetIntakeFormStatus = Action("GetIntakeFormStatus")
ListBatches = Action("ListBatches")
ListDatasetObjects = Action("ListDatasetObjects")
ListProjects = Action("ListProjects")
RunFilterOrSampleDatasetJob = Action("RunFilterOrSampleDatasetJob")
RunGenerateManifestByCrawlingJob = Action("RunGenerateManifestByCrawlingJob")
RunGenerateManifestMetricsJob = Action("RunGenerateManifestMetricsJob")
UpdateBatch = Action("UpdateBatch")
