# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SageMaker geospatial capabilities"
prefix = "sagemaker-geospatial"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DeleteEarthObservationJob = Action("DeleteEarthObservationJob")
DeleteVectorEnrichmentJob = Action("DeleteVectorEnrichmentJob")
ExportEarthObservationJob = Action("ExportEarthObservationJob")
ExportVectorEnrichmentJob = Action("ExportVectorEnrichmentJob")
GetEarthObservationJob = Action("GetEarthObservationJob")
GetRasterDataCollection = Action("GetRasterDataCollection")
GetTile = Action("GetTile")
GetVectorEnrichmentJob = Action("GetVectorEnrichmentJob")
ListEarthObservationJobs = Action("ListEarthObservationJobs")
ListRasterDataCollections = Action("ListRasterDataCollections")
ListTagsForResource = Action("ListTagsForResource")
ListVectorEnrichmentJobs = Action("ListVectorEnrichmentJobs")
SearchRasterDataCollection = Action("SearchRasterDataCollection")
StartEarthObservationJob = Action("StartEarthObservationJob")
StartVectorEnrichmentJob = Action("StartVectorEnrichmentJob")
StopEarthObservationJob = Action("StopEarthObservationJob")
StopVectorEnrichmentJob = Action("StopVectorEnrichmentJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
