# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon GameSparks"
prefix = "gamesparks"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateGame = Action("CreateGame")
CreateSnapshot = Action("CreateSnapshot")
CreateStage = Action("CreateStage")
DeleteGame = Action("DeleteGame")
DeleteStage = Action("DeleteStage")
DisconnectPlayer = Action("DisconnectPlayer")
ExportSnapshot = Action("ExportSnapshot")
GetExtension = Action("GetExtension")
GetExtensionVersion = Action("GetExtensionVersion")
GetGame = Action("GetGame")
GetGameConfiguration = Action("GetGameConfiguration")
GetGeneratedCodeJob = Action("GetGeneratedCodeJob")
GetPlayerConnectionStatus = Action("GetPlayerConnectionStatus")
GetSnapshot = Action("GetSnapshot")
GetStage = Action("GetStage")
GetStageDeployment = Action("GetStageDeployment")
ImportGameConfiguration = Action("ImportGameConfiguration")
InvokeBackend = Action("InvokeBackend")
ListExtensionVersions = Action("ListExtensionVersions")
ListExtensions = Action("ListExtensions")
ListGames = Action("ListGames")
ListGeneratedCodeJobs = Action("ListGeneratedCodeJobs")
ListSnapshots = Action("ListSnapshots")
ListStageDeployments = Action("ListStageDeployments")
ListStages = Action("ListStages")
ListTagsForResource = Action("ListTagsForResource")
StartGeneratedCodeJob = Action("StartGeneratedCodeJob")
StartStageDeployment = Action("StartStageDeployment")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGame = Action("UpdateGame")
UpdateGameConfiguration = Action("UpdateGameConfiguration")
UpdateSnapshot = Action("UpdateSnapshot")
UpdateStage = Action("UpdateStage")
