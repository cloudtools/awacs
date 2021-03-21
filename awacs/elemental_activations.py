# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental Appliances and Software Activation Service"
prefix = "elemental-activations"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CompleteAccountRegistration = Action("CompleteAccountRegistration")
CompleteFileUpload = Action("CompleteFileUpload")
DownloadSoftware = Action("DownloadSoftware")
GenerateLicenses = Action("GenerateLicenses")
GetActivation = Action("GetActivation")
ListTagsForResource = Action("ListTagsForResource")
StartAccountRegistration = Action("StartAccountRegistration")
StartFileUpload = Action("StartFileUpload")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
