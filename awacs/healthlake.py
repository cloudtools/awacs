# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS HealthLake"
prefix = "healthlake"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelFHIRExportJobWithDelete = Action("CancelFHIRExportJobWithDelete")
ConfirmAttributionList = Action("ConfirmAttributionList")
CreateDataTransformationProfile = Action("CreateDataTransformationProfile")
CreateFHIRDatastore = Action("CreateFHIRDatastore")
CreateResource = Action("CreateResource")
DeleteDataTransformationProfile = Action("DeleteDataTransformationProfile")
DeleteFHIRDatastore = Action("DeleteFHIRDatastore")
DeleteResource = Action("DeleteResource")
DescribeDataTransformationJob = Action("DescribeDataTransformationJob")
DescribeFHIRBulkDeleteJob = Action("DescribeFHIRBulkDeleteJob")
DescribeFHIRBulkMemberMatchJob = Action("DescribeFHIRBulkMemberMatchJob")
DescribeFHIRDatastore = Action("DescribeFHIRDatastore")
DescribeFHIRExportJob = Action("DescribeFHIRExportJob")
DescribeFHIRExportJobWithGet = Action("DescribeFHIRExportJobWithGet")
DescribeFHIRImportJob = Action("DescribeFHIRImportJob")
ExpandValueSetWithGet = Action("ExpandValueSetWithGet")
ExpandValueSetWithPost = Action("ExpandValueSetWithPost")
GenerateDocumentWithGet = Action("GenerateDocumentWithGet")
GenerateDocumentWithPost = Action("GenerateDocumentWithPost")
GetCapabilities = Action("GetCapabilities")
GetDataTransformationProfile = Action("GetDataTransformationProfile")
GetExportedFile = Action("GetExportedFile")
GetHistoryByResourceId = Action("GetHistoryByResourceId")
InquirePreAuthClaim = Action("InquirePreAuthClaim")
ListDataTransformationJobs = Action("ListDataTransformationJobs")
ListDataTransformationProfileVersions = Action("ListDataTransformationProfileVersions")
ListDataTransformationProfiles = Action("ListDataTransformationProfiles")
ListFHIRDatastores = Action("ListFHIRDatastores")
ListFHIRExportJobs = Action("ListFHIRExportJobs")
ListFHIRImportJobs = Action("ListFHIRImportJobs")
ListTagsForResource = Action("ListTagsForResource")
LookupCodeSystemWithGet = Action("LookupCodeSystemWithGet")
LookupCodeSystemWithPost = Action("LookupCodeSystemWithPost")
MemberAdd = Action("MemberAdd")
MemberMatch = Action("MemberMatch")
MemberRemove = Action("MemberRemove")
PatchResource = Action("PatchResource")
ProcessBundle = Action("ProcessBundle")
PublishDataTransformationProfile = Action("PublishDataTransformationProfile")
QuestionnairePackage = Action("QuestionnairePackage")
ReadResource = Action("ReadResource")
RetrieveAttributionStatus = Action("RetrieveAttributionStatus")
SearchEverything = Action("SearchEverything")
SearchWithGet = Action("SearchWithGet")
SearchWithPost = Action("SearchWithPost")
StartDataTransformationJob = Action("StartDataTransformationJob")
StartFHIRBulkDeleteJob = Action("StartFHIRBulkDeleteJob")
StartFHIRBulkMemberMatchJob = Action("StartFHIRBulkMemberMatchJob")
StartFHIRExportJob = Action("StartFHIRExportJob")
StartFHIRExportJobWithGet = Action("StartFHIRExportJobWithGet")
StartFHIRExportJobWithPost = Action("StartFHIRExportJobWithPost")
StartFHIRImportJob = Action("StartFHIRImportJob")
SubmitPreAuthClaim = Action("SubmitPreAuthClaim")
TagResource = Action("TagResource")
TransformData = Action("TransformData")
TranslateConceptMapWithGet = Action("TranslateConceptMapWithGet")
TranslateConceptMapWithPost = Action("TranslateConceptMapWithPost")
UntagResource = Action("UntagResource")
UpdateDataTransformationProfile = Action("UpdateDataTransformationProfile")
UpdateFHIRDatastore = Action("UpdateFHIRDatastore")
UpdateProfileWithAgent = Action("UpdateProfileWithAgent")
UpdateResource = Action("UpdateResource")
ValidateResource = Action("ValidateResource")
ValidateSource = Action("ValidateSource")
VersionReadResource = Action("VersionReadResource")
