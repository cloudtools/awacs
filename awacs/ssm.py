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
DescribeAutomationActions = Action('DescribeAutomationActions')
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
DescribeInstancePatches = Action('DescribeInstancePatches')
DescribeInstancePatchStates = Action('DescribeInstancePatchStates')
DescribeInstancePatchStatesForPatchGroup = \
    Action('DescribeInstancePatchStatesForPatchGroup')
DescribeMaintenanceWindowExecutions = \
    Action('DescribeMaintenanceWindowExecutions')
DescribeMaintenanceWindowExecutionTaskInvocations = \
    Action('DescribeMaintenanceWindowExecutionTaskInvocations')
DescribeMaintenanceWindowExecutionTasks = \
    Action('DescribeMaintenanceWindowExecutionTasks')
DescribeMaintenanceWindows = Action('DescribeMaintenanceWindows')
DescribeMaintenanceWindowTargets = \
    Action('DescribeMaintenanceWindowTargets')
DescribeMaintenanceWindowTasks = Action('DescribeMaintenanceWindowTasks')
DescribeParameters = Action('DescribeParameters')
DescribePatchBaselines = Action('DescribePatchBaselines')
DescribePatchGroups = Action('DescribePatchGroups')
DescribePatchGroupState = Action('DescribePatchGroupState')
GetCommandInvocation = Action('GetCommandInvocation')
GetDefaultPatchBaseline = Action('GetDefaultPatchBaseline')
GetDeployablePatchSnapshotForInstance = \
    Action('GetDeployablePatchSnapshotForInstance')
GetInventory = Action('GetInventory')
GetInventorySchema = Action('GetInventorySchema')
GetDocument = Action('GetDocument')
GetMaintenanceWindow = Action('GetMaintenanceWindow')
GetMaintenanceWindowExecution = Action('GetMaintenanceWindowExecution')
GetMaintenanceWindowExecutionTask = \
    Action('GetMaintenanceWindowExecutionTask')
GetParameterHistory = Action('GetParameterHistory')
GetParameters = Action('GetParameters')
GetPatchBaseline = Action('GetPatchBaseline')
GetPatchBaselineForPatchGroup = Action('GetPatchBaselineForPatchGroup')
ListAssociations = Action('ListAssociations')
ListCommandInvocations = Action('ListCommandInvocations')
ListCommands = Action('ListCommands')
ListDocuments = Action('ListDocuments')
ListDocumentVersions = Action('ListDocumentVersions')
ListInstanceAssociations = Action('ListInstanceAssociations')
ListInventoryEntries = Action('ListInventoryEntries')
ListTagsForResource = Action('ListTagsForResource')
ModifyDocumentPermission = Action('ModifyDocumentPermission')
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
UpdateAssociation = Action('UpdateAssociation')
UpdateAssociationStatus = Action('UpdateAssociationStatus')
UpdateDocument = Action('UpdateDocument')
UpdateDocumentDefaultVersion = Action('UpdateDocumentDefaultVersion')
UpdateInstanceAssociationStatus = \
    Action('UpdateInstanceAssociationStatus')
UpdateMaintenanceWindow = Action('UpdateMaintenanceWindow')
UpdateManagedInstanceRole = Action('UpdateManagedInstanceRole')
UpdatePatchBaseline = Action('UpdatePatchBaseline')
