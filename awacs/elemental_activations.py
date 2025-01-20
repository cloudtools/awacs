# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental Appliances and Software Activation Service"
prefix = "elemental-activations"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CompleteAccountRegistration = Action("CompleteAccountRegistration")
CompleteFileUpload = Action("CompleteFileUpload")
ConfirmAccount = Action("ConfirmAccount")
DownloadKickstart = Action("DownloadKickstart")
DownloadSoftware = Action("DownloadSoftware")
GenerateLicense = Action("GenerateLicense")
GenerateLicenses = Action("GenerateLicenses")
GetActivation = Action("GetActivation")
GetArtifactGroupSoftwareVersions = Action("GetArtifactGroupSoftwareVersions")
GetAsset = Action("GetAsset")
GetAssets = Action("GetAssets")
GetProductAdvisories = Action("GetProductAdvisories")
GetSoftwareVersions = Action("GetSoftwareVersions")
ListTagsForResource = Action("ListTagsForResource")
StartAccountRegistration = Action("StartAccountRegistration")
StartFileUpload = Action("StartFileUpload")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
