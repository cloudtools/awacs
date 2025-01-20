# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS HealthImaging"
prefix = "medical-imaging"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CopyImageSet = Action("CopyImageSet")
CreateDatastore = Action("CreateDatastore")
DeleteDatastore = Action("DeleteDatastore")
DeleteImageSet = Action("DeleteImageSet")
GetDICOMImportJob = Action("GetDICOMImportJob")
GetDICOMInstance = Action("GetDICOMInstance")
GetDICOMInstanceFrames = Action("GetDICOMInstanceFrames")
GetDICOMInstanceMetadata = Action("GetDICOMInstanceMetadata")
GetDatastore = Action("GetDatastore")
GetImageFrame = Action("GetImageFrame")
GetImageSet = Action("GetImageSet")
GetImageSetMetadata = Action("GetImageSetMetadata")
ListDICOMImportJobs = Action("ListDICOMImportJobs")
ListDatastores = Action("ListDatastores")
ListImageSetVersions = Action("ListImageSetVersions")
ListTagsForResource = Action("ListTagsForResource")
SearchImageSets = Action("SearchImageSets")
StartDICOMImportJob = Action("StartDICOMImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateImageSetMetadata = Action("UpdateImageSetMetadata")
