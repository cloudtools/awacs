# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Omics"
prefix = "omics"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchDeleteReadSet = Action("BatchDeleteReadSet")
CancelAnnotationImportJob = Action("CancelAnnotationImportJob")
CancelRun = Action("CancelRun")
CancelVariantImportJob = Action("CancelVariantImportJob")
CreateAnnotationStore = Action("CreateAnnotationStore")
CreateReferenceStore = Action("CreateReferenceStore")
CreateRunGroup = Action("CreateRunGroup")
CreateSequenceStore = Action("CreateSequenceStore")
CreateVariantStore = Action("CreateVariantStore")
CreateWorkflow = Action("CreateWorkflow")
DeleteAnnotationStore = Action("DeleteAnnotationStore")
DeleteReference = Action("DeleteReference")
DeleteReferenceStore = Action("DeleteReferenceStore")
DeleteRun = Action("DeleteRun")
DeleteRunGroup = Action("DeleteRunGroup")
DeleteSequenceStore = Action("DeleteSequenceStore")
DeleteVariantStore = Action("DeleteVariantStore")
DeleteWorkflow = Action("DeleteWorkflow")
GetAnnotationImportJob = Action("GetAnnotationImportJob")
GetAnnotationStore = Action("GetAnnotationStore")
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
GetRunGroup = Action("GetRunGroup")
GetRunTask = Action("GetRunTask")
GetSequenceStore = Action("GetSequenceStore")
GetVariantImportJob = Action("GetVariantImportJob")
GetVariantStore = Action("GetVariantStore")
GetWorkflow = Action("GetWorkflow")
ListAnnotationImportJobs = Action("ListAnnotationImportJobs")
ListAnnotationStores = Action("ListAnnotationStores")
ListReadSetActivationJobs = Action("ListReadSetActivationJobs")
ListReadSetExportJobs = Action("ListReadSetExportJobs")
ListReadSetImportJobs = Action("ListReadSetImportJobs")
ListReadSets = Action("ListReadSets")
ListReferenceImportJobs = Action("ListReferenceImportJobs")
ListReferenceStores = Action("ListReferenceStores")
ListReferences = Action("ListReferences")
ListRunGroups = Action("ListRunGroups")
ListRunTasks = Action("ListRunTasks")
ListRuns = Action("ListRuns")
ListSequenceStores = Action("ListSequenceStores")
ListTagsForResource = Action("ListTagsForResource")
ListVariantImportJobs = Action("ListVariantImportJobs")
ListVariantStores = Action("ListVariantStores")
ListWorkflows = Action("ListWorkflows")
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
UpdateRunGroup = Action("UpdateRunGroup")
UpdateVariantStore = Action("UpdateVariantStore")
UpdateWorkflow = Action("UpdateWorkflow")
