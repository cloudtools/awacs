# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Backup'
prefix = 'backup'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateBackupPlan = Action('CreateBackupPlan')
CreateBackupSelection = Action('CreateBackupSelection')
CreateBackupVault = Action('CreateBackupVault')
DeleteBackupPlan = Action('DeleteBackupPlan')
DeleteBackupSelection = Action('DeleteBackupSelection')
DeleteBackupVault = Action('DeleteBackupVault')
DeleteBackupVaultAccessPolicy = Action('DeleteBackupVaultAccessPolicy')
DeleteBackupVaultNotifications = Action('DeleteBackupVaultNotifications')
DeleteRecoveryPoint = Action('DeleteRecoveryPoint')
DescribeBackupJob = Action('DescribeBackupJob')
DescribeBackupVault = Action('DescribeBackupVault')
DescribeProtectedResource = Action('DescribeProtectedResource')
DescribeRecoveryPoint = Action('DescribeRecoveryPoint')
DescribeRestoreJob = Action('DescribeRestoreJob')
ExportBackupPlanTemplate = Action('ExportBackupPlanTemplate')
GetBackupPlan = Action('GetBackupPlan')
GetBackupPlanFromJSON = Action('GetBackupPlanFromJSON')
GetBackupPlanFromTemplate = Action('GetBackupPlanFromTemplate')
GetBackupSelection = Action('GetBackupSelection')
GetBackupVaultAccessPolicy = Action('GetBackupVaultAccessPolicy')
GetBackupVaultNotifications = Action('GetBackupVaultNotifications')
GetRecoveryPointRestoreMetadata = \
    Action('GetRecoveryPointRestoreMetadata')
GetSupportedResourceTypes = Action('GetSupportedResourceTypes')
ListBackupJobs = Action('ListBackupJobs')
ListBackupPlanTemplates = Action('ListBackupPlanTemplates')
ListBackupPlanVersions = Action('ListBackupPlanVersions')
ListBackupPlans = Action('ListBackupPlans')
ListBackupSelections = Action('ListBackupSelections')
ListBackupVaults = Action('ListBackupVaults')
ListProtectedResources = Action('ListProtectedResources')
ListRecoveryPointsByBackupVault = \
    Action('ListRecoveryPointsByBackupVault')
ListRecoveryPointsByResource = Action('ListRecoveryPointsByResource')
ListRestoreJobs = Action('ListRestoreJobs')
ListTags = Action('ListTags')
PutBackupVaultAccessPolicy = Action('PutBackupVaultAccessPolicy')
PutBackupVaultNotifications = Action('PutBackupVaultNotifications')
StartBackupJob = Action('StartBackupJob')
StartRestoreJob = Action('StartRestoreJob')
StopBackupJob = Action('StopBackupJob')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateBackupPlan = Action('UpdateBackupPlan')
UpdateRecoveryPointLifecycle = Action('UpdateRecoveryPointLifecycle')
