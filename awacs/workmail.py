# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon WorkMail'
prefix = 'workmail'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddMembersToGroup = Action('AddMembersToGroup')
AssociateDelegateToResource = Action('AssociateDelegateToResource')
AssociateMemberToGroup = Action('AssociateMemberToGroup')
CreateAlias = Action('CreateAlias')
CreateGroup = Action('CreateGroup')
CreateMailDomain = Action('CreateMailDomain')
CreateMailUser = Action('CreateMailUser')
CreateOrganization = Action('CreateOrganization')
CreateResource = Action('CreateResource')
CreateUser = Action('CreateUser')
DeleteAlias = Action('DeleteAlias')
DeleteGroup = Action('DeleteGroup')
DeleteMailDomain = Action('DeleteMailDomain')
DeleteMailboxPermissions = Action('DeleteMailboxPermissions')
DeleteMobileDevice = Action('DeleteMobileDevice')
DeleteOrganization = Action('DeleteOrganization')
DeleteResource = Action('DeleteResource')
DeleteUser = Action('DeleteUser')
DeregisterFromWorkMail = Action('DeregisterFromWorkMail')
DescribeDirectories = Action('DescribeDirectories')
DescribeGroup = Action('DescribeGroup')
DescribeKmsKeys = Action('DescribeKmsKeys')
DescribeMailDomains = Action('DescribeMailDomains')
DescribeMailGroups = Action('DescribeMailGroups')
DescribeMailUsers = Action('DescribeMailUsers')
DescribeOrganization = Action('DescribeOrganization')
DescribeOrganizations = Action('DescribeOrganizations')
DescribeResource = Action('DescribeResource')
DescribeUser = Action('DescribeUser')
DisableMailGroups = Action('DisableMailGroups')
DisableMailUsers = Action('DisableMailUsers')
DisassociateDelegateFromResource = \
    Action('DisassociateDelegateFromResource')
DisassociateMemberFromGroup = Action('DisassociateMemberFromGroup')
EnableMailDomain = Action('EnableMailDomain')
EnableMailGroups = Action('EnableMailGroups')
EnableMailUsers = Action('EnableMailUsers')
GetMailDomainDetails = Action('GetMailDomainDetails')
GetMailGroupDetails = Action('GetMailGroupDetails')
GetMailUserDetails = Action('GetMailUserDetails')
GetMailboxDetails = Action('GetMailboxDetails')
GetMobileDeviceDetails = Action('GetMobileDeviceDetails')
GetMobileDevicesForUser = Action('GetMobileDevicesForUser')
GetMobilePolicyDetails = Action('GetMobilePolicyDetails')
ListAliases = Action('ListAliases')
ListGroupMembers = Action('ListGroupMembers')
ListGroups = Action('ListGroups')
ListMailboxPermissions = Action('ListMailboxPermissions')
ListMembersInMailGroup = Action('ListMembersInMailGroup')
ListOrganizations = Action('ListOrganizations')
ListResourceDelegates = Action('ListResourceDelegates')
ListResources = Action('ListResources')
ListUsers = Action('ListUsers')
PutMailboxPermissions = Action('PutMailboxPermissions')
RegisterToWorkMail = Action('RegisterToWorkMail')
RemoveMembersFromGroup = Action('RemoveMembersFromGroup')
ResetPassword = Action('ResetPassword')
ResetUserPassword = Action('ResetUserPassword')
SearchMembers = Action('SearchMembers')
SetAdmin = Action('SetAdmin')
SetDefaultMailDomain = Action('SetDefaultMailDomain')
SetMailGroupDetails = Action('SetMailGroupDetails')
SetMailUserDetails = Action('SetMailUserDetails')
SetMobilePolicyDetails = Action('SetMobilePolicyDetails')
UpdateMailboxQuota = Action('UpdateMailboxQuota')
UpdatePrimaryEmailAddress = Action('UpdatePrimaryEmailAddress')
UpdateResource = Action('UpdateResource')
WipeMobileDevice = Action('WipeMobileDevice')
