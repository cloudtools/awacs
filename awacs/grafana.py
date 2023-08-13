# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Grafana"
prefix = "grafana"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateLicense = Action("AssociateLicense")
CreateWorkspace = Action("CreateWorkspace")
CreateWorkspaceApiKey = Action("CreateWorkspaceApiKey")
DeleteWorkspace = Action("DeleteWorkspace")
DeleteWorkspaceApiKey = Action("DeleteWorkspaceApiKey")
DescribeWorkspace = Action("DescribeWorkspace")
DescribeWorkspaceAuthentication = Action("DescribeWorkspaceAuthentication")
DescribeWorkspaceConfiguration = Action("DescribeWorkspaceConfiguration")
DisassociateLicense = Action("DisassociateLicense")
ListPermissions = Action("ListPermissions")
ListTagsForResource = Action("ListTagsForResource")
ListVersions = Action("ListVersions")
ListWorkspaces = Action("ListWorkspaces")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePermissions = Action("UpdatePermissions")
UpdateWorkspace = Action("UpdateWorkspace")
UpdateWorkspaceAuthentication = Action("UpdateWorkspaceAuthentication")
UpdateWorkspaceConfiguration = Action("UpdateWorkspaceConfiguration")
