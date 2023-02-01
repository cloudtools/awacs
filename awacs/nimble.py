# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Nimble Studio"
prefix = "nimble"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptEulas = Action("AcceptEulas")
CreateLaunchProfile = Action("CreateLaunchProfile")
CreateStreamingImage = Action("CreateStreamingImage")
CreateStreamingSession = Action("CreateStreamingSession")
CreateStreamingSessionStream = Action("CreateStreamingSessionStream")
CreateStudio = Action("CreateStudio")
CreateStudioComponent = Action("CreateStudioComponent")
DeleteLaunchProfile = Action("DeleteLaunchProfile")
DeleteLaunchProfileMember = Action("DeleteLaunchProfileMember")
DeleteStreamingImage = Action("DeleteStreamingImage")
DeleteStreamingSession = Action("DeleteStreamingSession")
DeleteStudio = Action("DeleteStudio")
DeleteStudioComponent = Action("DeleteStudioComponent")
DeleteStudioMember = Action("DeleteStudioMember")
GetEula = Action("GetEula")
GetFeatureMap = Action("GetFeatureMap")
GetLaunchProfile = Action("GetLaunchProfile")
GetLaunchProfileDetails = Action("GetLaunchProfileDetails")
GetLaunchProfileInitialization = Action("GetLaunchProfileInitialization")
GetLaunchProfileMember = Action("GetLaunchProfileMember")
GetStreamingImage = Action("GetStreamingImage")
GetStreamingSession = Action("GetStreamingSession")
GetStreamingSessionBackup = Action("GetStreamingSessionBackup")
GetStreamingSessionStream = Action("GetStreamingSessionStream")
GetStudio = Action("GetStudio")
GetStudioComponent = Action("GetStudioComponent")
GetStudioMember = Action("GetStudioMember")
ListEulaAcceptances = Action("ListEulaAcceptances")
ListEulas = Action("ListEulas")
ListLaunchProfileMembers = Action("ListLaunchProfileMembers")
ListLaunchProfiles = Action("ListLaunchProfiles")
ListStreamingImages = Action("ListStreamingImages")
ListStreamingSessionBackups = Action("ListStreamingSessionBackups")
ListStreamingSessions = Action("ListStreamingSessions")
ListStudioComponents = Action("ListStudioComponents")
ListStudioMembers = Action("ListStudioMembers")
ListStudios = Action("ListStudios")
ListTagsForResource = Action("ListTagsForResource")
PutLaunchProfileMembers = Action("PutLaunchProfileMembers")
PutStudioLogEvents = Action("PutStudioLogEvents")
PutStudioMembers = Action("PutStudioMembers")
StartStreamingSession = Action("StartStreamingSession")
StartStudioSSOConfigurationRepair = Action("StartStudioSSOConfigurationRepair")
StopStreamingSession = Action("StopStreamingSession")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLaunchProfile = Action("UpdateLaunchProfile")
UpdateLaunchProfileMember = Action("UpdateLaunchProfileMember")
UpdateStreamingImage = Action("UpdateStreamingImage")
UpdateStudio = Action("UpdateStudio")
UpdateStudioComponent = Action("UpdateStudioComponent")
