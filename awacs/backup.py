# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Backup"
prefix = "backup"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelLegalHold = Action("CancelLegalHold")
CopyFromBackupVault = Action("CopyFromBackupVault")
CopyIntoBackupVault = Action("CopyIntoBackupVault")
CreateBackupPlan = Action("CreateBackupPlan")
CreateBackupSelection = Action("CreateBackupSelection")
CreateBackupVault = Action("CreateBackupVault")
CreateFramework = Action("CreateFramework")
CreateLegalHold = Action("CreateLegalHold")
CreateLogicallyAirGappedBackupVault = Action("CreateLogicallyAirGappedBackupVault")
CreateReportPlan = Action("CreateReportPlan")
CreateRestoreTestingPlan = Action("CreateRestoreTestingPlan")
CreateRestoreTestingSelection = Action("CreateRestoreTestingSelection")
DeleteBackupPlan = Action("DeleteBackupPlan")
DeleteBackupSelection = Action("DeleteBackupSelection")
DeleteBackupVault = Action("DeleteBackupVault")
DeleteBackupVaultAccessPolicy = Action("DeleteBackupVaultAccessPolicy")
DeleteBackupVaultLockConfiguration = Action("DeleteBackupVaultLockConfiguration")
DeleteBackupVaultNotifications = Action("DeleteBackupVaultNotifications")
DeleteBackupVaultSharingPolicy = Action("DeleteBackupVaultSharingPolicy")
DeleteFramework = Action("DeleteFramework")
DeleteRecoveryPoint = Action("DeleteRecoveryPoint")
DeleteReportPlan = Action("DeleteReportPlan")
DeleteRestoreTestingPlan = Action("DeleteRestoreTestingPlan")
DeleteRestoreTestingSelection = Action("DeleteRestoreTestingSelection")
DescribeBackupJob = Action("DescribeBackupJob")
DescribeBackupVault = Action("DescribeBackupVault")
DescribeCopyJob = Action("DescribeCopyJob")
DescribeFramework = Action("DescribeFramework")
DescribeGlobalSettings = Action("DescribeGlobalSettings")
DescribeProtectedResource = Action("DescribeProtectedResource")
DescribeRecoveryPoint = Action("DescribeRecoveryPoint")
DescribeRegionSettings = Action("DescribeRegionSettings")
DescribeReportJob = Action("DescribeReportJob")
DescribeReportPlan = Action("DescribeReportPlan")
DescribeRestoreJob = Action("DescribeRestoreJob")
DisassociateRecoveryPoint = Action("DisassociateRecoveryPoint")
DisassociateRecoveryPointFromParent = Action("DisassociateRecoveryPointFromParent")
ExportBackupPlanTemplate = Action("ExportBackupPlanTemplate")
GetBackupPlan = Action("GetBackupPlan")
GetBackupPlanFromJSON = Action("GetBackupPlanFromJSON")
GetBackupPlanFromTemplate = Action("GetBackupPlanFromTemplate")
GetBackupSelection = Action("GetBackupSelection")
GetBackupVaultAccessPolicy = Action("GetBackupVaultAccessPolicy")
GetBackupVaultNotifications = Action("GetBackupVaultNotifications")
GetBackupVaultSharingPolicy = Action("GetBackupVaultSharingPolicy")
GetLegalHold = Action("GetLegalHold")
GetRecoveryPointRestoreMetadata = Action("GetRecoveryPointRestoreMetadata")
GetRestoreJobMetadata = Action("GetRestoreJobMetadata")
GetRestoreTestingInferredMetadata = Action("GetRestoreTestingInferredMetadata")
GetRestoreTestingPlan = Action("GetRestoreTestingPlan")
GetRestoreTestingSelection = Action("GetRestoreTestingSelection")
GetSupportedResourceTypes = Action("GetSupportedResourceTypes")
ListBackupJobSummaries = Action("ListBackupJobSummaries")
ListBackupJobs = Action("ListBackupJobs")
ListBackupPlanTemplates = Action("ListBackupPlanTemplates")
ListBackupPlanVersions = Action("ListBackupPlanVersions")
ListBackupPlans = Action("ListBackupPlans")
ListBackupSelections = Action("ListBackupSelections")
ListBackupVaults = Action("ListBackupVaults")
ListCopyJobSummaries = Action("ListCopyJobSummaries")
ListCopyJobs = Action("ListCopyJobs")
ListFrameworks = Action("ListFrameworks")
ListLegalHolds = Action("ListLegalHolds")
ListProtectedResources = Action("ListProtectedResources")
ListProtectedResourcesByBackupVault = Action("ListProtectedResourcesByBackupVault")
ListRecoveryPointsByBackupVault = Action("ListRecoveryPointsByBackupVault")
ListRecoveryPointsByLegalHold = Action("ListRecoveryPointsByLegalHold")
ListRecoveryPointsByResource = Action("ListRecoveryPointsByResource")
ListReportJobs = Action("ListReportJobs")
ListReportPlans = Action("ListReportPlans")
ListRestoreJobSummaries = Action("ListRestoreJobSummaries")
ListRestoreJobs = Action("ListRestoreJobs")
ListRestoreJobsByProtectedResource = Action("ListRestoreJobsByProtectedResource")
ListRestoreTestingPlans = Action("ListRestoreTestingPlans")
ListRestoreTestingSelections = Action("ListRestoreTestingSelections")
ListTags = Action("ListTags")
PutBackupVaultAccessPolicy = Action("PutBackupVaultAccessPolicy")
PutBackupVaultLockConfiguration = Action("PutBackupVaultLockConfiguration")
PutBackupVaultNotifications = Action("PutBackupVaultNotifications")
PutBackupVaultSharingPolicy = Action("PutBackupVaultSharingPolicy")
PutRestoreValidationResult = Action("PutRestoreValidationResult")
StartBackupJob = Action("StartBackupJob")
StartCopyJob = Action("StartCopyJob")
StartReportJob = Action("StartReportJob")
StartRestoreJob = Action("StartRestoreJob")
StopBackupJob = Action("StopBackupJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBackupPlan = Action("UpdateBackupPlan")
UpdateFramework = Action("UpdateFramework")
UpdateGlobalSettings = Action("UpdateGlobalSettings")
UpdateRecoveryPointLifecycle = Action("UpdateRecoveryPointLifecycle")
UpdateRegionSettings = Action("UpdateRegionSettings")
UpdateReportPlan = Action("UpdateReportPlan")
UpdateRestoreTestingPlan = Action("UpdateRestoreTestingPlan")
UpdateRestoreTestingSelection = Action("UpdateRestoreTestingSelection")
