# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Key Management Service'
prefix = 'kms'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelKeyDeletion = Action('CancelKeyDeletion')
CreateAlias = Action('CreateAlias')
CreateGrant = Action('CreateGrant')
CreateKey = Action('CreateKey')
Decrypt = Action('Decrypt')
DeleteAlias = Action('DeleteAlias')
DeleteImportedKeyMaterial = Action('DeleteImportedKeyMaterial')
DescribeKey = Action('DescribeKey')
DisableKey = Action('DisableKey')
DisableKeyRotation = Action('DisableKeyRotation')
EnableKey = Action('EnableKey')
EnableKeyRotation = Action('EnableKeyRotation')
Encrypt = Action('Encrypt')
GenerateDataKey = Action('GenerateDataKey')
GenerateDataKeyWithoutPlaintext = \
    Action('GenerateDataKeyWithoutPlaintext')
GenerateRandom = Action('GenerateRandom')
GetKeyPolicy = Action('GetKeyPolicy')
GetKeyRotationStatus = Action('GetKeyRotationStatus')
GetParametersForImport = Action('GetParametersForImport')
ImportKeyMaterial = Action('ImportKeyMaterial')
ListAliases = Action('ListAliases')
ListGrants = Action('ListGrants')
ListKeyPolicies = Action('ListKeyPolicies')
ListKeys = Action('ListKeys')
ListRetirableGrants = Action('ListRetirableGrants')
PutKeyPolicy = Action('PutKeyPolicy')
ReEncryptFrom = Action('ReEncryptFrom')
ReEncryptTo = Action('ReEncryptTo')
ReEncrypt = Action('ReEncrypt')
RevokeGrant = Action('RevokeGrant')
ScheduleKeyDeletion = Action('ScheduleKeyDeletion')
UpdateAlias = Action('UpdateAlias')
UpdateKeyDescription = Action('UpdateKeyDescription')
