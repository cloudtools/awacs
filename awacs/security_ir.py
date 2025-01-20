# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Security Incident Response"
prefix = "security-ir"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetMemberAccountDetails = Action("BatchGetMemberAccountDetails")
CancelMembership = Action("CancelMembership")
CloseCase = Action("CloseCase")
CreateCase = Action("CreateCase")
CreateCaseComment = Action("CreateCaseComment")
CreateMembership = Action("CreateMembership")
GetCase = Action("GetCase")
GetCaseAttachmentDownloadUrl = Action("GetCaseAttachmentDownloadUrl")
GetCaseAttachmentUploadUrl = Action("GetCaseAttachmentUploadUrl")
GetMembership = Action("GetMembership")
ListCaseEdits = Action("ListCaseEdits")
ListCases = Action("ListCases")
ListComments = Action("ListComments")
ListMemberships = Action("ListMemberships")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCase = Action("UpdateCase")
UpdateCaseComment = Action("UpdateCaseComment")
UpdateCaseStatus = Action("UpdateCaseStatus")
UpdateMembership = Action("UpdateMembership")
UpdateResolverType = Action("UpdateResolverType")
