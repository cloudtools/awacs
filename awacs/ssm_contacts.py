# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Systems Manager Incident Manager Contacts"
prefix = "ssm-contacts"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
DeactivateContactChannel = Action("DeactivateContactChannel")
DeleteContact = Action("DeleteContact")
DeleteContactChannel = Action("DeleteContactChannel")
DeleteContactPolicy = Action("DeleteContactPolicy")
DescribeEngagement = Action("DescribeEngagement")
DescribePage = Action("DescribePage")
GetContact = Action("GetContact")
GetContactChannel = Action("GetContactChannel")
ListContactChannels = Action("ListContactChannels")
ListContacts = Action("ListContacts")
ListEngagements = Action("ListEngagements")
ListPageReceipts = Action("ListPageReceipts")
ListPagesByContact = Action("ListPagesByContact")
ListPagesByEngagement = Action("ListPagesByEngagement")
PutContactPolicy = Action("PutContactPolicy")
SendActivationCode = Action("SendActivationCode")
StartEngagement = Action("StartEngagement")
StopEngagement = Action("StopEngagement")
UpdateContact = Action("UpdateContact")
UpdateContactChannel = Action("UpdateContactChannel")
UpdateContactPolicy = Action("UpdateContactPolicy")
