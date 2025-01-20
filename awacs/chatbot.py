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


AssociateToConfiguration = Action("AssociateToConfiguration")
CreateChimeWebhookConfiguration = Action("CreateChimeWebhookConfiguration")
CreateCustomAction = Action("CreateCustomAction")
CreateMicrosoftTeamsChannelConfiguration = Action(
    "CreateMicrosoftTeamsChannelConfiguration"
)
CreateSlackChannelConfiguration = Action("CreateSlackChannelConfiguration")
DeleteChimeWebhookConfiguration = Action("DeleteChimeWebhookConfiguration")
DeleteCustomAction = Action("DeleteCustomAction")
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
DisassociateFromConfiguration = Action("DisassociateFromConfiguration")
GetAccountPreferences = Action("GetAccountPreferences")
GetCustomAction = Action("GetCustomAction")
GetMicrosoftTeamsChannelConfiguration = Action("GetMicrosoftTeamsChannelConfiguration")
GetMicrosoftTeamsOauthParameters = Action("GetMicrosoftTeamsOauthParameters")
GetSlackOauthParameters = Action("GetSlackOauthParameters")
ListAssociations = Action("ListAssociations")
ListCustomActions = Action("ListCustomActions")
ListMicrosoftTeamsChannelConfigurations = Action(
    "ListMicrosoftTeamsChannelConfigurations"
)
ListMicrosoftTeamsConfiguredTeams = Action("ListMicrosoftTeamsConfiguredTeams")
ListMicrosoftTeamsUserIdentities = Action("ListMicrosoftTeamsUserIdentities")
ListTagsForResource = Action("ListTagsForResource")
RedeemMicrosoftTeamsOauthCode = Action("RedeemMicrosoftTeamsOauthCode")
RedeemSlackOauthCode = Action("RedeemSlackOauthCode")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccountPreferences = Action("UpdateAccountPreferences")
UpdateChimeWebhookConfiguration = Action("UpdateChimeWebhookConfiguration")
UpdateCustomAction = Action("UpdateCustomAction")
UpdateMicrosoftTeamsChannelConfiguration = Action(
    "UpdateMicrosoftTeamsChannelConfiguration"
)
UpdateSlackChannelConfiguration = Action("UpdateSlackChannelConfiguration")
