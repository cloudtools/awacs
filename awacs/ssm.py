# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Simple Systems Manager'
prefix = 'ssm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToResource = Action('AddTagsToResource')
CancelCommand = Action('CancelCommand')
CreateActivation = Action('CreateActivation')
CreateAssociation = Action('CreateAssociation')
CreateAssociationBatch = Action('CreateAssociationBatch')
CreateDocument = Action('CreateDocument')
CreateMaintenanceWindow = Action('CreateMaintenanceWindow')
CreatePatchBaseline = Action('CreatePatchBaseline')
DeleteActivation = Action('DeleteActivation')
DeleteAssociation = Action('DeleteAssociation')
DeleteDocument = Action('DeleteDocument')
DeleteMaintenanceWindow = Action('DeleteMaintenanceWindow')
DeleteParameter = Action('DeleteParameter')
DeletePatchBaseline = Action('DeletePatchBaseline')
DeregisterManagedInstance = Action('DeregisterManagedInstance')
DeregisterPatchBaselineForPatchGroup = \
    Action('DeregisterPatchBaselineForPatchGroup')
DeregisterTargetFromMaintenanceWindow = \
    Action('DeregisterTargetFromMaintenanceWindow')
DeregisterTaskFromMaintenanceWindow = \
    Action('DeregisterTaskFromMaintenanceWindow')
DescribeActivations = Action('DescribeActivations')
DescribeAssociation = Action('DescribeAssociation')
DescribeAutomationExecutions = Action('DescribeAutomationExecutions')
DescribeAvailablePatches = Action('DescribeAvailablePatches')
DescribeDocument = Action('DescribeDocument')
DescribeDocumentPermission = Action('DescribeDocumentPermission')
DescribeEffectiveInstanceAssociations = \
    Action('DescribeEffectiveInstanceAssociations')
DescribeEffectivePatchesForPatchBaseline = \
    Action('DescribeEffectivePatchesForPatchBaseline')
DescribeInstanceAssociationsStatus = \
    Action('DescribeInstanceAssociationsStatus')
DescribeInstanceInformation = Action('DescribeInstanceInformation')
DescribeInstancePatchStates = Action('DescribeInstancePatchStates')
DescribeInstancePatchStatesForPatchGroup = \
    Action('DescribeInstancePatchStatesForPatchGroup')
DescribeInstancePatches = Action('DescribeInstancePatches')
DescribeMaintenanceWindowExecutionTaskInvocations = \
    Action('DescribeMaintenanceWindowExecutionTaskInvocations')
DescribeMaintenanceWindowExecutionTasks = \
    Action('DescribeMaintenanceWindowExecutionTasks')
DescribeMaintenanceWindowExecutions = \
    Action('DescribeMaintenanceWindowExecutions')
DescribeMaintenanceWindowTargets = \
    Action('DescribeMaintenanceWindowTargets')
DescribeMaintenanceWindowTasks = Action('DescribeMaintenanceWindowTasks')
DescribeMaintenanceWindows = Action('DescribeMaintenanceWindows')
DescribeParameters = Action('DescribeParameters')
DescribePatchBaselines = Action('DescribePatchBaselines')
DescribePatchGroupState = Action('DescribePatchGroupState')
DescribePatchGroups = Action('DescribePatchGroups')
GetAutomationExecution = Action('GetAutomationExecution')
GetCommandInvocation = Action('GetCommandInvocation')
GetDefaultPatchBaseline = Action('GetDefaultPatchBaseline')
GetDeployablePatchSnapshotForInstance = \
    Action('GetDeployablePatchSnapshotForInstance')
GetDocument = Action('GetDocument')
GetInventory = Action('GetInventory')
GetInventorySchema = Action('GetInventorySchema')
GetMaintenanceWindow = Action('GetMaintenanceWindow')
GetMaintenanceWindowExecution = Action('GetMaintenanceWindowExecution')
GetMaintenanceWindowExecutionTask = \
    Action('GetMaintenanceWindowExecutionTask')
GetManifest = Action('GetManifest')
GetParameter = Action('GetParameter')
GetParameterHistory = Action('GetParameterHistory')
GetParameters = Action('GetParameters')
GetParametersByPath = Action('GetParametersByPath')
GetPatchBaseline = Action('GetPatchBaseline')
GetPatchBaselineForPatchGroup = Action('GetPatchBaselineForPatchGroup')
ListAssociationVersions = Action('ListAssociationVersions')
ListAssociations = Action('ListAssociations')
ListCommandInvocations = Action('ListCommandInvocations')
ListCommands = Action('ListCommands')
ListDocumentVersions = Action('ListDocumentVersions')
ListDocuments = Action('ListDocuments')
ListInstanceAssociations = Action('ListInstanceAssociations')
ListInventoryEntries = Action('ListInventoryEntries')
ListTagsForResource = Action('ListTagsForResource')
ModifyDocumentPermission = Action('ModifyDocumentPermission')
PutComplianceItems = Action('PutComplianceItems')
PutInventory = Action('PutInventory')
PutParameter = Action('PutParameter')
RegisterDefaultPatchBaseline = Action('RegisterDefaultPatchBaseline')
RegisterPatchBaselineForPatchGroup = \
    Action('RegisterPatchBaselineForPatchGroup')
RegisterTargetWithMaintenanceWindow = \
    Action('RegisterTargetWithMaintenanceWindow')
RegisterTaskWithMaintenanceWindow = \
    Action('RegisterTaskWithMaintenanceWindow')
RemoveTagsFromResource = Action('RemoveTagsFromResource')
SendCommand = Action('SendCommand')
StartAssociationsOnce = Action('StartAssociationsOnce')
StartAutomationExecution = Action('StartAutomationExecution')
StopAutomationExecution = Action('StopAutomationExecution')
UpdateAssociation = Action('UpdateAssociation')
UpdateAssociationStatus = Action('UpdateAssociationStatus')
UpdateDocument = Action('UpdateDocument')
UpdateDocumentDefaultVersion = Action('UpdateDocumentDefaultVersion')
UpdateInstanceAssociationStatus = \
    Action('UpdateInstanceAssociationStatus')
UpdateMaintenanceWindow = Action('UpdateMaintenanceWindow')
UpdateMaintenanceWindowTarget = Action('UpdateMaintenanceWindowTarget')
UpdateMaintenanceWindowTask = Action('UpdateMaintenanceWindowTask')
UpdateManagedInstanceRole = Action('UpdateManagedInstanceRole')
UpdatePatchBaseline = Action('UpdatePatchBaseline')
