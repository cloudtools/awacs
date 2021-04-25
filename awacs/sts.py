# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Security Token Service"
prefix = "sts"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssumeRole = Action("AssumeRole")
AssumeRoleWithSAML = Action("AssumeRoleWithSAML")
AssumeRoleWithWebIdentity = Action("AssumeRoleWithWebIdentity")
DecodeAuthorizationMessage = Action("DecodeAuthorizationMessage")
GetAccessKeyInfo = Action("GetAccessKeyInfo")
GetCallerIdentity = Action("GetCallerIdentity")
GetFederationToken = Action("GetFederationToken")
GetServiceBearerToken = Action("GetServiceBearerToken")
GetSessionToken = Action("GetSessionToken")
SetSourceIdentity = Action("SetSourceIdentity")
TagSession = Action("TagSession")
