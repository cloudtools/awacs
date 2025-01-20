# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS User Notifications"
prefix = "notifications"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateChannel = Action("AssociateChannel")
AssociateManagedNotificationAccountContact = Action(
    "AssociateManagedNotificationAccountContact"
)
AssociateManagedNotificationAdditionalChannel = Action(
    "AssociateManagedNotificationAdditionalChannel"
)
CreateEventRule = Action("CreateEventRule")
CreateNotificationConfiguration = Action("CreateNotificationConfiguration")
DeleteEventRule = Action("DeleteEventRule")
DeleteNotificationConfiguration = Action("DeleteNotificationConfiguration")
DeregisterNotificationHub = Action("DeregisterNotificationHub")
DisableNotificationsAccessForOrganization = Action(
    "DisableNotificationsAccessForOrganization"
)
DisassociateChannel = Action("DisassociateChannel")
DisassociateManagedNotificationAccountContact = Action(
    "DisassociateManagedNotificationAccountContact"
)
DisassociateManagedNotificationAdditionalChannel = Action(
    "DisassociateManagedNotificationAdditionalChannel"
)
EnableNotificationsAccessForOrganization = Action(
    "EnableNotificationsAccessForOrganization"
)
GetEventRule = Action("GetEventRule")
GetFeatureOptInStatus = Action("GetFeatureOptInStatus")
GetManagedNotificationChildEvent = Action("GetManagedNotificationChildEvent")
GetManagedNotificationConfiguration = Action("GetManagedNotificationConfiguration")
GetManagedNotificationEvent = Action("GetManagedNotificationEvent")
GetNotificationConfiguration = Action("GetNotificationConfiguration")
GetNotificationEvent = Action("GetNotificationEvent")
GetNotificationsAccessForOrganization = Action("GetNotificationsAccessForOrganization")
ListChannels = Action("ListChannels")
ListEventRules = Action("ListEventRules")
ListManagedNotificationChannelAssociations = Action(
    "ListManagedNotificationChannelAssociations"
)
ListManagedNotificationChildEvents = Action("ListManagedNotificationChildEvents")
ListManagedNotificationConfigurations = Action("ListManagedNotificationConfigurations")
ListManagedNotificationEvents = Action("ListManagedNotificationEvents")
ListNotificationConfigurations = Action("ListNotificationConfigurations")
ListNotificationEvents = Action("ListNotificationEvents")
ListNotificationHubs = Action("ListNotificationHubs")
ListTagsForResource = Action("ListTagsForResource")
PutFeatureOptInStatus = Action("PutFeatureOptInStatus")
RegisterNotificationHub = Action("RegisterNotificationHub")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEventRule = Action("UpdateEventRule")
UpdateNotificationConfiguration = Action("UpdateNotificationConfiguration")
