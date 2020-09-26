# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Marketplace'
prefix = 'aws-marketplace'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptAgreementApprovalRequest = Action('AcceptAgreementApprovalRequest')
CancelAgreementRequest = Action('CancelAgreementRequest')
DescribeAgreement = Action('DescribeAgreement')
GetAgreementApprovalRequest = Action('GetAgreementApprovalRequest')
GetAgreementRequest = Action('GetAgreementRequest')
GetAgreementTerms = Action('GetAgreementTerms')
ListAgreementApprovalRequests = Action('ListAgreementApprovalRequests')
ListAgreementRequests = Action('ListAgreementRequests')
RegisterUsage = Action('RegisterUsage')
RejectAgreementApprovalRequest = Action('RejectAgreementApprovalRequest')
SearchAgreements = Action('SearchAgreements')
Subscribe = Action('Subscribe')
Unsubscribe = Action('Unsubscribe')
UpdateAgreementApprovalRequest = Action('UpdateAgreementApprovalRequest')
ViewSubscriptions = Action('ViewSubscriptions')
AcceptAgreementApprovalRequest = Action('AcceptAgreementApprovalRequest')
BatchMeterUsage = Action('BatchMeterUsage')
CancelAgreementRequest = Action('CancelAgreementRequest')
DescribeAgreement = Action('DescribeAgreement')
GetAgreementApprovalRequest = Action('GetAgreementApprovalRequest')
GetAgreementRequest = Action('GetAgreementRequest')
GetAgreementTerms = Action('GetAgreementTerms')
ListAgreementApprovalRequests = Action('ListAgreementApprovalRequests')
ListAgreementRequests = Action('ListAgreementRequests')
MeterUsage = Action('MeterUsage')
RegisterUsage = Action('RegisterUsage')
RejectAgreementApprovalRequest = Action('RejectAgreementApprovalRequest')
ResolveCustomer = Action('ResolveCustomer')
SearchAgreements = Action('SearchAgreements')
UpdateAgreementApprovalRequest = Action('UpdateAgreementApprovalRequest')
