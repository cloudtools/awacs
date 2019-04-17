# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Cognito Identity'
prefix = 'cognito-identity'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateIdentityPool = Action('CreateIdentityPool')
DeleteIdentities = Action('DeleteIdentities')
DeleteIdentityPool = Action('DeleteIdentityPool')
DescribeIdentity = Action('DescribeIdentity')
DescribeIdentityPool = Action('DescribeIdentityPool')
GetCredentialsForIdentity = Action('GetCredentialsForIdentity')
GetId = Action('GetId')
GetIdentityPoolRoles = Action('GetIdentityPoolRoles')
GetOpenIdToken = Action('GetOpenIdToken')
GetOpenIdTokenForDeveloperIdentity = \
    Action('GetOpenIdTokenForDeveloperIdentity')
ListIdentities = Action('ListIdentities')
ListIdentityPools = Action('ListIdentityPools')
ListTagsForResource = Action('ListTagsForResource')
LookupDeveloperIdentity = Action('LookupDeveloperIdentity')
MergeDeveloperIdentities = Action('MergeDeveloperIdentities')
SetIdentityPoolRoles = Action('SetIdentityPoolRoles')
TagResource = Action('TagResource')
UnlinkDeveloperIdentity = Action('UnlinkDeveloperIdentity')
UnlinkIdentity = Action('UnlinkIdentity')
UntagResource = Action('UntagResource')
UpdateIdentityPool = Action('UpdateIdentityPool')
