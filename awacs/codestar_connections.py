# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodeStar Connections"
prefix = "codestar-connections"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateConnection = Action("CreateConnection")
CreateHost = Action("CreateHost")
CreateRepositoryLink = Action("CreateRepositoryLink")
CreateSyncConfiguration = Action("CreateSyncConfiguration")
DeleteConnection = Action("DeleteConnection")
DeleteHost = Action("DeleteHost")
DeleteRepositoryLink = Action("DeleteRepositoryLink")
DeleteSyncConfiguration = Action("DeleteSyncConfiguration")
GetConnection = Action("GetConnection")
GetConnectionToken = Action("GetConnectionToken")
GetHost = Action("GetHost")
GetIndividualAccessToken = Action("GetIndividualAccessToken")
GetInstallationUrl = Action("GetInstallationUrl")
GetRepositoryLink = Action("GetRepositoryLink")
GetRepositorySyncStatus = Action("GetRepositorySyncStatus")
GetResourceSyncStatus = Action("GetResourceSyncStatus")
GetSyncBlockerSummary = Action("GetSyncBlockerSummary")
GetSyncConfiguration = Action("GetSyncConfiguration")
ListConnections = Action("ListConnections")
ListHosts = Action("ListHosts")
ListInstallationTargets = Action("ListInstallationTargets")
ListRepositoryLinks = Action("ListRepositoryLinks")
ListRepositorySyncDefinitions = Action("ListRepositorySyncDefinitions")
ListSyncConfigurations = Action("ListSyncConfigurations")
ListTagsForResource = Action("ListTagsForResource")
PassConnection = Action("PassConnection")
PassRepository = Action("PassRepository")
RegisterAppCode = Action("RegisterAppCode")
StartAppRegistrationHandshake = Action("StartAppRegistrationHandshake")
StartOAuthHandshake = Action("StartOAuthHandshake")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnectionInstallation = Action("UpdateConnectionInstallation")
UpdateHost = Action("UpdateHost")
UpdateRepositoryLink = Action("UpdateRepositoryLink")
UpdateSyncBlocker = Action("UpdateSyncBlocker")
UpdateSyncConfiguration = Action("UpdateSyncConfiguration")
UseConnection = Action("UseConnection")
