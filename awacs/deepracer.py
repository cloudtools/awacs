# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DeepRacer"
prefix = "deepracer"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CloneReinforcementLearningModel = Action("CloneReinforcementLearningModel")
CreateAccountResources = Action("CreateAccountResources")
CreateLeaderboardSubmission = Action("CreateLeaderboardSubmission")
CreateReinforcementLearningModel = Action("CreateReinforcementLearningModel")
DeleteAccountResources = Action("DeleteAccountResources")
DeleteModel = Action("DeleteModel")
GetAccountResources = Action("GetAccountResources")
GetAlias = Action("GetAlias")
GetEvaluation = Action("GetEvaluation")
GetLatestUserSubmission = Action("GetLatestUserSubmission")
GetLeaderboard = Action("GetLeaderboard")
GetModel = Action("GetModel")
GetRankedUserSubmission = Action("GetRankedUserSubmission")
GetTrack = Action("GetTrack")
GetTrainingJob = Action("GetTrainingJob")
ListEvaluations = Action("ListEvaluations")
ListLeaderboardSubmissions = Action("ListLeaderboardSubmissions")
ListLeaderboards = Action("ListLeaderboards")
ListModels = Action("ListModels")
ListTracks = Action("ListTracks")
ListTrainingJobs = Action("ListTrainingJobs")
SetAlias = Action("SetAlias")
StartEvaluation = Action("StartEvaluation")
StopEvaluation = Action("StopEvaluation")
StopTrainingReinforcementLearningModel = Action(
    "StopTrainingReinforcementLearningModel"
)
TestRewardFunction = Action("TestRewardFunction")
