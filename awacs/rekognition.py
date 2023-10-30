# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Rekognition"
prefix = "rekognition"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateFaces = Action("AssociateFaces")
CompareFaces = Action("CompareFaces")
CopyProjectVersion = Action("CopyProjectVersion")
CreateCollection = Action("CreateCollection")
CreateDataset = Action("CreateDataset")
CreateFaceLivenessSession = Action("CreateFaceLivenessSession")
CreateProject = Action("CreateProject")
CreateProjectVersion = Action("CreateProjectVersion")
CreateStreamProcessor = Action("CreateStreamProcessor")
CreateUser = Action("CreateUser")
DeleteCollection = Action("DeleteCollection")
DeleteDataset = Action("DeleteDataset")
DeleteFaces = Action("DeleteFaces")
DeleteProject = Action("DeleteProject")
DeleteProjectPolicy = Action("DeleteProjectPolicy")
DeleteProjectVersion = Action("DeleteProjectVersion")
DeleteStreamProcessor = Action("DeleteStreamProcessor")
DeleteUser = Action("DeleteUser")
DescribeCollection = Action("DescribeCollection")
DescribeDataset = Action("DescribeDataset")
DescribeProjectVersions = Action("DescribeProjectVersions")
DescribeProjects = Action("DescribeProjects")
DescribeStreamProcessor = Action("DescribeStreamProcessor")
DetectCustomLabels = Action("DetectCustomLabels")
DetectFaces = Action("DetectFaces")
DetectLabels = Action("DetectLabels")
DetectModerationLabels = Action("DetectModerationLabels")
DetectProtectiveEquipment = Action("DetectProtectiveEquipment")
DetectText = Action("DetectText")
DisassociateFaces = Action("DisassociateFaces")
DistributeDatasetEntries = Action("DistributeDatasetEntries")
GetCelebrityInfo = Action("GetCelebrityInfo")
GetCelebrityRecognition = Action("GetCelebrityRecognition")
GetContentModeration = Action("GetContentModeration")
GetFaceDetection = Action("GetFaceDetection")
GetFaceLivenessSessionResults = Action("GetFaceLivenessSessionResults")
GetFaceSearch = Action("GetFaceSearch")
GetLabelDetection = Action("GetLabelDetection")
GetMediaAnalysisJob = Action("GetMediaAnalysisJob")
GetPersonTracking = Action("GetPersonTracking")
GetSegmentDetection = Action("GetSegmentDetection")
GetTextDetection = Action("GetTextDetection")
IndexFaces = Action("IndexFaces")
ListCollections = Action("ListCollections")
ListDatasetEntries = Action("ListDatasetEntries")
ListDatasetLabels = Action("ListDatasetLabels")
ListFaces = Action("ListFaces")
ListMediaAnalysisJobs = Action("ListMediaAnalysisJobs")
ListProjectPolicies = Action("ListProjectPolicies")
ListStreamProcessors = Action("ListStreamProcessors")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
PutProjectPolicy = Action("PutProjectPolicy")
RecognizeCelebrities = Action("RecognizeCelebrities")
SearchFaces = Action("SearchFaces")
SearchFacesByImage = Action("SearchFacesByImage")
SearchUsers = Action("SearchUsers")
SearchUsersByImage = Action("SearchUsersByImage")
StartCelebrityRecognition = Action("StartCelebrityRecognition")
StartContentModeration = Action("StartContentModeration")
StartFaceDetection = Action("StartFaceDetection")
StartFaceLivenessSession = Action("StartFaceLivenessSession")
StartFaceSearch = Action("StartFaceSearch")
StartLabelDetection = Action("StartLabelDetection")
StartMediaAnalysisJob = Action("StartMediaAnalysisJob")
StartPersonTracking = Action("StartPersonTracking")
StartProjectVersion = Action("StartProjectVersion")
StartSegmentDetection = Action("StartSegmentDetection")
StartStreamProcessor = Action("StartStreamProcessor")
StartTextDetection = Action("StartTextDetection")
StopProjectVersion = Action("StopProjectVersion")
StopStreamProcessor = Action("StopStreamProcessor")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDatasetEntries = Action("UpdateDatasetEntries")
UpdateStreamProcessor = Action("UpdateStreamProcessor")
