# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS HealthOmics"
prefix = "omics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AbortMultipartReadSetUpload = Action("AbortMultipartReadSetUpload")
AcceptShare = Action("AcceptShare")
BatchDeleteReadSet = Action("BatchDeleteReadSet")
CancelAnnotationImportJob = Action("CancelAnnotationImportJob")
CancelRun = Action("CancelRun")
CancelVariantImportJob = Action("CancelVariantImportJob")
CompleteMultipartReadSetUpload = Action("CompleteMultipartReadSetUpload")
CreateAnnotationStore = Action("CreateAnnotationStore")
CreateAnnotationStoreVersion = Action("CreateAnnotationStoreVersion")
CreateMultipartReadSetUpload = Action("CreateMultipartReadSetUpload")
CreateReferenceStore = Action("CreateReferenceStore")
CreateRunCache = Action("CreateRunCache")
CreateRunGroup = Action("CreateRunGroup")
CreateSequenceStore = Action("CreateSequenceStore")
CreateShare = Action("CreateShare")
CreateVariantStore = Action("CreateVariantStore")
CreateWorkflow = Action("CreateWorkflow")
DeleteAnnotationStore = Action("DeleteAnnotationStore")
DeleteAnnotationStoreVersions = Action("DeleteAnnotationStoreVersions")
DeleteReference = Action("DeleteReference")
DeleteReferenceStore = Action("DeleteReferenceStore")
DeleteRun = Action("DeleteRun")
DeleteRunCache = Action("DeleteRunCache")
DeleteRunGroup = Action("DeleteRunGroup")
DeleteS3AccessPolicy = Action("DeleteS3AccessPolicy")
DeleteSequenceStore = Action("DeleteSequenceStore")
DeleteShare = Action("DeleteShare")
DeleteVariantStore = Action("DeleteVariantStore")
DeleteWorkflow = Action("DeleteWorkflow")
GetAnnotationImportJob = Action("GetAnnotationImportJob")
GetAnnotationStore = Action("GetAnnotationStore")
GetAnnotationStoreVersion = Action("GetAnnotationStoreVersion")
GetReadSet = Action("GetReadSet")
GetReadSetActivationJob = Action("GetReadSetActivationJob")
GetReadSetExportJob = Action("GetReadSetExportJob")
GetReadSetImportJob = Action("GetReadSetImportJob")
GetReadSetMetadata = Action("GetReadSetMetadata")
GetReference = Action("GetReference")
GetReferenceImportJob = Action("GetReferenceImportJob")
GetReferenceMetadata = Action("GetReferenceMetadata")
GetReferenceStore = Action("GetReferenceStore")
GetRun = Action("GetRun")
GetRunCache = Action("GetRunCache")
GetRunGroup = Action("GetRunGroup")
GetRunTask = Action("GetRunTask")
GetS3AccessPolicy = Action("GetS3AccessPolicy")
GetSequenceStore = Action("GetSequenceStore")
GetShare = Action("GetShare")
GetVariantImportJob = Action("GetVariantImportJob")
GetVariantStore = Action("GetVariantStore")
GetWorkflow = Action("GetWorkflow")
ListAnnotationImportJobs = Action("ListAnnotationImportJobs")
ListAnnotationStoreVersions = Action("ListAnnotationStoreVersions")
ListAnnotationStores = Action("ListAnnotationStores")
ListMultipartReadSetUploads = Action("ListMultipartReadSetUploads")
ListReadSetActivationJobs = Action("ListReadSetActivationJobs")
ListReadSetExportJobs = Action("ListReadSetExportJobs")
ListReadSetImportJobs = Action("ListReadSetImportJobs")
ListReadSetUploadParts = Action("ListReadSetUploadParts")
ListReadSets = Action("ListReadSets")
ListReferenceImportJobs = Action("ListReferenceImportJobs")
ListReferenceStores = Action("ListReferenceStores")
ListReferences = Action("ListReferences")
ListRunCaches = Action("ListRunCaches")
ListRunGroups = Action("ListRunGroups")
ListRunTasks = Action("ListRunTasks")
ListRuns = Action("ListRuns")
ListSequenceStores = Action("ListSequenceStores")
ListShares = Action("ListShares")
ListTagsForResource = Action("ListTagsForResource")
ListVariantImportJobs = Action("ListVariantImportJobs")
ListVariantStores = Action("ListVariantStores")
ListWorkflows = Action("ListWorkflows")
PutS3AccessPolicy = Action("PutS3AccessPolicy")
StartAnnotationImportJob = Action("StartAnnotationImportJob")
StartReadSetActivationJob = Action("StartReadSetActivationJob")
StartReadSetExportJob = Action("StartReadSetExportJob")
StartReadSetImportJob = Action("StartReadSetImportJob")
StartReferenceImportJob = Action("StartReferenceImportJob")
StartRun = Action("StartRun")
StartVariantImportJob = Action("StartVariantImportJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAnnotationStore = Action("UpdateAnnotationStore")
UpdateAnnotationStoreVersion = Action("UpdateAnnotationStoreVersion")
UpdateRunCache = Action("UpdateRunCache")
UpdateRunGroup = Action("UpdateRunGroup")
UpdateSequenceStore = Action("UpdateSequenceStore")
UpdateVariantStore = Action("UpdateVariantStore")
UpdateWorkflow = Action("UpdateWorkflow")
UploadReadSetPart = Action("UploadReadSetPart")
