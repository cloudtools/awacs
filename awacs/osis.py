# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon OpenSearch Ingestion"
prefix = "osis"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreatePipeline = Action("CreatePipeline")
DeletePipeline = Action("DeletePipeline")
GetPipeline = Action("GetPipeline")
GetPipelineBlueprint = Action("GetPipelineBlueprint")
GetPipelineChangeProgress = Action("GetPipelineChangeProgress")
Ingest = Action("Ingest")
ListPipelineBlueprints = Action("ListPipelineBlueprints")
ListPipelines = Action("ListPipelines")
ListTagsForResource = Action("ListTagsForResource")
StartPipeline = Action("StartPipeline")
StopPipeline = Action("StopPipeline")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePipeline = Action("UpdatePipeline")
ValidatePipeline = Action("ValidatePipeline")
