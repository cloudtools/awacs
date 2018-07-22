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
CreateResource = Action('CreateResource')
DeleteMailDomain = Action('DeleteMailDomain')
DeleteMobileDevice = Action('DeleteMobileDevice')
DeleteOrganization = Action('DeleteOrganization')
DescribeDirectories = Action('DescribeDirectories')
DescribeKmsKeys = Action('DescribeKmsKeys')
DescribeMailDomains = Action('DescribeMailDomains')
DescribeMailGroups = Action('DescribeMailGroups')
DescribeMailUsers = Action('DescribeMailUsers')
DescribeOrganizations = Action('DescribeOrganizations')
DisableMailGroups = Action('DisableMailGroups')
DisableMailUsers = Action('DisableMailUsers')
EnableMailDomain = Action('EnableMailDomain')
EnableMailGroups = Action('EnableMailGroups')
EnableMailUsers = Action('EnableMailUsers')
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
