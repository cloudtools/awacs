# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS End User Messaging"
prefix = "end-user-messaging"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBrandProfile = Action("CreateBrandProfile")
CreateBrandProfileAttributes = Action("CreateBrandProfileAttributes")
CreateBrandProfileFromRegistration = Action("CreateBrandProfileFromRegistration")
CreateNotifyCodeConfiguration = Action("CreateNotifyCodeConfiguration")
CreateRegistrationsFromBrandProfile = Action("CreateRegistrationsFromBrandProfile")
DeleteBrandProfile = Action("DeleteBrandProfile")
DeleteBrandProfileAttribute = Action("DeleteBrandProfileAttribute")
DeleteNotifyCodeConfiguration = Action("DeleteNotifyCodeConfiguration")
GetBrandProfile = Action("GetBrandProfile")
GetBrandProfileAttribute = Action("GetBrandProfileAttribute")
GetJob = Action("GetJob")
GetNotifyCodeConfiguration = Action("GetNotifyCodeConfiguration")
ListBrandProfileAttributes = Action("ListBrandProfileAttributes")
ListBrandProfiles = Action("ListBrandProfiles")
ListJobs = Action("ListJobs")
ListNotifyCodeConfigurations = Action("ListNotifyCodeConfigurations")
ListRegistrationsFromBrandProfile = Action("ListRegistrationsFromBrandProfile")
ListTagsForResource = Action("ListTagsForResource")
SendNotifyCodeVerification = Action("SendNotifyCodeVerification")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBrandProfile = Action("UpdateBrandProfile")
UpdateBrandProfileAttribute = Action("UpdateBrandProfileAttribute")
UpdateBrandProfileFromRegistration = Action("UpdateBrandProfileFromRegistration")
UpdateNotifyCodeConfiguration = Action("UpdateNotifyCodeConfiguration")
UpdateRegistrationsFromBrandProfile = Action("UpdateRegistrationsFromBrandProfile")
ValidateNotifyCodeVerification = Action("ValidateNotifyCodeVerification")
