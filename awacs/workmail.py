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
CreateGroup = Action('CreateGroup')
CreateMailDomain = Action('CreateMailDomain')
CreateMailUser = Action('CreateMailUser')
CreateOrganization = Action('CreateOrganization')
DeleteOrganization = Action('DeleteOrganization')
DeleteMailDomain = Action('DeleteMailDomain')
DeleteMobileDevice = Action('DeleteMobileDevice')
DescribeDirectories = Action('DescribeDirectories')
DescribeKmsKeys = Action('DescribeKmsKeys')
DescribeOrganizations = Action('DescribeOrganizations')
DescribeMailDomains = Action('DescribeMailDomains')
DescribeMailGroups = Action('DescribeMailGroups')
DescribeMailUsers = Action('DescribeMailUsers')
DisableMailGroups = Action('DisableMailGroups')
DisableMailUsers = Action('DisableMailUsers')
EnableMailDomain = Action('EnableMailDomain')
EnableMailUsers = Action('EnableMailUsers')
EnableMailGroups = Action('EnableMailGroups')
GetMailDomainDetails = Action('GetMailDomainDetails')
GetMailGroupDetails = Action('GetMailGroupDetails')
GetMailUserDetails = Action('GetMailUserDetails')
GetMobileDeviceDetails = Action('GetMobileDeviceDetails')
GetMobileDevicesForUser = Action('GetMobileDevicesForUser')
GetMobilePolicyDetails = Action('GetMobilePolicyDetails')
ListMembersInMailGroup = Action('ListMembersInMailGroup')
RemoveMembersFromGroup = Action('RemoveMembersFromGroup')
ResetUserPassword = Action('ResetUserPassword')
SearchMembers = Action('SearchMembers')
SetAdmin = Action('SetAdmin')
SetDefaultMailDomain = Action('SetDefaultMailDomain')
SetMailGroupDetails = Action('SetMailGroupDetails')
SetMailUserDetails = Action('SetMailUserDetails')
SetMobilePolicyDetails = Action('SetMobilePolicyDetails')
WipeMobileDevice = Action('WipeMobileDevice')
