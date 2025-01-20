# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon WorkSpaces Secure Browser"
prefix = "workspaces-web"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateBrowserSettings = Action("AssociateBrowserSettings")
AssociateDataProtectionSettings = Action("AssociateDataProtectionSettings")
AssociateIpAccessSettings = Action("AssociateIpAccessSettings")
AssociateNetworkSettings = Action("AssociateNetworkSettings")
AssociateTrustStore = Action("AssociateTrustStore")
AssociateUserAccessLoggingSettings = Action("AssociateUserAccessLoggingSettings")
AssociateUserSettings = Action("AssociateUserSettings")
CreateBrowserSettings = Action("CreateBrowserSettings")
CreateDataProtectionSettings = Action("CreateDataProtectionSettings")
CreateIdentityProvider = Action("CreateIdentityProvider")
CreateIpAccessSettings = Action("CreateIpAccessSettings")
CreateNetworkSettings = Action("CreateNetworkSettings")
CreatePortal = Action("CreatePortal")
CreateTrustStore = Action("CreateTrustStore")
CreateUserAccessLoggingSettings = Action("CreateUserAccessLoggingSettings")
CreateUserSettings = Action("CreateUserSettings")
DeleteBrowserSettings = Action("DeleteBrowserSettings")
DeleteDataProtectionSettings = Action("DeleteDataProtectionSettings")
DeleteIdentityProvider = Action("DeleteIdentityProvider")
DeleteIpAccessSettings = Action("DeleteIpAccessSettings")
DeleteNetworkSettings = Action("DeleteNetworkSettings")
DeletePortal = Action("DeletePortal")
DeleteTrustStore = Action("DeleteTrustStore")
DeleteUserAccessLoggingSettings = Action("DeleteUserAccessLoggingSettings")
DeleteUserSettings = Action("DeleteUserSettings")
DisassociateBrowserSettings = Action("DisassociateBrowserSettings")
DisassociateDataProtectionSettings = Action("DisassociateDataProtectionSettings")
DisassociateIpAccessSettings = Action("DisassociateIpAccessSettings")
DisassociateNetworkSettings = Action("DisassociateNetworkSettings")
DisassociateTrustStore = Action("DisassociateTrustStore")
DisassociateUserAccessLoggingSettings = Action("DisassociateUserAccessLoggingSettings")
DisassociateUserSettings = Action("DisassociateUserSettings")
ExpireSession = Action("ExpireSession")
GetBrowserSettings = Action("GetBrowserSettings")
GetDataProtectionSettings = Action("GetDataProtectionSettings")
GetIdentityProvider = Action("GetIdentityProvider")
GetIpAccessSettings = Action("GetIpAccessSettings")
GetNetworkSettings = Action("GetNetworkSettings")
GetPortal = Action("GetPortal")
GetPortalServiceProviderMetadata = Action("GetPortalServiceProviderMetadata")
GetSession = Action("GetSession")
GetTrustStore = Action("GetTrustStore")
GetTrustStoreCertificate = Action("GetTrustStoreCertificate")
GetUserAccessLoggingSettings = Action("GetUserAccessLoggingSettings")
GetUserSettings = Action("GetUserSettings")
ListBrowserSettings = Action("ListBrowserSettings")
ListDataProtectionSettings = Action("ListDataProtectionSettings")
ListIdentityProviders = Action("ListIdentityProviders")
ListIpAccessSettings = Action("ListIpAccessSettings")
ListNetworkSettings = Action("ListNetworkSettings")
ListPortals = Action("ListPortals")
ListSessions = Action("ListSessions")
ListTagsForResource = Action("ListTagsForResource")
ListTrustStoreCertificates = Action("ListTrustStoreCertificates")
ListTrustStores = Action("ListTrustStores")
ListUserAccessLoggingSettings = Action("ListUserAccessLoggingSettings")
ListUserSettings = Action("ListUserSettings")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBrowserSettings = Action("UpdateBrowserSettings")
UpdateDataProtectionSettings = Action("UpdateDataProtectionSettings")
UpdateIdentityProvider = Action("UpdateIdentityProvider")
UpdateIpAccessSettings = Action("UpdateIpAccessSettings")
UpdateNetworkSettings = Action("UpdateNetworkSettings")
UpdatePortal = Action("UpdatePortal")
UpdateTrustStore = Action("UpdateTrustStore")
UpdateUserAccessLoggingSettings = Action("UpdateUserAccessLoggingSettings")
UpdateUserSettings = Action("UpdateUserSettings")
