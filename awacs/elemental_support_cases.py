# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental Support Cases"
prefix = "elemental-support-cases"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddCaseComment = Action("AddCaseComment")
CheckCasePermission = Action("CheckCasePermission")
CompleteMultipartUpload = Action("CompleteMultipartUpload")
CreateCase = Action("CreateCase")
CreateS3CLIUploadCommand = Action("CreateS3CLIUploadCommand")
CreateS3DownloadUrl = Action("CreateS3DownloadUrl")
GetCase = Action("GetCase")
GetCasePermission = Action("GetCasePermission")
GetCases = Action("GetCases")
GetUICache = Action("GetUICache")
ListTagsForCase = Action("ListTagsForCase")
StartMultipartUpload = Action("StartMultipartUpload")
TagCase = Action("TagCase")
UntagCase = Action("UntagCase")
UpdateCase = Action("UpdateCase")
UpdateCaseStatus = Action("UpdateCaseStatus")
UpdateMultipartUpload = Action("UpdateMultipartUpload")
