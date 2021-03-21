# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AppIntegrations"
prefix = "app-integrations"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateEventIntegration = Action("CreateEventIntegration")
CreateEventIntegrationAssociation = Action("CreateEventIntegrationAssociation")
DeleteEventIntegration = Action("DeleteEventIntegration")
DeleteEventIntegrationAssociation = Action("DeleteEventIntegrationAssociation")
GetEventIntegration = Action("GetEventIntegration")
ListEventIntegrationAssociations = Action("ListEventIntegrationAssociations")
ListEventIntegrations = Action("ListEventIntegrations")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateEventIntegration = Action("UpdateEventIntegration")
