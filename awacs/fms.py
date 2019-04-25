# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Firewall Manager'
prefix = 'fms'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateAdminAccount = Action('AssociateAdminAccount')
DeleteNotificationChannel = Action('DeleteNotificationChannel')
DeletePolicy = Action('DeletePolicy')
DisassociateAdminAccount = Action('DisassociateAdminAccount')
GetAdminAccount = Action('GetAdminAccount')
GetComplianceDetail = Action('GetComplianceDetail')
GetNotificationChannel = Action('GetNotificationChannel')
GetPolicy = Action('GetPolicy')
ListComplianceStatus = Action('ListComplianceStatus')
ListMemberAccounts = Action('ListMemberAccounts')
ListPolicies = Action('ListPolicies')
PutNotificationChannel = Action('PutNotificationChannel')
PutPolicy = Action('PutPolicy')
