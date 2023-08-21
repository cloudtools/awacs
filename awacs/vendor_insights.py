# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Marketplace Vendor Insights"
prefix = "vendor-insights"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateSecurityProfile = Action("ActivateSecurityProfile")
AssociateDataSource = Action("AssociateDataSource")
CreateDataSource = Action("CreateDataSource")
CreateSecurityProfile = Action("CreateSecurityProfile")
DeactivateSecurityProfile = Action("DeactivateSecurityProfile")
DeleteDataSource = Action("DeleteDataSource")
DisassociateDataSource = Action("DisassociateDataSource")
GetDataSource = Action("GetDataSource")
GetEntitledSecurityProfileSnapshot = Action("GetEntitledSecurityProfileSnapshot")
GetProfileAccessTerms = Action("GetProfileAccessTerms")
GetSecurityProfile = Action("GetSecurityProfile")
GetSecurityProfileSnapshot = Action("GetSecurityProfileSnapshot")
ListDataSources = Action("ListDataSources")
ListEntitledSecurityProfileSnapshots = Action("ListEntitledSecurityProfileSnapshots")
ListEntitledSecurityProfiles = Action("ListEntitledSecurityProfiles")
ListSecurityProfileSnapshots = Action("ListSecurityProfileSnapshots")
ListSecurityProfiles = Action("ListSecurityProfiles")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataSource = Action("UpdateDataSource")
UpdateSecurityProfile = Action("UpdateSecurityProfile")
UpdateSecurityProfileSnapshotCreationConfiguration = Action(
    "UpdateSecurityProfileSnapshotCreationConfiguration"
)
UpdateSecurityProfileSnapshotReleaseConfiguration = Action(
    "UpdateSecurityProfileSnapshotReleaseConfiguration"
)
