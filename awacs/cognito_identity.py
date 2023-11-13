# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Cognito Identity"
prefix = "cognito-identity"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateIdentityPool = Action("CreateIdentityPool")
DeleteIdentities = Action("DeleteIdentities")
DeleteIdentityPool = Action("DeleteIdentityPool")
DescribeIdentity = Action("DescribeIdentity")
DescribeIdentityPool = Action("DescribeIdentityPool")
GetCredentialsForIdentity = Action("GetCredentialsForIdentity")
GetId = Action("GetId")
GetIdentityPoolAnalytics = Action("GetIdentityPoolAnalytics")
GetIdentityPoolDailyAnalytics = Action("GetIdentityPoolDailyAnalytics")
GetIdentityPoolRoles = Action("GetIdentityPoolRoles")
GetIdentityProviderDailyAnalytics = Action("GetIdentityProviderDailyAnalytics")
GetOpenIdToken = Action("GetOpenIdToken")
GetOpenIdTokenForDeveloperIdentity = Action("GetOpenIdTokenForDeveloperIdentity")
GetPrincipalTagAttributeMap = Action("GetPrincipalTagAttributeMap")
ListIdentities = Action("ListIdentities")
ListIdentityPools = Action("ListIdentityPools")
ListTagsForResource = Action("ListTagsForResource")
LookupDeveloperIdentity = Action("LookupDeveloperIdentity")
MergeDeveloperIdentities = Action("MergeDeveloperIdentities")
SetIdentityPoolRoles = Action("SetIdentityPoolRoles")
SetPrincipalTagAttributeMap = Action("SetPrincipalTagAttributeMap")
TagResource = Action("TagResource")
UnlinkDeveloperIdentity = Action("UnlinkDeveloperIdentity")
UnlinkIdentity = Action("UnlinkIdentity")
UntagResource = Action("UntagResource")
UpdateIdentityPool = Action("UpdateIdentityPool")
