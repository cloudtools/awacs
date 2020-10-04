# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Service Quotas'
prefix = 'servicequotas'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateServiceQuotaTemplate = Action('AssociateServiceQuotaTemplate')
DeleteServiceQuotaIncreaseRequestFromTemplate = \
    Action('DeleteServiceQuotaIncreaseRequestFromTemplate')
DisassociateServiceQuotaTemplate = \
    Action('DisassociateServiceQuotaTemplate')
GetAWSDefaultServiceQuota = Action('GetAWSDefaultServiceQuota')
GetAssociationForServiceQuotaTemplate = \
    Action('GetAssociationForServiceQuotaTemplate')
GetRequestedServiceQuotaChange = Action('GetRequestedServiceQuotaChange')
GetServiceQuota = Action('GetServiceQuota')
GetServiceQuotaIncreaseRequestFromTemplate = \
    Action('GetServiceQuotaIncreaseRequestFromTemplate')
ListAWSDefaultServiceQuotas = Action('ListAWSDefaultServiceQuotas')
ListRequestedServiceQuotaChangeHistory = \
    Action('ListRequestedServiceQuotaChangeHistory')
ListRequestedServiceQuotaChangeHistoryByQuota = \
    Action('ListRequestedServiceQuotaChangeHistoryByQuota')
ListServiceQuotaIncreaseRequestsInTemplate = \
    Action('ListServiceQuotaIncreaseRequestsInTemplate')
ListServiceQuotas = Action('ListServiceQuotas')
ListServices = Action('ListServices')
PutServiceQuotaIncreaseRequestIntoTemplate = \
    Action('PutServiceQuotaIncreaseRequestIntoTemplate')
RequestServiceQuotaIncrease = Action('RequestServiceQuotaIncrease')
