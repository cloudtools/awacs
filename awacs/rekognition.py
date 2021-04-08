# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Rekognition"
prefix = "rekognition"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CompareFaces = Action("CompareFaces")
CreateCollection = Action("CreateCollection")
CreateProject = Action("CreateProject")
CreateProjectVersion = Action("CreateProjectVersion")
CreateStreamProcessor = Action("CreateStreamProcessor")
DeleteCollection = Action("DeleteCollection")
DeleteFaces = Action("DeleteFaces")
DeleteProject = Action("DeleteProject")
DeleteProjectVersion = Action("DeleteProjectVersion")
DeleteStreamProcessor = Action("DeleteStreamProcessor")
DescribeCollection = Action("DescribeCollection")
DescribeProjectVersions = Action("DescribeProjectVersions")
DescribeProjects = Action("DescribeProjects")
DescribeStreamProcessor = Action("DescribeStreamProcessor")
DetectCustomLabels = Action("DetectCustomLabels")
DetectFaces = Action("DetectFaces")
DetectLabels = Action("DetectLabels")
DetectModerationLabels = Action("DetectModerationLabels")
DetectProtectiveEquipment = Action("DetectProtectiveEquipment")
DetectText = Action("DetectText")
GetCelebrityInfo = Action("GetCelebrityInfo")
GetCelebrityRecognition = Action("GetCelebrityRecognition")
GetContentModeration = Action("GetContentModeration")
GetFaceDetection = Action("GetFaceDetection")
GetFaceSearch = Action("GetFaceSearch")
GetLabelDetection = Action("GetLabelDetection")
GetPersonTracking = Action("GetPersonTracking")
GetSegmentDetection = Action("GetSegmentDetection")
GetTextDetection = Action("GetTextDetection")
IndexFaces = Action("IndexFaces")
ListCollections = Action("ListCollections")
ListFaces = Action("ListFaces")
ListStreamProcessors = Action("ListStreamProcessors")
ListTagsForResource = Action("ListTagsForResource")
RecognizeCelebrities = Action("RecognizeCelebrities")
SearchFaces = Action("SearchFaces")
SearchFacesByImage = Action("SearchFacesByImage")
StartCelebrityRecognition = Action("StartCelebrityRecognition")
StartContentModeration = Action("StartContentModeration")
StartFaceDetection = Action("StartFaceDetection")
StartFaceSearch = Action("StartFaceSearch")
StartLabelDetection = Action("StartLabelDetection")
StartPersonTracking = Action("StartPersonTracking")
StartProjectVersion = Action("StartProjectVersion")
StartSegmentDetection = Action("StartSegmentDetection")
StartStreamProcessor = Action("StartStreamProcessor")
StartTextDetection = Action("StartTextDetection")
StopProjectVersion = Action("StopProjectVersion")
StopStreamProcessor = Action("StopStreamProcessor")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
