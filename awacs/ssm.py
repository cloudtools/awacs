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
DeleteActivation = Action('DeleteActivation')
DeleteAssociation = Action('DeleteAssociation')
DeleteDocument = Action('DeleteDocument')
DeleteMaintenanceWindow = Action('DeleteMaintenanceWindow')
DeleteParameter = Action('DeleteParameter')
DeregisterManagedInstance = Action('DeregisterManagedInstance')
DeregisterTargetFromMaintenanceWindow = \
    Action('DeregisterTargetFromMaintenanceWindow')
DeregisterTaskFromMaintenanceWindow = \
    Action('DeregisterTaskFromMaintenanceWindow')
DescribeActivations = Action('DescribeActivations')
DescribeAssociation = Action('DescribeAssociation')
DescribeAutomationActions = Action('DescribeAutomationActions')
DescribeAutomationExecutions = Action('DescribeAutomationExecutions')
DescribeDocument = Action('DescribeDocument')
DescribeDocumentPermission = Action('DescribeDocumentPermission')
DescribeEffectiveInstanceAssociations = \
    Action('DescribeEffectiveInstanceAssociations')
DescribeInstanceAssociationsStatus = \
    Action('DescribeInstanceAssociationsStatus')
DescribeInstanceInformation = Action('DescribeInstanceInformation')
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
GetCommandInvocation = Action('GetCommandInvocation')
GetInventory = Action('GetInventory')
GetInventorySchema = Action('GetInventorySchema')
GetDocument = Action('GetDocument')
GetMaintenanceWindow = Action('GetMaintenanceWindow')
GetMaintenanceWindowExecution = Action('GetMaintenanceWindowExecution')
GetMaintenanceWindowExecutionTask = \
    Action('GetMaintenanceWindowExecutionTask')
GetParameterHistory = Action('GetParameterHistory')
GetParameters = Action('GetParameters')
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
