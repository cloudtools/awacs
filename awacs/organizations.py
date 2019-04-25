# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Organizations'
prefix = 'organizations'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptHandshake = Action('AcceptHandshake')
AttachPolicy = Action('AttachPolicy')
CancelHandshake = Action('CancelHandshake')
CreateAccount = Action('CreateAccount')
CreateOrganization = Action('CreateOrganization')
CreateOrganizationalUnit = Action('CreateOrganizationalUnit')
CreatePolicy = Action('CreatePolicy')
DeclineHandshake = Action('DeclineHandshake')
DeleteOrganization = Action('DeleteOrganization')
DeleteOrganizationalUnit = Action('DeleteOrganizationalUnit')
DeletePolicy = Action('DeletePolicy')
DescribeAccount = Action('DescribeAccount')
DescribeCreateAccountStatus = Action('DescribeCreateAccountStatus')
DescribeHandshake = Action('DescribeHandshake')
DescribeOrganization = Action('DescribeOrganization')
DescribeOrganizationalUnit = Action('DescribeOrganizationalUnit')
DescribePolicy = Action('DescribePolicy')
DetachPolicy = Action('DetachPolicy')
DisableAWSServiceAccess = Action('DisableAWSServiceAccess')
DisablePolicyType = Action('DisablePolicyType')
EnableAWSServiceAccess = Action('EnableAWSServiceAccess')
EnableAllFeatures = Action('EnableAllFeatures')
EnablePolicyType = Action('EnablePolicyType')
InviteAccountToOrganization = Action('InviteAccountToOrganization')
LeaveOrganization = Action('LeaveOrganization')
ListAWSServiceAccessForOrganization = \
    Action('ListAWSServiceAccessForOrganization')
ListAccounts = Action('ListAccounts')
ListAccountsForParent = Action('ListAccountsForParent')
ListChildren = Action('ListChildren')
ListCreateAccountStatus = Action('ListCreateAccountStatus')
ListHandshakesForAccount = Action('ListHandshakesForAccount')
ListHandshakesForOrganization = Action('ListHandshakesForOrganization')
ListOrganizationalUnitsForParent = \
    Action('ListOrganizationalUnitsForParent')
ListParents = Action('ListParents')
ListPolicies = Action('ListPolicies')
ListPoliciesForTarget = Action('ListPoliciesForTarget')
ListRoots = Action('ListRoots')
ListTargetsForPolicy = Action('ListTargetsForPolicy')
MoveAccount = Action('MoveAccount')
RemoveAccountFromOrganization = Action('RemoveAccountFromOrganization')
UpdateOrganizationalUnit = Action('UpdateOrganizationalUnit')
UpdatePolicy = Action('UpdatePolicy')
