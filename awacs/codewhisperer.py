# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CodeWhisperer"
prefix = "codewhisperer"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
AssociateCustomizationPermission = Action("AssociateCustomizationPermission")
CreateCustomization = Action("CreateCustomization")
CreateProfile = Action("CreateProfile")
DeleteCustomization = Action("DeleteCustomization")
DeleteProfile = Action("DeleteProfile")
DisassociateCustomizationPermission = Action("DisassociateCustomizationPermission")
GenerateRecommendations = Action("GenerateRecommendations")
GetCustomization = Action("GetCustomization")
ListCustomizationPermissions = Action("ListCustomizationPermissions")
ListCustomizationVersions = Action("ListCustomizationVersions")
ListCustomizations = Action("ListCustomizations")
ListProfiles = Action("ListProfiles")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCustomization = Action("UpdateCustomization")
UpdateProfile = Action("UpdateProfile")
