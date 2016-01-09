from aws import Action, BaseARN

service_name = 'Amazon Key Management Service'
prefix = 'kms'


class ARN(BaseARN):
    def __init__(self, resource, region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)

CancelKeyDeletion = Action(prefix, 'CancelKeyDeletion')
CreateAlias = Action(prefix, 'CreateAlias')
CreateGrant = Action(prefix, 'CreateGrant')
CreateKey = Action(prefix, 'CreateKey')
Decrypt = Action(prefix, 'Decrypt')
DeleteAlias = Action(prefix, 'DeleteAlias')
DescribeKey = Action(prefix, 'DescribeKey')
DisableKey = Action(prefix, 'DisableKey')
DisableKeyRotation = Action(prefix, 'DisableKeyRotation')
EnableKey = Action(prefix, 'EnableKey')
EnableKeyRotation = Action(prefix, 'EnableKeyRotation')
Encrypt = Action(prefix, 'Encrypt')
GenerateDataKey = Action(prefix, 'GenerateDataKey')
GenerateDataKeyWithoutPlaintext = \
    Action(prefix, 'GenerateDataKeyWithoutPlaintext')
GenerateRandom = Action(prefix, 'GenerateRandom')
GetKeyPolicy = Action(prefix, 'GetKeyPolicy')
GetKeyRotationStatus = Action(prefix, 'GetKeyRotationStatus')
ListAliases = Action(prefix, 'ListAliases')
ListGrants = Action(prefix, 'ListGrants')
ListKeyPolicies = Action(prefix, 'ListKeyPolicies')
ListKeys = Action(prefix, 'ListKeys')
ListRetirableGrants = Action(prefix, 'ListRetirableGrants')
PutKeyPolicy = Action(prefix, 'PutKeyPolicy')
ReEncrypt = Action(prefix, 'ReEncrypt')
RetireGrant = Action(prefix, 'RetireGrant')
RevokeGrant = Action(prefix, 'RevokeGrant')
ScheduleKeyDeletion = Action(prefix, 'ScheduleKeyDeletion')
UpdateAlias = Action(prefix, 'UpdateAlias')
UpdateKeyDescription = Action(prefix, 'UpdateKeyDescription')
