# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Chatbot"
prefix = "chatbot"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateChimeWebhookConfiguration = Action("CreateChimeWebhookConfiguration")
CreateMicrosoftTeamsChannelConfiguration = Action(
    "CreateMicrosoftTeamsChannelConfiguration"
)
CreateSlackChannelConfiguration = Action("CreateSlackChannelConfiguration")
DeleteChimeWebhookConfiguration = Action("DeleteChimeWebhookConfiguration")
DeleteMicrosoftTeamsChannelConfiguration = Action(
    "DeleteMicrosoftTeamsChannelConfiguration"
)
DeleteMicrosoftTeamsConfiguredTeam = Action("DeleteMicrosoftTeamsConfiguredTeam")
DeleteMicrosoftTeamsUserIdentity = Action("DeleteMicrosoftTeamsUserIdentity")
DeleteSlackChannelConfiguration = Action("DeleteSlackChannelConfiguration")
DeleteSlackUserIdentity = Action("DeleteSlackUserIdentity")
DeleteSlackWorkspaceAuthorization = Action("DeleteSlackWorkspaceAuthorization")
DescribeChimeWebhookConfigurations = Action("DescribeChimeWebhookConfigurations")
DescribeSlackChannelConfigurations = Action("DescribeSlackChannelConfigurations")
DescribeSlackChannels = Action("DescribeSlackChannels")
DescribeSlackUserIdentities = Action("DescribeSlackUserIdentities")
DescribeSlackWorkspaces = Action("DescribeSlackWorkspaces")
GetAccountPreferences = Action("GetAccountPreferences")
GetMicrosoftTeamsChannelConfiguration = Action("GetMicrosoftTeamsChannelConfiguration")
GetMicrosoftTeamsOauthParameters = Action("GetMicrosoftTeamsOauthParameters")
GetSlackOauthParameters = Action("GetSlackOauthParameters")
ListMicrosoftTeamsChannelConfigurations = Action(
    "ListMicrosoftTeamsChannelConfigurations"
)
ListMicrosoftTeamsConfiguredTeams = Action("ListMicrosoftTeamsConfiguredTeams")
ListMicrosoftTeamsUserIdentities = Action("ListMicrosoftTeamsUserIdentities")
RedeemMicrosoftTeamsOauthCode = Action("RedeemMicrosoftTeamsOauthCode")
RedeemSlackOauthCode = Action("RedeemSlackOauthCode")
UpdateAccountPreferences = Action("UpdateAccountPreferences")
UpdateChimeWebhookConfiguration = Action("UpdateChimeWebhookConfiguration")
UpdateMicrosoftTeamsChannelConfiguration = Action(
    "UpdateMicrosoftTeamsChannelConfiguration"
)
UpdateSlackChannelConfiguration = Action("UpdateSlackChannelConfiguration")
