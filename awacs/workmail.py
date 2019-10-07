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
CreateInboundMailFlowRule = Action('CreateInboundMailFlowRule')
CreateMailDomain = Action('CreateMailDomain')
CreateMailUser = Action('CreateMailUser')
CreateOrganization = Action('CreateOrganization')
CreateOutboundMailFlowRule = Action('CreateOutboundMailFlowRule')
CreateResource = Action('CreateResource')
CreateSmtpGateway = Action('CreateSmtpGateway')
CreateUser = Action('CreateUser')
DeleteAlias = Action('DeleteAlias')
DeleteGroup = Action('DeleteGroup')
DeleteInboundMailFlowRule = Action('DeleteInboundMailFlowRule')
DeleteMailDomain = Action('DeleteMailDomain')
DeleteMailboxPermissions = Action('DeleteMailboxPermissions')
DeleteMobileDevice = Action('DeleteMobileDevice')
DeleteOrganization = Action('DeleteOrganization')
DeleteOutboundMailFlowRule = Action('DeleteOutboundMailFlowRule')
DeleteResource = Action('DeleteResource')
DeleteSmtpGateway = Action('DeleteSmtpGateway')
DeleteUser = Action('DeleteUser')
DeregisterFromWorkMail = Action('DeregisterFromWorkMail')
DescribeDirectories = Action('DescribeDirectories')
DescribeGroup = Action('DescribeGroup')
DescribeInboundMailFlowRule = Action('DescribeInboundMailFlowRule')
DescribeKmsKeys = Action('DescribeKmsKeys')
DescribeMailDomains = Action('DescribeMailDomains')
DescribeMailGroups = Action('DescribeMailGroups')
DescribeMailUsers = Action('DescribeMailUsers')
DescribeOrganization = Action('DescribeOrganization')
DescribeOrganizations = Action('DescribeOrganizations')
DescribeOutboundMailFlowRule = Action('DescribeOutboundMailFlowRule')
DescribeResource = Action('DescribeResource')
DescribeSmtpGateway = Action('DescribeSmtpGateway')
DescribeUser = Action('DescribeUser')
DisableMailGroups = Action('DisableMailGroups')
DisableMailUsers = Action('DisableMailUsers')
DisassociateDelegateFromResource = \
    Action('DisassociateDelegateFromResource')
DisassociateMemberFromGroup = Action('DisassociateMemberFromGroup')
EnableMailDomain = Action('EnableMailDomain')
EnableMailGroups = Action('EnableMailGroups')
EnableMailUsers = Action('EnableMailUsers')
GetJournalingRules = Action('GetJournalingRules')
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
ListInboundMailFlowRules = Action('ListInboundMailFlowRules')
ListMailboxPermissions = Action('ListMailboxPermissions')
ListMembersInMailGroup = Action('ListMembersInMailGroup')
ListOrganizations = Action('ListOrganizations')
ListOutboundMailFlowRules = Action('ListOutboundMailFlowRules')
ListResourceDelegates = Action('ListResourceDelegates')
ListResources = Action('ListResources')
ListSmtpGateways = Action('ListSmtpGateways')
ListUsers = Action('ListUsers')
PutMailboxPermissions = Action('PutMailboxPermissions')
RegisterToWorkMail = Action('RegisterToWorkMail')
RemoveMembersFromGroup = Action('RemoveMembersFromGroup')
ResetPassword = Action('ResetPassword')
ResetUserPassword = Action('ResetUserPassword')
SearchMembers = Action('SearchMembers')
SetAdmin = Action('SetAdmin')
SetDefaultMailDomain = Action('SetDefaultMailDomain')
SetJournalingRules = Action('SetJournalingRules')
SetMailGroupDetails = Action('SetMailGroupDetails')
SetMailUserDetails = Action('SetMailUserDetails')
SetMobilePolicyDetails = Action('SetMobilePolicyDetails')
TestInboundMailFlowRules = Action('TestInboundMailFlowRules')
TestOutboundMailFlowRules = Action('TestOutboundMailFlowRules')
UpdateInboundMailFlowRule = Action('UpdateInboundMailFlowRule')
UpdateMailboxQuota = Action('UpdateMailboxQuota')
UpdateOutboundMailFlowRule = Action('UpdateOutboundMailFlowRule')
UpdatePrimaryEmailAddress = Action('UpdatePrimaryEmailAddress')
UpdateResource = Action('UpdateResource')
UpdateSmtpGateway = Action('UpdateSmtpGateway')
WipeMobileDevice = Action('WipeMobileDevice')
