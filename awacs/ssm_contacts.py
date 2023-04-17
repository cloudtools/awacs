# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Systems Manager Incident Manager Contacts"
prefix = "ssm-contacts"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptPage = Action("AcceptPage")
ActivateContactChannel = Action("ActivateContactChannel")
AssociateContact = Action("AssociateContact")
CreateContact = Action("CreateContact")
CreateContactChannel = Action("CreateContactChannel")
CreateRotation = Action("CreateRotation")
CreateRotationOverride = Action("CreateRotationOverride")
DeactivateContactChannel = Action("DeactivateContactChannel")
DeleteContact = Action("DeleteContact")
DeleteContactChannel = Action("DeleteContactChannel")
DeleteContactPolicy = Action("DeleteContactPolicy")
DeleteRotation = Action("DeleteRotation")
DeleteRotationOverride = Action("DeleteRotationOverride")
DescribeEngagement = Action("DescribeEngagement")
DescribePage = Action("DescribePage")
GetContact = Action("GetContact")
GetContactChannel = Action("GetContactChannel")
GetContactPolicy = Action("GetContactPolicy")
GetRotation = Action("GetRotation")
GetRotationOverride = Action("GetRotationOverride")
ListContactChannels = Action("ListContactChannels")
ListContacts = Action("ListContacts")
ListEngagements = Action("ListEngagements")
ListPageReceipts = Action("ListPageReceipts")
ListPageResolutions = Action("ListPageResolutions")
ListPagesByContact = Action("ListPagesByContact")
ListPagesByEngagement = Action("ListPagesByEngagement")
ListPreviewRotationShifts = Action("ListPreviewRotationShifts")
ListRotationOverrides = Action("ListRotationOverrides")
ListRotationShifts = Action("ListRotationShifts")
ListRotations = Action("ListRotations")
ListTagsForResource = Action("ListTagsForResource")
PutContactPolicy = Action("PutContactPolicy")
SendActivationCode = Action("SendActivationCode")
StartEngagement = Action("StartEngagement")
StopEngagement = Action("StopEngagement")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateContact = Action("UpdateContact")
UpdateContactChannel = Action("UpdateContactChannel")
UpdateContactPolicy = Action("UpdateContactPolicy")
UpdateRotation = Action("UpdateRotation")
