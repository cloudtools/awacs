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
AssociatePhoneNumberWithUser = Action('AssociatePhoneNumberWithUser')
AssociatePhoneNumbersWithVoiceConnector = \
    Action('AssociatePhoneNumbersWithVoiceConnector')
AuthorizeDirectory = Action('AuthorizeDirectory')
BatchDeletePhoneNumber = Action('BatchDeletePhoneNumber')
BatchSuspendUser = Action('BatchSuspendUser')
BatchUnsuspendUser = Action('BatchUnsuspendUser')
BatchUpdatePhoneNumber = Action('BatchUpdatePhoneNumber')
BatchUpdateUser = Action('BatchUpdateUser')
ConnectDirectory = Action('ConnectDirectory')
CreateAccount = Action('CreateAccount')
CreateApiKey = Action('CreateApiKey')
CreateCDRBucket = Action('CreateCDRBucket')
CreatePhoneNumberOrder = Action('CreatePhoneNumberOrder')
CreateVoiceConnector = Action('CreateVoiceConnector')
DeleteAccount = Action('DeleteAccount')
DeleteAccountOpenIdConfig = Action('DeleteAccountOpenIdConfig')
DeleteApiKey = Action('DeleteApiKey')
DeleteCDRBucket = Action('DeleteCDRBucket')
DeleteDelegate = Action('DeleteDelegate')
DeleteDomain = Action('DeleteDomain')
DeleteGroups = Action('DeleteGroups')
DeletePhoneNumber = Action('DeletePhoneNumber')
DeleteVoiceConnector = Action('DeleteVoiceConnector')
DeleteVoiceConnectorOrigination = \
    Action('DeleteVoiceConnectorOrigination')
DeleteVoiceConnectorTermination = \
    Action('DeleteVoiceConnectorTermination')
DeleteVoiceConnectorTerminationCredentials = \
    Action('DeleteVoiceConnectorTerminationCredentials')
DisassociatePhoneNumberFromUser = \
    Action('DisassociatePhoneNumberFromUser')
DisassociatePhoneNumbersFromVoiceConnector = \
    Action('DisassociatePhoneNumbersFromVoiceConnector')
DisconnectDirectory = Action('DisconnectDirectory')
GetAccount = Action('GetAccount')
GetAccountResource = Action('GetAccountResource')
GetAccountSettings = Action('GetAccountSettings')
GetAccountWithOpenIdConfig = Action('GetAccountWithOpenIdConfig')
GetCDRBucket = Action('GetCDRBucket')
GetDomain = Action('GetDomain')
GetGlobalSettings = Action('GetGlobalSettings')
GetMeetingDetail = Action('GetMeetingDetail')
GetPhoneNumber = Action('GetPhoneNumber')
GetPhoneNumberOrder = Action('GetPhoneNumberOrder')
GetTelephonyLimits = Action('GetTelephonyLimits')
GetUser = Action('GetUser')
GetUserActivityReportData = Action('GetUserActivityReportData')
GetUserByEmail = Action('GetUserByEmail')
GetUserSettings = Action('GetUserSettings')
GetVoiceConnector = Action('GetVoiceConnector')
GetVoiceConnectorOrigination = Action('GetVoiceConnectorOrigination')
GetVoiceConnectorTermination = Action('GetVoiceConnectorTermination')
GetVoiceConnectorTerminationHealth = \
    Action('GetVoiceConnectorTerminationHealth')
InviteDelegate = Action('InviteDelegate')
InviteUsers = Action('InviteUsers')
ListAccountUsageReportData = Action('ListAccountUsageReportData')
ListAccounts = Action('ListAccounts')
ListApiKeys = Action('ListApiKeys')
ListCDRBucket = Action('ListCDRBucket')
ListCallingRegions = Action('ListCallingRegions')
ListDelegates = Action('ListDelegates')
ListDirectories = Action('ListDirectories')
ListDomains = Action('ListDomains')
ListGroups = Action('ListGroups')
ListMeetingEvents = Action('ListMeetingEvents')
ListMeetingsReportData = Action('ListMeetingsReportData')
ListPhoneNumberOrders = Action('ListPhoneNumberOrders')
ListPhoneNumbers = Action('ListPhoneNumbers')
ListUsers = Action('ListUsers')
ListVoiceConnectorTerminationCredentials = \
    Action('ListVoiceConnectorTerminationCredentials')
ListVoiceConnectors = Action('ListVoiceConnectors')
LogoutUser = Action('LogoutUser')
PutVoiceConnectorOrigination = Action('PutVoiceConnectorOrigination')
PutVoiceConnectorTermination = Action('PutVoiceConnectorTermination')
PutVoiceConnectorTerminationCredentials = \
    Action('PutVoiceConnectorTerminationCredentials')
RenameAccount = Action('RenameAccount')
RenewDelegate = Action('RenewDelegate')
ResetAccountResource = Action('ResetAccountResource')
ResetPersonalPIN = Action('ResetPersonalPIN')
ResetPersonalPin = Action('ResetPersonalPin')
RestorePhoneNumber = Action('RestorePhoneNumber')
RetrieveDataExports = Action('RetrieveDataExports')
SearchAvailablePhoneNumbers = Action('SearchAvailablePhoneNumbers')
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
UpdateGlobalSettings = Action('UpdateGlobalSettings')
UpdatePhoneNumber = Action('UpdatePhoneNumber')
UpdateSupportedLicenses = Action('UpdateSupportedLicenses')
UpdateUser = Action('UpdateUser')
UpdateUserLicenses = Action('UpdateUserLicenses')
UpdateUserSettings = Action('UpdateUserSettings')
UpdateVoiceConnector = Action('UpdateVoiceConnector')
ValidateAccountResource = Action('ValidateAccountResource')
ValidateDelegate = Action('ValidateDelegate')
