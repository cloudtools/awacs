# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS B2B Data Interchange"
prefix = "b2bi"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateCapability = Action("CreateCapability")
CreatePartnership = Action("CreatePartnership")
CreateProfile = Action("CreateProfile")
CreateStarterMappingTemplate = Action("CreateStarterMappingTemplate")
CreateTransformer = Action("CreateTransformer")
DeleteCapability = Action("DeleteCapability")
DeletePartnership = Action("DeletePartnership")
DeleteProfile = Action("DeleteProfile")
DeleteTransformer = Action("DeleteTransformer")
GenerateMapping = Action("GenerateMapping")
GetCapability = Action("GetCapability")
GetPartnership = Action("GetPartnership")
GetProfile = Action("GetProfile")
GetTransformer = Action("GetTransformer")
GetTransformerJob = Action("GetTransformerJob")
ListCapabilities = Action("ListCapabilities")
ListPartnerships = Action("ListPartnerships")
ListProfiles = Action("ListProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListTransformers = Action("ListTransformers")
StartTransformerJob = Action("StartTransformerJob")
TagResource = Action("TagResource")
TestConversion = Action("TestConversion")
TestMapping = Action("TestMapping")
TestParsing = Action("TestParsing")
UntagResource = Action("UntagResource")
UpdateCapability = Action("UpdateCapability")
UpdatePartnership = Action("UpdatePartnership")
UpdateProfile = Action("UpdateProfile")
UpdateTransformer = Action("UpdateTransformer")
