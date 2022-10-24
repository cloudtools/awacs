# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Support App for Slack"
prefix = "supportapp"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
GetAccountAlias = Action("GetAccountAlias")
ListSlackChannelConfigurations = Action("ListSlackChannelConfigurations")
ListSlackWorkspaceConfigurations = Action("ListSlackWorkspaceConfigurations")
PutAccountAlias = Action("PutAccountAlias")
RegisterSlackWorkspaceForOrganization = Action("RegisterSlackWorkspaceForOrganization")
UpdateSlackChannelConfiguration = Action("UpdateSlackChannelConfiguration")
