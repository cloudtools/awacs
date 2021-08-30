# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Backup"
prefix = "backup"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CopyFromBackupVault = Action("CopyFromBackupVault")
CopyIntoBackupVault = Action("CopyIntoBackupVault")
CreateBackupPlan = Action("CreateBackupPlan")
CreateBackupSelection = Action("CreateBackupSelection")
CreateBackupVault = Action("CreateBackupVault")
CreateFramework = Action("CreateFramework")
CreateReportPlan = Action("CreateReportPlan")
DeleteBackupPlan = Action("DeleteBackupPlan")
DeleteBackupSelection = Action("DeleteBackupSelection")
DeleteBackupVault = Action("DeleteBackupVault")
DeleteBackupVaultAccessPolicy = Action("DeleteBackupVaultAccessPolicy")
DeleteBackupVaultNotifications = Action("DeleteBackupVaultNotifications")
DeleteFramework = Action("DeleteFramework")
DeleteRecoveryPoint = Action("DeleteRecoveryPoint")
DeleteReportPlan = Action("DeleteReportPlan")
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
ExportBackupPlanTemplate = Action("ExportBackupPlanTemplate")
GetBackupPlan = Action("GetBackupPlan")
GetBackupPlanFromJSON = Action("GetBackupPlanFromJSON")
GetBackupPlanFromTemplate = Action("GetBackupPlanFromTemplate")
GetBackupSelection = Action("GetBackupSelection")
GetBackupVaultAccessPolicy = Action("GetBackupVaultAccessPolicy")
GetBackupVaultNotifications = Action("GetBackupVaultNotifications")
GetRecoveryPointRestoreMetadata = Action("GetRecoveryPointRestoreMetadata")
GetSupportedResourceTypes = Action("GetSupportedResourceTypes")
ListBackupJobs = Action("ListBackupJobs")
ListBackupPlanTemplates = Action("ListBackupPlanTemplates")
ListBackupPlanVersions = Action("ListBackupPlanVersions")
ListBackupPlans = Action("ListBackupPlans")
ListBackupSelections = Action("ListBackupSelections")
ListBackupVaults = Action("ListBackupVaults")
ListCopyJobs = Action("ListCopyJobs")
ListFrameworks = Action("ListFrameworks")
ListProtectedResources = Action("ListProtectedResources")
ListRecoveryPointsByBackupVault = Action("ListRecoveryPointsByBackupVault")
ListRecoveryPointsByResource = Action("ListRecoveryPointsByResource")
ListReportJobs = Action("ListReportJobs")
ListReportPlans = Action("ListReportPlans")
ListRestoreJobs = Action("ListRestoreJobs")
ListTags = Action("ListTags")
PutBackupVaultAccessPolicy = Action("PutBackupVaultAccessPolicy")
PutBackupVaultNotifications = Action("PutBackupVaultNotifications")
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
