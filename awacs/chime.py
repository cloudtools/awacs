# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Chime'
prefix = 'chime'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptDelegate = Action('AcceptDelegate')
ActivateUsers = Action('ActivateUsers')
AddDomain = Action('AddDomain')
AddOrUpdateGroups = Action('AddOrUpdateGroups')
AuthorizeDirectory = Action('AuthorizeDirectory')
BatchSuspendUser = Action('BatchSuspendUser')
BatchUnsuspendUser = Action('BatchUnsuspendUser')
BatchUpdateUser = Action('BatchUpdateUser')
ConnectDirectory = Action('ConnectDirectory')
CreateAccount = Action('CreateAccount')
CreateApiKey = Action('CreateApiKey')
CreateCDRBucket = Action('CreateCDRBucket')
DeleteAccount = Action('DeleteAccount')
DeleteAccountOpenIdConfig = Action('DeleteAccountOpenIdConfig')
DeleteApiKey = Action('DeleteApiKey')
DeleteCDRBucket = Action('DeleteCDRBucket')
DeleteDelegate = Action('DeleteDelegate')
DeleteDomain = Action('DeleteDomain')
DeleteGroups = Action('DeleteGroups')
DisconnectDirectory = Action('DisconnectDirectory')
GetAccount = Action('GetAccount')
GetAccountResource = Action('GetAccountResource')
GetAccountSettings = Action('GetAccountSettings')
GetAccountWithOpenIdConfig = Action('GetAccountWithOpenIdConfig')
GetCDRBucket = Action('GetCDRBucket')
GetDomain = Action('GetDomain')
GetMeetingDetail = Action('GetMeetingDetail')
GetUser = Action('GetUser')
GetUserActivityReportData = Action('GetUserActivityReportData')
GetUserByEmail = Action('GetUserByEmail')
InviteDelegate = Action('InviteDelegate')
InviteUsers = Action('InviteUsers')
ListAccountUsageReportData = Action('ListAccountUsageReportData')
ListAccounts = Action('ListAccounts')
ListApiKeys = Action('ListApiKeys')
ListCDRBucket = Action('ListCDRBucket')
ListDelegates = Action('ListDelegates')
ListDirectories = Action('ListDirectories')
ListDomains = Action('ListDomains')
ListGroups = Action('ListGroups')
ListMeetingEvents = Action('ListMeetingEvents')
ListMeetingsReportData = Action('ListMeetingsReportData')
ListUsers = Action('ListUsers')
LogoutUser = Action('LogoutUser')
RenameAccount = Action('RenameAccount')
RenewDelegate = Action('RenewDelegate')
ResetAccountResource = Action('ResetAccountResource')
ResetPersonalPin = Action('ResetPersonalPin')
RetrieveDataExports = Action('RetrieveDataExports')
StartDataExport = Action('StartDataExport')
SubmitSupportRequest = Action('SubmitSupportRequest')
SuspendUsers = Action('SuspendUsers')
UnauthorizeDirectory = Action('UnauthorizeDirectory')
UpdateAccount = Action('UpdateAccount')
UpdateAccountOpenIdConfig = Action('UpdateAccountOpenIdConfig')
UpdateAccountResource = Action('UpdateAccountResource')
UpdateAccountSettings = Action('UpdateAccountSettings')
UpdateCDRBucket = Action('UpdateCDRBucket')
UpdateCDRSettings = Action('UpdateCDRSettings')
UpdateSupportedLicenses = Action('UpdateSupportedLicenses')
UpdateUser = Action('UpdateUser')
UpdateUserLicenses = Action('UpdateUserLicenses')
ValidateAccountResource = Action('ValidateAccountResource')
ValidateDelegate = Action('ValidateDelegate')
