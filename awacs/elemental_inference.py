# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental Inference"
prefix = "elemental-inference"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFeed = Action("AssociateFeed")
CreateDictionary = Action("CreateDictionary")
CreateFeed = Action("CreateFeed")
DeleteDictionary = Action("DeleteDictionary")
DeleteFeed = Action("DeleteFeed")
DisassociateFeed = Action("DisassociateFeed")
ExportDictionaryEntries = Action("ExportDictionaryEntries")
GetDictionary = Action("GetDictionary")
GetFeed = Action("GetFeed")
GetMetadata = Action("GetMetadata")
ListDictionaries = Action("ListDictionaries")
ListFeeds = Action("ListFeeds")
ListTagsForResource = Action("ListTagsForResource")
PutMedia = Action("PutMedia")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDictionary = Action("UpdateDictionary")
UpdateFeed = Action("UpdateFeed")
