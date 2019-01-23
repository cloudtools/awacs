# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Secrets Manager'
prefix = 'secretsmanager'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelRotateSecret = Action('CancelRotateSecret')
CreateSecret = Action('CreateSecret')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteSecret = Action('DeleteSecret')
DescribeSecret = Action('DescribeSecret')
GetRandomPassword = Action('GetRandomPassword')
GetResourcePolicy = Action('GetResourcePolicy')
GetSecretValue = Action('GetSecretValue')
ListSecretVersionIds = Action('ListSecretVersionIds')
ListSecrets = Action('ListSecrets')
PutResourcePolicy = Action('PutResourcePolicy')
PutSecretValue = Action('PutSecretValue')
RestoreSecret = Action('RestoreSecret')
RotateSecret = Action('RotateSecret')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateSecret = Action('UpdateSecret')
UpdateSecretVersionStage = Action('UpdateSecretVersionStage')
