# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Cloud9'
prefix = 'cloud9'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateEnvironmentEC2 = Action('CreateEnvironmentEC2')
CreateEnvironmentMembership = Action('CreateEnvironmentMembership')
CreateEnvironmentSSH = Action('CreateEnvironmentSSH')
DeleteEnvironment = Action('DeleteEnvironment')
DeleteEnvironmentMembership = Action('DeleteEnvironmentMembership')
DescribeEnvironmentMemberships = Action('DescribeEnvironmentMemberships')
DescribeEnvironmentStatus = Action('DescribeEnvironmentStatus')
DescribeEnvironments = Action('DescribeEnvironments')
GetUserPublicKey = Action('GetUserPublicKey')
GetUserSettings = Action('GetUserSettings')
ListEnvironments = Action('ListEnvironments')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateEnvironment = Action('UpdateEnvironment')
UpdateEnvironmentMembership = Action('UpdateEnvironmentMembership')
UpdateUserSettings = Action('UpdateUserSettings')
ValidateEnvironmentName = Action('ValidateEnvironmentName')
