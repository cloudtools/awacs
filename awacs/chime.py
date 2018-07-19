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
ConnectDirectory = Action('ConnectDirectory')
CreateAccount = Action('CreateAccount')
CreateCDRBucket = Action('CreateCDRBucket')
DeleteAccount = Action('DeleteAccount')
DeleteCDRBucket = Action('DeleteCDRBucket')
DeleteDelegate = Action('DeleteDelegate')
DeleteDomain = Action('DeleteDomain')
DeleteGroups = Action('DeleteGroups')
DisconnectDirectory = Action('DisconnectDirectory')
GetAccount = Action('GetAccount')
GetAccountResource = Action('GetAccountResource')
GetAccountSettings = Action('GetAccountSettings')
GetCDRBucket = Action('GetCDRBucket')
GetDomain = Action('GetDomain')
GetUser = Action('GetUser')
GetUserByEmail = Action('GetUserByEmail')
InviteDelegate = Action('InviteDelegate')
InviteUsers = Action('InviteUsers')
ListAccounts = Action('ListAccounts')
ListCDRBucket = Action('ListCDRBucket')
ListDelegates = Action('ListDelegates')
ListDirectories = Action('ListDirectories')
ListDomains = Action('ListDomains')
ListGroups = Action('ListGroups')
ListUsers = Action('ListUsers')
LogoutUser = Action('LogoutUser')
RenameAccount = Action('RenameAccount')
RenewDelegate = Action('RenewDelegate')
ResetAccountResource = Action('ResetAccountResource')
ResetPersonalPin = Action('ResetPersonalPin')
SubmitSupportRequest = Action('SubmitSupportRequest')
SuspendUsers = Action('SuspendUsers')
UnauthorizeDirectory = Action('UnauthorizeDirectory')
UpdateAccountResource = Action('UpdateAccountResource')
UpdateAccountSettings = Action('UpdateAccountSettings')
UpdateCDRBucket = Action('UpdateCDRBucket')
UpdateSupportedLicenses = Action('UpdateSupportedLicenses')
UpdateUserLicenses = Action('UpdateUserLicenses')
ValidateAccountResource = Action('ValidateAccountResource')
ValidateDelegate = Action('ValidateDelegate')
