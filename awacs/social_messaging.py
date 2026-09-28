# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS End User Messaging Social"
prefix = "social-messaging"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateWhatsAppBusinessAccount = Action("AssociateWhatsAppBusinessAccount")
CreateWhatsAppFlow = Action("CreateWhatsAppFlow")
CreateWhatsAppMessageTemplate = Action("CreateWhatsAppMessageTemplate")
CreateWhatsAppMessageTemplateFromLibrary = Action(
    "CreateWhatsAppMessageTemplateFromLibrary"
)
CreateWhatsAppMessageTemplateMedia = Action("CreateWhatsAppMessageTemplateMedia")
DeleteWhatsAppFlow = Action("DeleteWhatsAppFlow")
DeleteWhatsAppMessageMedia = Action("DeleteWhatsAppMessageMedia")
DeleteWhatsAppMessageTemplate = Action("DeleteWhatsAppMessageTemplate")
DeprecateWhatsAppFlow = Action("DeprecateWhatsAppFlow")
DisassociateWhatsAppBusinessAccount = Action("DisassociateWhatsAppBusinessAccount")
GetLinkedWhatsAppBusinessAccount = Action("GetLinkedWhatsAppBusinessAccount")
GetLinkedWhatsAppBusinessAccountPhoneNumber = Action(
    "GetLinkedWhatsAppBusinessAccountPhoneNumber"
)
GetWhatsAppCallPermission = Action("GetWhatsAppCallPermission")
GetWhatsAppFlow = Action("GetWhatsAppFlow")
GetWhatsAppFlowPreview = Action("GetWhatsAppFlowPreview")
GetWhatsAppMessageMedia = Action("GetWhatsAppMessageMedia")
GetWhatsAppMessageTemplate = Action("GetWhatsAppMessageTemplate")
ListLinkedWhatsAppBusinessAccounts = Action("ListLinkedWhatsAppBusinessAccounts")
ListTagsForResource = Action("ListTagsForResource")
ListWhatsAppFlowAssets = Action("ListWhatsAppFlowAssets")
ListWhatsAppFlows = Action("ListWhatsAppFlows")
ListWhatsAppMessageTemplates = Action("ListWhatsAppMessageTemplates")
ListWhatsAppTemplateLibrary = Action("ListWhatsAppTemplateLibrary")
PostWhatsAppMessageMedia = Action("PostWhatsAppMessageMedia")
PublishWhatsAppFlow = Action("PublishWhatsAppFlow")
PutWhatsAppBusinessAccountEventDestinations = Action(
    "PutWhatsAppBusinessAccountEventDestinations"
)
SendWhatsAppCallEvent = Action("SendWhatsAppCallEvent")
SendWhatsAppMessage = Action("SendWhatsAppMessage")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLinkedWhatsAppBusinessAccountPhoneNumber = Action(
    "UpdateLinkedWhatsAppBusinessAccountPhoneNumber"
)
UpdateWhatsAppFlow = Action("UpdateWhatsAppFlow")
UpdateWhatsAppFlowAssets = Action("UpdateWhatsAppFlowAssets")
UpdateWhatsAppMessageTemplate = Action("UpdateWhatsAppMessageTemplate")
