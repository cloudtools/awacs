# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon WorkDocs'
prefix = 'workdocs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AbortDocumentVersionUpload = Action('AbortDocumentVersionUpload')
ActivateUser = Action('ActivateUser')
AddResourcePermissions = Action('AddResourcePermissions')
AddUserToGroup = Action('AddUserToGroup')
CheckAlias = Action('CheckAlias')
CreateFolder = Action('CreateFolder')
CreateInstance = Action('CreateInstance')
CreateNotificationSubscription = Action('CreateNotificationSubscription')
CreateUser = Action('CreateUser')
DeactivateUser = Action('DeactivateUser')
DeleteDocument = Action('DeleteDocument')
DeleteFolder = Action('DeleteFolder')
DeleteFolderContents = Action('DeleteFolderContents')
DeleteInstance = Action('DeleteInstance')
DeleteNotificationSubscription = Action('DeleteNotificationSubscription')
DeleteUser = Action('DeleteUser')
DeregisterDirectory = Action('DeregisterDirectory')
DescribeAvailableDirectories = Action('DescribeAvailableDirectories')
DescribeDocumentVersions = Action('DescribeDocumentVersions')
DescribeFolderContents = Action('DescribeFolderContents')
DescribeInstances = Action('DescribeInstances')
DescribeNotificationSubscriptions = \
    Action('DescribeNotificationSubscriptions')
DescribeResourcePermissions = Action('DescribeResourcePermissions')
DescribeUsers = Action('DescribeUsers')
GetDocument = Action('GetDocument')
GetDocumentPath = Action('GetDocumentPath')
GetDocumentVersion = Action('GetDocumentVersion')
GetFolder = Action('GetFolder')
GetFolderPath = Action('GetFolderPath')
InitiateDocumentVersionUpload = Action('InitiateDocumentVersionUpload')
RegisterDirectory = Action('RegisterDirectory')
RemoveAllResourcePermissions = Action('RemoveAllResourcePermissions')
RemoveResourcePermission = Action('RemoveResourcePermission')
RemoveUserFromGroup = Action('RemoveUserFromGroup')
UpdateDocument = Action('UpdateDocument')
UpdateDocumentVersion = Action('UpdateDocumentVersion')
UpdateFolder = Action('UpdateFolder')
UpdateInstanceAlias = Action('UpdateInstanceAlias')
UpdateUser = Action('UpdateUser')
