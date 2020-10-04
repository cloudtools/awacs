# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Lake Formation'
prefix = 'lakeformation'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGrantPermissions = Action('BatchGrantPermissions')
BatchRevokePermissions = Action('BatchRevokePermissions')
DeregisterResource = Action('DeregisterResource')
DescribeResource = Action('DescribeResource')
GetDataAccess = Action('GetDataAccess')
GetDataLakeSettings = Action('GetDataLakeSettings')
GetEffectivePermissionsForPath = Action('GetEffectivePermissionsForPath')
GrantPermissions = Action('GrantPermissions')
ListPermissions = Action('ListPermissions')
ListResources = Action('ListResources')
PutDataLakeSettings = Action('PutDataLakeSettings')
RegisterResource = Action('RegisterResource')
RevokePermissions = Action('RevokePermissions')
UpdateResource = Action('UpdateResource')
