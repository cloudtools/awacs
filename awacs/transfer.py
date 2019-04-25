# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Transfer for SFTP'
prefix = 'transfer'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateServer = Action('CreateServer')
CreateUser = Action('CreateUser')
DeleteServer = Action('DeleteServer')
DeleteSshPublicKey = Action('DeleteSshPublicKey')
DeleteUser = Action('DeleteUser')
DescribeServer = Action('DescribeServer')
DescribeUser = Action('DescribeUser')
ImportSshPublicKey = Action('ImportSshPublicKey')
ListServers = Action('ListServers')
ListTagsForResource = Action('ListTagsForResource')
ListUsers = Action('ListUsers')
StartServer = Action('StartServer')
StopServer = Action('StopServer')
TagResource = Action('TagResource')
TestIdentityProvider = Action('TestIdentityProvider')
UntagResource = Action('UntagResource')
UpdateServer = Action('UpdateServer')
UpdateUser = Action('UpdateUser')
