# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify UI Builder"
prefix = "amplifyuibuilder"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateComponent = Action("CreateComponent")
CreateTheme = Action("CreateTheme")
DeleteComponent = Action("DeleteComponent")
DeleteTheme = Action("DeleteTheme")
ExchangeCodeForToken = Action("ExchangeCodeForToken")
ExportComponents = Action("ExportComponents")
ExportThemes = Action("ExportThemes")
GetComponent = Action("GetComponent")
GetTheme = Action("GetTheme")
ListComponents = Action("ListComponents")
ListTagsForResource = Action("ListTagsForResource")
ListThemes = Action("ListThemes")
RefreshToken = Action("RefreshToken")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComponent = Action("UpdateComponent")
UpdateTheme = Action("UpdateTheme")
