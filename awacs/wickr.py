# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Wickr"
prefix = "wickr"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchCreateUser = Action("BatchCreateUser")
BatchDeleteUser = Action("BatchDeleteUser")
BatchLookupUserUname = Action("BatchLookupUserUname")
BatchReinviteUser = Action("BatchReinviteUser")
BatchResetDevicesForUser = Action("BatchResetDevicesForUser")
BatchToggleUserSuspendStatus = Action("BatchToggleUserSuspendStatus")
CreateAdminSession = Action("CreateAdminSession")
CreateBot = Action("CreateBot")
CreateDataRetentionBot = Action("CreateDataRetentionBot")
CreateDataRetentionBotChallenge = Action("CreateDataRetentionBotChallenge")
CreateNetwork = Action("CreateNetwork")
CreateSecurityGroup = Action("CreateSecurityGroup")
DeleteBot = Action("DeleteBot")
DeleteDataRetentionBot = Action("DeleteDataRetentionBot")
DeleteNetwork = Action("DeleteNetwork")
DeleteSecurityGroup = Action("DeleteSecurityGroup")
GetBot = Action("GetBot")
GetBotsCount = Action("GetBotsCount")
GetDataRetentionBot = Action("GetDataRetentionBot")
GetGuestUserHistoryCount = Action("GetGuestUserHistoryCount")
GetNetwork = Action("GetNetwork")
GetNetworkSettings = Action("GetNetworkSettings")
GetOidcInfo = Action("GetOidcInfo")
GetSecurityGroup = Action("GetSecurityGroup")
GetUser = Action("GetUser")
GetUsersCount = Action("GetUsersCount")
ListBlockedGuestUsers = Action("ListBlockedGuestUsers")
ListBots = Action("ListBots")
ListDevicesForUser = Action("ListDevicesForUser")
ListGuestUsers = Action("ListGuestUsers")
ListNetworks = Action("ListNetworks")
ListSecurityGroupUsers = Action("ListSecurityGroupUsers")
ListSecurityGroups = Action("ListSecurityGroups")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
RegisterOidcConfig = Action("RegisterOidcConfig")
RegisterOidcConfigTest = Action("RegisterOidcConfigTest")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBot = Action("UpdateBot")
UpdateDataRetention = Action("UpdateDataRetention")
UpdateGuestUser = Action("UpdateGuestUser")
UpdateNetworkDetails = Action("UpdateNetworkDetails")
UpdateNetworkSettings = Action("UpdateNetworkSettings")
UpdateSecurityGroup = Action("UpdateSecurityGroup")
UpdateUser = Action("UpdateUser")
