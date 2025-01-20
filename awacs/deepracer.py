# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DeepRacer"
prefix = "deepracer"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddLeaderboardAccessPermission = Action("AddLeaderboardAccessPermission")
AdminDescribeAccountKey = Action("AdminDescribeAccountKey")
AdminGetAccountConfig = Action("AdminGetAccountConfig")
AdminListAssociatedResources = Action("AdminListAssociatedResources")
AdminListAssociatedUsers = Action("AdminListAssociatedUsers")
AdminManageUser = Action("AdminManageUser")
AdminSetAccountConfig = Action("AdminSetAccountConfig")
AdminUpdateAccountKey = Action("AdminUpdateAccountKey")
CloneReinforcementLearningModel = Action("CloneReinforcementLearningModel")
CreateAccountResources = Action("CreateAccountResources")
CreateCar = Action("CreateCar")
CreateLeaderboard = Action("CreateLeaderboard")
CreateLeaderboardAccessToken = Action("CreateLeaderboardAccessToken")
CreateLeaderboardSubmission = Action("CreateLeaderboardSubmission")
CreateReinforcementLearningModel = Action("CreateReinforcementLearningModel")
DeleteAccountResources = Action("DeleteAccountResources")
DeleteLeaderboard = Action("DeleteLeaderboard")
DeleteModel = Action("DeleteModel")
EditLeaderboard = Action("EditLeaderboard")
GetAccountConfig = Action("GetAccountConfig")
GetAccountResources = Action("GetAccountResources")
GetAlias = Action("GetAlias")
GetAssetUrl = Action("GetAssetUrl")
GetCar = Action("GetCar")
GetCars = Action("GetCars")
GetEvaluation = Action("GetEvaluation")
GetLatestUserSubmission = Action("GetLatestUserSubmission")
GetLeaderboard = Action("GetLeaderboard")
GetModel = Action("GetModel")
GetPrivateLeaderboard = Action("GetPrivateLeaderboard")
GetRankedUserSubmission = Action("GetRankedUserSubmission")
GetTrack = Action("GetTrack")
GetTrainingJob = Action("GetTrainingJob")
ImportModel = Action("ImportModel")
ListEvaluations = Action("ListEvaluations")
ListLeaderboardEvaluations = Action("ListLeaderboardEvaluations")
ListLeaderboardSubmissions = Action("ListLeaderboardSubmissions")
ListLeaderboards = Action("ListLeaderboards")
ListModels = Action("ListModels")
ListPrivateLeaderboardParticipants = Action("ListPrivateLeaderboardParticipants")
ListPrivateLeaderboards = Action("ListPrivateLeaderboards")
ListSubscribedPrivateLeaderboards = Action("ListSubscribedPrivateLeaderboards")
ListTagsForResource = Action("ListTagsForResource")
ListTracks = Action("ListTracks")
ListTrainingJobs = Action("ListTrainingJobs")
MigrateModels = Action("MigrateModels")
PerformLeaderboardOperation = Action("PerformLeaderboardOperation")
RemoveLeaderboardAccessPermission = Action("RemoveLeaderboardAccessPermission")
SetAlias = Action("SetAlias")
StartEvaluation = Action("StartEvaluation")
StopEvaluation = Action("StopEvaluation")
StopTrainingReinforcementLearningModel = Action(
    "StopTrainingReinforcementLearningModel"
)
TagResource = Action("TagResource")
TestRewardFunction = Action("TestRewardFunction")
UntagResource = Action("UntagResource")
UpdateCar = Action("UpdateCar")
