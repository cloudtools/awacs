# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Cognito Identity'
prefix = 'cognito-identity'

CreateIdentityPool = Action(prefix, 'CreateIdentityPool')
DeleteIdentityPool = Action(prefix, 'DeleteIdentityPool')
DescribeIdentityPool = Action(prefix, 'DescribeIdentityPool')
ListIdentities = Action(prefix, 'ListIdentities')
ListIdentityPools = Action(prefix, 'ListIdentityPools')
UpdateIdentityPool = Action(prefix, 'UpdateIdentityPool')
