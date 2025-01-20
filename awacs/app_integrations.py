# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AppIntegrations"
prefix = "app-integrations"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateApplication = Action("CreateApplication")
CreateApplicationAssociation = Action("CreateApplicationAssociation")
CreateDataIntegration = Action("CreateDataIntegration")
CreateDataIntegrationAssociation = Action("CreateDataIntegrationAssociation")
CreateEventIntegration = Action("CreateEventIntegration")
CreateEventIntegrationAssociation = Action("CreateEventIntegrationAssociation")
DeleteApplication = Action("DeleteApplication")
DeleteApplicationAssociation = Action("DeleteApplicationAssociation")
DeleteDataIntegration = Action("DeleteDataIntegration")
DeleteDataIntegrationAssociation = Action("DeleteDataIntegrationAssociation")
DeleteEventIntegration = Action("DeleteEventIntegration")
DeleteEventIntegrationAssociation = Action("DeleteEventIntegrationAssociation")
GetApplication = Action("GetApplication")
GetDataIntegration = Action("GetDataIntegration")
GetEventIntegration = Action("GetEventIntegration")
ListApplicationAssociations = Action("ListApplicationAssociations")
ListApplications = Action("ListApplications")
ListDataIntegrationAssociations = Action("ListDataIntegrationAssociations")
ListDataIntegrations = Action("ListDataIntegrations")
ListEventIntegrationAssociations = Action("ListEventIntegrationAssociations")
ListEventIntegrations = Action("ListEventIntegrations")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateDataIntegration = Action("UpdateDataIntegration")
UpdateDataIntegrationAssociation = Action("UpdateDataIntegrationAssociation")
UpdateEventIntegration = Action("UpdateEventIntegration")
