# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support App in Slack"
prefix = "supportapp"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateSlackChannelConfiguration = Action("CreateSlackChannelConfiguration")
DeleteAccountAlias = Action("DeleteAccountAlias")
DeleteSlackChannelConfiguration = Action("DeleteSlackChannelConfiguration")
DeleteSlackWorkspaceConfiguration = Action("DeleteSlackWorkspaceConfiguration")
DescribeSlackChannels = Action("DescribeSlackChannels")
GetAccountAlias = Action("GetAccountAlias")
GetSlackOauthParameters = Action("GetSlackOauthParameters")
ListSlackChannelConfigurations = Action("ListSlackChannelConfigurations")
ListSlackWorkspaceConfigurations = Action("ListSlackWorkspaceConfigurations")
PutAccountAlias = Action("PutAccountAlias")
RedeemSlackOauthCode = Action("RedeemSlackOauthCode")
RegisterSlackWorkspaceForOrganization = Action("RegisterSlackWorkspaceForOrganization")
UpdateSlackChannelConfiguration = Action("UpdateSlackChannelConfiguration")
