# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Lake Formation"
prefix = "lakeformation"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddLFTagsToResource = Action("AddLFTagsToResource")
BatchGrantPermissions = Action("BatchGrantPermissions")
BatchRevokePermissions = Action("BatchRevokePermissions")
CreateLFTag = Action("CreateLFTag")
DeleteLFTag = Action("DeleteLFTag")
DeregisterResource = Action("DeregisterResource")
DescribeResource = Action("DescribeResource")
GetDataAccess = Action("GetDataAccess")
GetDataLakeSettings = Action("GetDataLakeSettings")
GetEffectivePermissionsForPath = Action("GetEffectivePermissionsForPath")
GetLFTag = Action("GetLFTag")
GetResourceLFTags = Action("GetResourceLFTags")
GrantPermissions = Action("GrantPermissions")
ListLFTags = Action("ListLFTags")
ListPermissions = Action("ListPermissions")
ListResources = Action("ListResources")
PutDataLakeSettings = Action("PutDataLakeSettings")
RegisterResource = Action("RegisterResource")
RemoveLFTagsFromResource = Action("RemoveLFTagsFromResource")
RevokePermissions = Action("RevokePermissions")
SearchDatabasesByLFTags = Action("SearchDatabasesByLFTags")
SearchTablesByLFTags = Action("SearchTablesByLFTags")
UpdateLFTag = Action("UpdateLFTag")
UpdateResource = Action("UpdateResource")
