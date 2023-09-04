# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Private CA Connector for Active Directory"
prefix = "pca-connector-ad"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateConnector = Action("CreateConnector")
CreateDirectoryRegistration = Action("CreateDirectoryRegistration")
CreateServicePrincipalName = Action("CreateServicePrincipalName")
CreateTemplate = Action("CreateTemplate")
CreateTemplateGroupAccessControlEntry = Action("CreateTemplateGroupAccessControlEntry")
DeleteConnector = Action("DeleteConnector")
DeleteDirectoryRegistration = Action("DeleteDirectoryRegistration")
DeleteServicePrincipalName = Action("DeleteServicePrincipalName")
DeleteTemplate = Action("DeleteTemplate")
DeleteTemplateGroupAccessControlEntry = Action("DeleteTemplateGroupAccessControlEntry")
GetConnector = Action("GetConnector")
GetDirectoryRegistration = Action("GetDirectoryRegistration")
GetServicePrincipalName = Action("GetServicePrincipalName")
GetTemplate = Action("GetTemplate")
GetTemplateGroupAccessControlEntry = Action("GetTemplateGroupAccessControlEntry")
ListConnectors = Action("ListConnectors")
ListDirectoryRegistrations = Action("ListDirectoryRegistrations")
ListServicePrincipalNames = Action("ListServicePrincipalNames")
ListTagsForResource = Action("ListTagsForResource")
ListTemplateGroupAccessControlEntries = Action("ListTemplateGroupAccessControlEntries")
ListTemplates = Action("ListTemplates")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateTemplate = Action("UpdateTemplate")
UpdateTemplateGroupAccessControlEntry = Action("UpdateTemplateGroupAccessControlEntry")
