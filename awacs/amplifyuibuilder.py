# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify UI Builder"
prefix = "amplifyuibuilder"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateComponent = Action("CreateComponent")
CreateForm = Action("CreateForm")
CreateTheme = Action("CreateTheme")
DeleteComponent = Action("DeleteComponent")
DeleteForm = Action("DeleteForm")
DeleteTheme = Action("DeleteTheme")
ExchangeCodeForToken = Action("ExchangeCodeForToken")
ExportComponents = Action("ExportComponents")
ExportForms = Action("ExportForms")
ExportThemes = Action("ExportThemes")
GetCodegenJob = Action("GetCodegenJob")
GetComponent = Action("GetComponent")
GetForm = Action("GetForm")
GetMetadata = Action("GetMetadata")
GetTheme = Action("GetTheme")
ListCodegenJobs = Action("ListCodegenJobs")
ListComponents = Action("ListComponents")
ListForms = Action("ListForms")
ListTagsForResource = Action("ListTagsForResource")
ListThemes = Action("ListThemes")
PutMetadataFlag = Action("PutMetadataFlag")
RefreshToken = Action("RefreshToken")
ResetMetadataFlag = Action("ResetMetadataFlag")
StartCodegenJob = Action("StartCodegenJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComponent = Action("UpdateComponent")
UpdateForm = Action("UpdateForm")
UpdateTheme = Action("UpdateTheme")
