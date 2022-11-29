# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DeepComposer"
prefix = "deepcomposer"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateCoupon = Action("AssociateCoupon")
CreateAudio = Action("CreateAudio")
CreateComposition = Action("CreateComposition")
CreateModel = Action("CreateModel")
DeleteComposition = Action("DeleteComposition")
DeleteModel = Action("DeleteModel")
GetComposition = Action("GetComposition")
GetModel = Action("GetModel")
GetSampleModel = Action("GetSampleModel")
ListCompositions = Action("ListCompositions")
ListModels = Action("ListModels")
ListSampleModels = Action("ListSampleModels")
ListTagsForResource = Action("ListTagsForResource")
ListTrainingTopics = Action("ListTrainingTopics")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateComposition = Action("UpdateComposition")
UpdateModel = Action("UpdateModel")
